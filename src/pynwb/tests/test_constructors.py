"""Test in-memory Python API constructors for ndx-ophys-devices extension."""

import pytest

from ndx_ophys_devices.testing import (
    mock_DeviceModel,
    mock_DeviceInstance,
    mock_ViralVector,
    mock_ViralVectorInjection,
    mock_Indicator,
    mock_Effector,
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
    mock_LensPositioning,
    mock_FiberInsertion,
)


def test_constructor_device_model():
    mock_DeviceModel()


def test_constructor_device_instance():
    model = mock_DeviceModel()
    mock_DeviceInstance(model=model)

def test_constructor_viral_vector():
    mock_ViralVector()

def test_constructor_viral_vector_injection():
    mock_ViralVectorInjection()

def test_constructor_indicator():
    mock_Indicator()


def test_constructor_effector():
    mock_Effector()


def test_constructor_optical_fiber_model():
    mock_OpticalFiberModel()


def test_constructor_optical_fiber():
    mock_OpticalFiber()


def test_constructor_photodetector_model():
    mock_PhotodetectorModel()


def test_constructor_photodetector():
    mock_Photodetector()


def test_constructor_dichroic_mirror_model():
    mock_DichroicMirrorModel()


def test_constructor_dichroic_mirror():
    mock_DichroicMirror()


def test_constructor_optical_filter_model():
    mock_OpticalFilterModel()


def test_constructor_optical_filter():
    mock_OpticalFilter()


def test_constructor_band_optical_filter_model():
    mock_BandOpticalFilterModel()


def test_constructor_band_optical_filter():
    mock_BandOpticalFilter()


def test_constructor_edge_optical_filter_model():
    mock_EdgeOpticalFilterModel()


def test_constructor_edge_optical_filter():
    mock_EdgeOpticalFilter()


def test_constructor_optical_lens_model():
    mock_OpticalLensModel()


def test_constructor_optical_lens():
    mock_OpticalLens()


def test_constructor_excitation_source_model():
    mock_ExcitationSourceModel()


def test_constructor_excitation_source():
    mock_ExcitationSource()


def test_constructor_pulsed_excitation_source():
    mock_PulsedExcitationSource()


def test_constructor_lens_positioning():
    mock_LensPositioning()


def test_constructor_fiber_insertion():
    mock_FiberInsertion()


if __name__ == "__main__":
    pytest.main()  # Required since not a typical package structure
