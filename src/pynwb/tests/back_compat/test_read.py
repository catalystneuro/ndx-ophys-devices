"""Read a file written with ndx-ophys-devices 0.3.1, whose types and attributes 0.4.0 replaced."""

import warnings
from pathlib import Path

import pytest
from pynwb import NWBHDF5IO, validate

from ndx_ophys_devices import (
    FiberInsertion,
    LensPositioning,
    OpticalFiber,
    OpticalLens,
    OpticalLensModel,
    PhotodetectorModel,
    ViralVectorInjection,
)
from ndx_ophys_devices.testing import mock_ViralVector

FILE_PATH = Path(__file__).parent / "0.3.1_changed_types.nwb"


@pytest.fixture(scope="module")
def nwbfile():
    with warnings.catch_warnings():
        warnings.filterwarnings("ignore", message=r"Ignoring the following cached namespace.*", category=UserWarning)
        with NWBHDF5IO(FILE_PATH, "r") as io:
            yield io.read()


def test_viral_vector_injection_coordinates(nwbfile):
    injection = nwbfile.lab_meta_data["molecular_tools"].viral_vector_injections["ViralVectorInjection"]
    assert injection.viral_injection_coordinates is None
    assert injection.location == "Dorsal CA1"
    assert injection.hemisphere == "left"
    assert injection.reference == "Bregma at the cortical surface"
    assert (injection.ap_in_mm, injection.ml_in_mm, injection.dv_in_mm) == (-2.0, -1.5, -1.25)
    assert (injection.pitch_in_deg, injection.yaw_in_deg, injection.roll_in_deg) == (10.0, 0.0, 0.0)
    assert injection.stereotactic_rotation_in_deg == 5.0
    assert injection.stereotactic_tilt_in_deg == 2.0


def test_optical_fiber_insertion(nwbfile):
    fiber_insertion = nwbfile.devices["OpticalFiber"].fiber_insertion
    assert isinstance(fiber_insertion, FiberInsertion)
    assert fiber_insertion.insertion_position_ap_in_mm == -3.0
    assert fiber_insertion.insertion_position_ml_in_mm == -1.0
    assert fiber_insertion.insertion_position_dv_in_mm == 0.0
    assert fiber_insertion.depth_in_mm == 4.0
    assert fiber_insertion.position_reference == "Bregma at the cortical surface"
    assert fiber_insertion.hemisphere == "left"
    assert fiber_insertion.insertion_angle_roll_in_deg == 10.0


def test_optical_lens(nwbfile):
    optical_lens = nwbfile.devices["OpticalLens"]
    assert isinstance(optical_lens, OpticalLens)
    assert isinstance(optical_lens.model, OpticalLensModel)
    assert optical_lens.model.numerical_aperture == 0.5
    assert isinstance(optical_lens.lens_positioning, LensPositioning)
    assert optical_lens.lens_positioning.positioning_type == "inserted"
    assert optical_lens.lens_positioning.target_position_dv_in_mm == -2.0
    assert optical_lens.lens_positioning.depth_in_mm == 2.0


def test_photodetector_model_gain(nwbfile):
    photodetector_model = nwbfile.devices["Photodetector"].model
    assert photodetector_model.gain == 100.0
    assert photodetector_model.gain_unit == "V/W"


def test_new_optical_fiber_rejects_fiber_insertion():
    fiber_insertion = FiberInsertion(name="fiber_insertion", depth_in_mm=4.0)
    with pytest.raises(TypeError, match="replaced by StereotacticPosition"):
        OpticalFiber(name="OpticalFiber", fiber_insertion=fiber_insertion)


def test_new_viral_vector_injection_rejects_deprecated_coordinates():
    with pytest.raises(TypeError, match="passed to ViralVectorInjection: ap_in_mm"):
        ViralVectorInjection(
            name="ViralVectorInjection", volume_in_uL=0.45, viral_vector=mock_ViralVector(), ap_in_mm=-2.0
        )


def test_new_photodetector_model_rejects_gain():
    with pytest.raises(TypeError, match="passed to PhotodetectorModel: gain"):
        PhotodetectorModel(name="PhotodetectorModel", manufacturer="Hamamatsu", detector_type="PMT", gain=100.0)


def test_read_validates_without_unexpected_warnings():
    with warnings.catch_warnings(record=True) as warnings_on_read:
        warnings.simplefilter("always")
        with NWBHDF5IO(FILE_PATH, "r") as io:
            errors = validate(io=io)
            io.read()
    unexpected_warnings = [
        str(w.message)
        for w in warnings_on_read
        if not str(w.message).startswith("Ignoring the following cached namespace")
    ]
    assert unexpected_warnings == []
    assert errors == []
