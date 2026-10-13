"""Roundtrip (write, read, validate) tests for ndx-ophys-devices."""

from datetime import datetime

import pytest
from pytz import UTC
from pynwb import NWBHDF5IO, get_class, load_namespaces, validate
from pynwb.spec import NWBGroupSpec, NWBNamespaceBuilder
from pynwb.testing import TestCase
from pynwb.testing.mock.file import mock_NWBFile

from ndx_ophys_devices.testing import (
    mock_BandOpticalFilter,
    mock_BandOpticalFilterModel,
    mock_DichroicMirror,
    mock_DichroicMirrorModel,
    mock_EdgeOpticalFilter,
    mock_EdgeOpticalFilterModel,
    mock_Effector,
    mock_ExcitationSource,
    mock_ExcitationSourceModel,
    mock_Indicator,
    mock_ObjectiveLens,
    mock_ObjectiveLensModel,
    mock_OpticalFiber,
    mock_OpticalFiberModel,
    mock_OpticalFilter,
    mock_OpticalFilterModel,
    mock_Photodetector,
    mock_PhotodetectorModel,
    mock_PulsedExcitationSource,
    mock_StereotacticPosition,
    mock_ViralVector,
    mock_ViralVectorInjection,
)

MOLECULAR_TOOL_TYPES = ("ViralVector", "ViralVectorInjection", "Indicator", "Effector")


@pytest.fixture(scope="module")
def MolecularToolsMetadata(tmp_path_factory):
    """A test-only LabMetaData that holds the molecular tool containers.

    The containers cannot be added to an NWB file directly; the experiment extensions provide a
    LabMetaData for them. This minimal one lets us roundtrip them here.
    """
    namespace_name = "ndx-ophys-devices-testing"
    output_dir = tmp_path_factory.mktemp("spec")
    builder = NWBNamespaceBuilder(
        doc="Test-only namespace", name=namespace_name, version="0.1.0", author="test", contact="test"
    )
    builder.include_type("LabMetaData", namespace="core")
    for neurodata_type in MOLECULAR_TOOL_TYPES:
        builder.include_type(neurodata_type, namespace="ndx-ophys-devices")
    metadata_spec = NWBGroupSpec(
        neurodata_type_def="MolecularToolsMetadata",
        neurodata_type_inc="LabMetaData",
        doc="Holds molecular tool containers for testing.",
        groups=[
            NWBGroupSpec(neurodata_type_inc=neurodata_type, doc=f"{neurodata_type} objects.", quantity="*")
            for neurodata_type in MOLECULAR_TOOL_TYPES
        ],
    )
    builder.add_spec(f"{namespace_name}.extensions.yaml", metadata_spec)
    builder.export(f"{namespace_name}.namespace.yaml", outdir=str(output_dir))
    load_namespaces(str(output_dir / f"{namespace_name}.namespace.yaml"))
    return get_class("MolecularToolsMetadata", namespace_name)


def write_read_and_validate(nwbfile, path):
    with NWBHDF5IO(path=path, mode="w") as io:
        io.write(nwbfile)
    assert validate(path=str(path)) == []
    io = NWBHDF5IO(path=path, mode="r")
    return io, io.read()


class TestDevicesRoundtrip(TestCase):
    """Every device type, linked to its model, survives a write and read."""

    def setUp(self):
        self.nwbfile_path = "test_ophys_devices_roundtrip.nwb"

    def tearDown(self):
        from pynwb.testing import remove_test_file

        remove_test_file(self.nwbfile_path)

    def test_roundtrip(self):
        nwbfile = mock_NWBFile(session_start_time=datetime(2000, 1, 1, tzinfo=UTC))
        models = {
            "photodetector": mock_PhotodetectorModel(name="PhotodetectorModel"),
            "dichroic_mirror": mock_DichroicMirrorModel(name="DichroicMirrorModel"),
            "optical_filter": mock_OpticalFilterModel(name="OpticalFilterModel"),
            "band_optical_filter": mock_BandOpticalFilterModel(name="BandOpticalFilterModel"),
            "edge_optical_filter": mock_EdgeOpticalFilterModel(name="EdgeOpticalFilterModel"),
            "optical_fiber": mock_OpticalFiberModel(name="OpticalFiberModel"),
            "objective_lens": mock_ObjectiveLensModel(name="ObjectiveLensModel"),
            "excitation_source": mock_ExcitationSourceModel(name="ExcitationSourceModel"),
            "pulsed_excitation_source": mock_ExcitationSourceModel(
                name="PulsedExcitationSourceModel", excitation_mode="two-photon"
            ),
        }
        for model in models.values():
            nwbfile.add_device_model(model)

        devices = [
            mock_Photodetector(name="Photodetector", model=models["photodetector"]),
            mock_DichroicMirror(name="DichroicMirror", model=models["dichroic_mirror"]),
            mock_OpticalFilter(name="OpticalFilter", model=models["optical_filter"]),
            mock_BandOpticalFilter(name="BandOpticalFilter", model=models["band_optical_filter"]),
            mock_EdgeOpticalFilter(name="EdgeOpticalFilter", model=models["edge_optical_filter"]),
            mock_OpticalFiber(name="OpticalFiber", model=models["optical_fiber"]),
            mock_OpticalFiber(name="PatchCord", model=models["optical_fiber"], fiber_insertion=None),
            mock_OpticalFiber(
                name="AngledFiber",
                model=models["optical_fiber"],
                fiber_insertion=mock_StereotacticPosition(
                    name="fiber_insertion", roll_in_deg=10.0, pitch_in_deg=None, yaw_in_deg=None
                ),
            ),
            mock_ObjectiveLens(name="ObjectiveLens", model=models["objective_lens"]),
            mock_ObjectiveLens(name="ObjectiveLensNotImplanted", model=models["objective_lens"], lens_positioning=None),
            mock_ExcitationSource(name="ExcitationSource", model=models["excitation_source"]),
            mock_PulsedExcitationSource(name="PulsedExcitationSource", model=models["pulsed_excitation_source"]),
        ]
        for device in devices:
            nwbfile.add_device(device)

        io, read_nwbfile = write_read_and_validate(nwbfile, self.nwbfile_path)
        with io:
            for device in devices:
                self.assertContainerEqual(device, read_nwbfile.devices[device.name])
            self.assertIsNone(read_nwbfile.devices["PatchCord"].fiber_insertion)
            self.assertIsNone(read_nwbfile.devices["AngledFiber"].fiber_insertion.pitch_in_deg)
            self.assertEqual(read_nwbfile.devices["Photodetector"].gain, 1.0e6)


def test_molecular_tools_roundtrip(MolecularToolsMetadata, tmp_path):
    """ViralVector, ViralVectorInjection, Indicator and Effector survive a write and read, with their links."""
    nwbfile = mock_NWBFile(session_start_time=datetime(2000, 1, 1, tzinfo=UTC))

    viral_vector = mock_ViralVector(name="ViralVector")
    injection = mock_ViralVectorInjection(name="ViralVectorInjection", viral_vector=viral_vector)
    injection_without_coordinates = mock_ViralVectorInjection(
        name="ViralVectorInjectionWithoutCoordinates", viral_vector=viral_vector, viral_injection_coordinates=None
    )
    indicator = mock_Indicator(name="Indicator", viral_vector_injection=injection)
    effector = mock_Effector(name="Effector", viral_vector_injection=injection)
    transgenic_indicator = mock_Indicator(name="TransgenicIndicator", viral_vector_injection=None)

    nwbfile.add_lab_meta_data(
        MolecularToolsMetadata(
            name="molecular_tools",
            viral_vectors=[viral_vector],
            viral_vector_injections=[injection, injection_without_coordinates],
            indicators=[indicator, transgenic_indicator],
            effectors=[effector],
        )
    )

    io, read_nwbfile = write_read_and_validate(nwbfile, tmp_path / "molecular_tools.nwb")
    with io:
        read_metadata = read_nwbfile.lab_meta_data["molecular_tools"]
        read_injection = read_metadata.viral_vector_injections["ViralVectorInjection"]

        assert read_injection.viral_injection_coordinates.anatomical_target == "Dorsal CA1"
        assert read_injection.viral_injection_coordinates.z_in_mm == -1.5
        assert read_injection.viral_vector is read_metadata.viral_vectors["ViralVector"]
        read_injection_without_coordinates = read_metadata.viral_vector_injections[
            "ViralVectorInjectionWithoutCoordinates"
        ]
        assert read_injection_without_coordinates.viral_injection_coordinates is None
        assert read_metadata.indicators["Indicator"].viral_vector_injection is read_injection
        assert read_metadata.effectors["Effector"].viral_vector_injection is read_injection
        assert read_metadata.indicators["TransgenicIndicator"].viral_vector_injection is None
