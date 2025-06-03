from datetime import datetime

from pytz import UTC
from pynwb.testing import TestCase as pynwb_TestCase
from pynwb.testing.mock.file import mock_NWBFile

import pynwb

from ndx_ophys_devices.testing import (
    mock_OpticalFiberModel,
    mock_OpticalFiber,
    mock_PhotodetectorModel,
    mock_Photodetector,
    mock_DichroicMirrorModel,
    mock_DichroicMirror,
    mock_OpticalFilterModel,
    mock_OpticalFilter,
    mock_BandOpticalFilterModel,
    mock_BandOpticalFilter,
    mock_EdgeOpticalFilterModel,
    mock_EdgeOpticalFilter,
    mock_OpticalLensModel,
    mock_OpticalLens,
    mock_ExcitationSourceModel,
    mock_ExcitationSource,
    mock_PulsedExcitationSource,
)


class TestOphysDevicesSimpleRoundtrip(pynwb_TestCase):
    """
    Simple roundtrip test for OphysDevices.

    This test creates various optical physiology devices, adds them to an NWBFile,
    writes the file to disk, reads it back, and verifies that all devices are
    correctly preserved in the roundtrip process.
    """

    def setUp(self):
        self.nwbfile_path = "test_ophys_devices_roundtrip.nwb"

    def tearDown(self):
        pynwb.testing.remove_test_file(self.nwbfile_path)

    def test_roundtrip(self):
        """Test that all optical physiology devices can be written to and read from an NWB file."""
        # Create a mock NWBFile
        nwbfile = mock_NWBFile(session_start_time=datetime(2000, 1, 1, tzinfo=UTC))

        photodetector_model = mock_PhotodetectorModel(name="PhotodetectorModel")
        nwbfile.add_device(devices=photodetector_model)
        dichroic_mirror_model = mock_DichroicMirrorModel(name="DichroicMirrorModel")
        nwbfile.add_device(devices=dichroic_mirror_model)
        optical_filter_model = mock_OpticalFilterModel(name="OpticalFilterModel")
        nwbfile.add_device(devices=optical_filter_model)
        band_optical_filter_model = mock_BandOpticalFilterModel(name="BandOpticalFilterModel")
        nwbfile.add_device(devices=band_optical_filter_model)
        edge_optical_filter_model = mock_EdgeOpticalFilterModel(name="EdgeOpticalFilterModel")
        nwbfile.add_device(devices=edge_optical_filter_model)
        optical_fiber_model = mock_OpticalFiberModel(name="OpticalFiberModel")
        nwbfile.add_device(devices=optical_fiber_model)
        optical_lens_model = mock_OpticalLensModel(name="OpticalLensModel")
        nwbfile.add_device(devices=optical_lens_model)
        excitation_source_model = mock_ExcitationSourceModel(name="ExcitationSourceModel")
        nwbfile.add_device(devices=excitation_source_model)
        pulsed_excitation_source_model = mock_ExcitationSourceModel(name="PulsedExcitationSourceModel")
        nwbfile.add_device(devices=pulsed_excitation_source_model)

        # Create a dictionary of devices to test
        devices = {
            "photodetector": mock_Photodetector(name="Photodetector", model=photodetector_model),
            "dichroic_mirror": mock_DichroicMirror(name="DichroicMirror", model=dichroic_mirror_model),
            "optical_filter": mock_OpticalFilter(name="OpticalFilter", model=optical_filter_model),
            "band_optical_filter": mock_BandOpticalFilter(name="BandOpticalFilter", model=band_optical_filter_model),
            "edge_optical_filter": mock_EdgeOpticalFilter(name="EdgeOpticalFilter", model=edge_optical_filter_model),
            "optical_fiber": mock_OpticalFiber(name="OpticalFiber", model=optical_fiber_model),
            "optical_lens": mock_OpticalLens(name="OpticalLens", model=optical_lens_model),
            "excitation_source": mock_ExcitationSource(name="ExcitationSource", model=excitation_source_model),
            "pulsed_excitation_source": mock_PulsedExcitationSource(
                name="PulsedExcitationSource", model=pulsed_excitation_source_model
            ),
        }

        # Add all devices to the NWBFile
        for device in devices.values():
            nwbfile.add_device(devices=device)

        # Write the NWBFile to disk
        with pynwb.NWBHDF5IO(path=self.nwbfile_path, mode="w") as io:
            io.write(nwbfile)

        # Read the NWBFile back from disk
        with pynwb.NWBHDF5IO(path=self.nwbfile_path, mode="r", load_namespaces=True) as io:
            read_nwbfile = io.read()

            # Verify that all devices are correctly preserved in the roundtrip
            for device in devices.values():
                self.assertContainerEqual(device, read_nwbfile.devices[device.name])
