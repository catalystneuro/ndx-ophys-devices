from pynwb import NWBFile
from pynwb.testing.mock.file import mock_NWBFile
import pytest

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
    optical_lens_model = mock_OpticalLensModel()

    # Create devices with models
    mock_OpticalFiber(model=optical_fiber_model)
    mock_ExcitationSource(model=excitation_source_model)
    mock_PulsedExcitationSource(model=excitation_source_model)
    mock_Photodetector(model=photodetector_model)
    mock_DichroicMirror(model=dichroic_mirror_model)
    mock_OpticalFilter(model=optical_filter_model)
    mock_BandOpticalFilter(model=band_optical_filter_model)
    mock_EdgeOpticalFilter(model=edge_optical_filter_model)
    mock_OpticalLens(model=optical_lens_model)

    return nwbfile


def set_up_nwbfile(nwbfile: NWBFile = None):
    """Create an NWBFile"""
    nwbfile = nwbfile or mock_NWBFile()
    return nwbfile
