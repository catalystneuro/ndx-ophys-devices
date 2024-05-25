"""Test in-memory Python API constructors for ndx-ophys-devices extension."""

import pytest

from ndx_ophys_devices.testing import (
    mock_Indicator,
    mock_Effector,
    mock_OpticalFiber,
    mock_Photodetector,
    mock_DichroicMirror,
    mock_BandOpticalFilter,
    mock_EdgeOpticalFilter,
    mock_ObjectiveLens,
    mock_ExcitationSource,
    mock_Microscope,
)


def test_constructor_indicator():
    mock_Indicator()


def test_constructor_effector():
    mock_Effector()


def test_constructor_optical_fiber():
    mock_OpticalFiber()


def test_constructor_photodetector():
    mock_Photodetector()


def test_constructor_dichroic_mirror():
    mock_DichroicMirror()


def test_constructor_band_optical_filter():
    mock_BandOpticalFilter()


def test_constructor_edge_optical_filter():
    mock_EdgeOpticalFilter()


def test_constructor_objective_lens():
    mock_ObjectiveLens()

def test_constructor_microscope():
    mock_Microscope()


def test_constructor_excitation_source():
    mock_ExcitationSource()

if __name__ == "__main__":
    pytest.main()  # Required since not a typical package structure
