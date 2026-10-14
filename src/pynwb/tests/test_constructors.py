"""Test in-memory Python API constructors for ndx-ophys-devices extension."""

import pytest

import ndx_ophys_devices.testing as testing
from ndx_ophys_devices.testing import (
    mock_ExcitationSource,
    mock_OpticalFiber,
    mock_Photodetector,
    mock_PulsedExcitationSource,
    mock_StereotacticPosition,
)


@pytest.mark.parametrize("mock_name", testing.__all__)
def test_constructor(mock_name):
    """Every mock function builds an instance of the type it is named after."""
    neurodata_type = mock_name.removeprefix("mock_")
    instance = getattr(testing, mock_name)()
    assert type(instance).__name__ == neurodata_type


def test_device_links_its_model():
    photodetector = mock_Photodetector()
    assert photodetector.model.detector_type == "PMT"


def test_photodetector_gain_is_set_on_the_instance():
    photodetector = mock_Photodetector(gain=2.0e10, gain_unit="V/W")
    assert photodetector.gain == 2.0e10
    assert photodetector.gain_unit == "V/W"
    assert not hasattr(photodetector.model, "gain")


def test_optical_fiber_without_fiber_insertion():
    optical_fiber = mock_OpticalFiber(fiber_insertion=None)
    assert optical_fiber.fiber_insertion is None


def test_fiber_insertion_requires_its_fixed_name():
    with pytest.raises(ValueError, match="must be named 'fiber_insertion'"):
        mock_OpticalFiber(fiber_insertion=mock_StereotacticPosition(name="tip"))


def test_stereotactic_position_angles_are_optional():
    position = mock_StereotacticPosition(pitch_in_deg=None, yaw_in_deg=None, roll_in_deg=None)
    assert position.pitch_in_deg is None


def test_pulsed_excitation_source_is_an_excitation_source():
    pulsed_excitation_source = mock_PulsedExcitationSource()
    assert isinstance(pulsed_excitation_source, type(mock_ExcitationSource()))
    assert pulsed_excitation_source.pulse_width_in_s == 1.4e-13
