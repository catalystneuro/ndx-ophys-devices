from pynwb import NWBFile
from pynwb.testing.mock.file import mock_NWBFile
import pytest

from ndx_ophys_devices.testing import (
    mock_DeviceModel,
    mock_DeviceInstance,
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
    mock_ObjectiveLensModel,
    mock_ObjectiveLens,
    mock_ExcitationSourceModel,
    mock_ExcitationSource,
    mock_PulsedExcitationSource,
)


def test_constructor_device_model():
    mock_DeviceModel()


def test_constructor_device_instance():
    mock_DeviceInstance()
    model = mock_DeviceModel()
    mock_DeviceInstance(model=model)


def test_constructor_indicator():
    mock_Indicator()


def test_constructor_effector():
    mock_Effector()


def test_constructor_optical_fiber_model():
    mock_OpticalFiberModel()


def test_constructor_optical_fiber():
    mock_OpticalFiber()
    model = mock_OpticalFiberModel()
    mock_OpticalFiber(model=model)


def test_constructor_photodetector_model():
    mock_PhotodetectorModel()


def test_constructor_photodetector():
    mock_Photodetector()
    model = mock_PhotodetectorModel()
    mock_Photodetector(model=model)


def test_constructor_dichroic_mirror_model():
    mock_DichroicMirrorModel()


def test_constructor_dichroic_mirror():
    mock_DichroicMirror()
    model = mock_DichroicMirrorModel()
    mock_DichroicMirror(model=model)


def test_constructor_optical_filter_model():
    mock_OpticalFilterModel()


def test_constructor_optical_filter():
    mock_OpticalFilter()
    model = mock_OpticalFilterModel()
    mock_OpticalFilter(model=model)


def test_constructor_band_optical_filter_model():
    mock_BandOpticalFilterModel()


def test_constructor_band_optical_filter():
    mock_BandOpticalFilter()
    model = mock_BandOpticalFilterModel()
    mock_BandOpticalFilter(model=model)


def test_constructor_edge_optical_filter_model():
    mock_EdgeOpticalFilterModel()


def test_constructor_edge_optical_filter():
    mock_EdgeOpticalFilter()
    model = mock_EdgeOpticalFilterModel()
    mock_EdgeOpticalFilter(model=model)


def test_constructor_objective_lens_model():
    mock_ObjectiveLensModel()


def test_constructor_objective_lens():
    mock_ObjectiveLens()
    model = mock_ObjectiveLensModel()
    mock_ObjectiveLens(model=model)


def test_constructor_excitation_source_model():
    mock_ExcitationSourceModel()


def test_constructor_excitation_source():
    mock_ExcitationSource()
    model = mock_ExcitationSourceModel()
    mock_ExcitationSource(model=model)


def test_constructor_pulsed_excitation_source():
    mock_PulsedExcitationSource()
    model = mock_ExcitationSourceModel()
    mock_PulsedExcitationSource(model=model)


@pytest.fixture(scope="module")
def nwbfile_with_ophys_devices():
    nwbfile = mock_NWBFile()

    # Create models
    optical_fiber_model = mock_OpticalFiberModel()
    excitation_source_model = mock_ExcitationSourceModel()
    photodetector_model = mock_PhotodetectorModel()
    dichroic_mirror_model = mock_DichroicMirrorModel()
    optical_filter_model = mock_OpticalFilterModel()
    band_optical_filter_model = mock_BandOpticalFilterModel()
    edge_optical_filter_model = mock_EdgeOpticalFilterModel()
    objective_lens_model = mock_ObjectiveLensModel()

    # Create devices with models
    mock_Indicator()
    mock_OpticalFiber(model=optical_fiber_model)
    mock_ExcitationSource(model=excitation_source_model)
    mock_PulsedExcitationSource(model=excitation_source_model)
    mock_Photodetector(model=photodetector_model)
    mock_DichroicMirror(model=dichroic_mirror_model)
    mock_OpticalFilter(model=optical_filter_model)
    mock_BandOpticalFilter(model=band_optical_filter_model)
    mock_EdgeOpticalFilter(model=edge_optical_filter_model)
    mock_Effector()
    mock_ObjectiveLens(model=objective_lens_model)

    return nwbfile


def set_up_nwbfile(nwbfile: NWBFile = None):
    """Create an NWBFile"""
    nwbfile = nwbfile or mock_NWBFile()
    return nwbfile
