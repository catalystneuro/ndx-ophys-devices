from pynwb import NWBFile
from pynwb.testing.mock.file import mock_NWBFile
import pytest

from ndx_ophys_devices.testing import (
    mock_DeviceModel,
    mock_Indicator,
    mock_Effector,
    mock_OpticalFiber,
    mock_Photodetector,
    mock_DichroicMirror,
    mock_OpticalFilter,
    mock_BandOpticalFilter,
    mock_EdgeOpticalFilter,
    mock_ObjectiveLens,
    mock_ExcitationSource,
    mock_PulsedExcitationSource,
)


def test_constructor_device_model():
    mock_DeviceModel()


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


def test_constructor_optical_filter():
    mock_OpticalFilter()


def test_constructor_band_optical_filter():
    mock_BandOpticalFilter()


def test_constructor_edge_optical_filter():
    mock_EdgeOpticalFilter()


def test_constructor_objective_lens():
    mock_ObjectiveLens()


def test_constructor_excitation_source():
    mock_ExcitationSource()


def test_constructor_pulsed_excitation_source():
    mock_PulsedExcitationSource()


@pytest.fixture(scope="module")
def nwbfile_with_ophys_devices():
    nwbfile = mock_NWBFile()

    mock_DeviceModel()
    mock_Indicator()
    mock_OpticalFiber()
    mock_ExcitationSource()
    mock_PulsedExcitationSource()
    mock_Photodetector()
    mock_DichroicMirror()
    mock_OpticalFilter()
    mock_BandOpticalFilter()
    mock_EdgeOpticalFilter()
    mock_Effector()
    mock_ObjectiveLens()

    return nwbfile


def set_up_nwbfile(nwbfile: NWBFile = None):
    """Create an NWBFile"""
    nwbfile = nwbfile or mock_NWBFile()
    return nwbfile
