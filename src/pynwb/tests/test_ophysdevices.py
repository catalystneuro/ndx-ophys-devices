from pynwb import NWBHDF5IO, NWBFile
from pynwb.testing import TestCase, remove_test_file
from pynwb.testing.mock.file import mock_NWBFile

from ndx_ophys_devices import (
    Indicator,
    OpticalFiber,
    ExcitationSource,
    Photodetector,
    DichroicMirror,
    BandOpticalFilter,
    EdgeOpticalFilter,
    ObjectiveLens,
    Effector,
    Microscope,
)


def set_up_nwbfile(nwbfile: NWBFile = None):
    """Create an NWBFile."""
    nwbfile = nwbfile or mock_NWBFile()
    return nwbfile


class TestIntegrationRoundtrip(TestCase):
    """
    Full Roundtrip Integration Test
    Creates, writes, and reads instances of:
        Indicator,
        OpticalFiber,
        ExcitationSource,
        Photodetector,
        DichroicMirror,
        BandOpticalFilter,
        EdgeOpticalFilter,
        ObjectiveLens,
        Effector,
        Microscope,
    """

    def setUp(self):
        self.nwbfile = set_up_nwbfile()
        self.path = "test.nwb"

    def tearDown(self):
        remove_test_file(self.path)

    def test_roundtrip(self):

        indicator = Indicator(
            name="indicator",
            description="Green indicator",
            label="GCamp6f",
            injection_location="VTA",
            injection_coordinates_in_mm=(3.0, 2.0, 1.0),
        )
        optical_fiber = OpticalFiber(
            name="optical_fiber",
            model="fiber_model",
            numerical_aperture=0.2,
            core_diameter_in_um=400.0,
        )
        excitation_source = ExcitationSource(
            name="excitation_source",
            description="excitation sources for green indicator",
            model="laser model",
            illumination_type="laser",
            excitation_wavelength_in_nm=470.0,
            peak_power_in_W=0.7,
            peak_pulse_energy_in_J=1.,
            intensity_in_W_per_m2=1.,
            pulse_rate_in_Hz=5e8,
            exposure_time_in_s=1/5e8,
        )
        photodetector = Photodetector(
            name="photodetector",
            description="photodetector for green emission",
            detector_type="PMT",
            detected_wavelength_in_nm=520.0,
            gain=100.0,
        )
        dichroic_mirror = DichroicMirror(
            name="dichroic_mirror",
            description="Dichroic mirror for green indicator",
            model="dicdichroic mirror model",
            cut_on_wavelength_in_nm=470.0,
            cut_off_wavelength_in_nm=500.0,
            reflection_bandwidth_in_nm=50.0,
            transmission_bandwidth_in_nm=50.0,
            angle_of_incidence_in_degrees=45.0,
        )
        band_optical_filter = BandOpticalFilter(
            name="band_optical_filter",
            description="emission filter for green indicator",
            model="emission filter model",
            center_wavelength_in_nm=505.0,
            bandwidth_in_nm=30.0,  # 505±15nm
            filter_type="Bandpass",
        )
        edge_optical_filter = EdgeOpticalFilter(
            name="edge_optical_filter",
            description="emission filter for red indicator",
            model="emission filter model",
            cut_wavelength_in_nm=585.0,
            slope_in_percent_cut_wavelength=1.0,
            slope_starting_transmission_in_percent=10.0,
            slope_ending_transmission_in_percent=80.0,
            filter_type="Longpass",
        )
        opsin = Effector(
            name="opsin",
            description="Red opsin",
            label="ChroME2s",
            injection_location="VTA",
            injection_coordinates_in_mm=(3.0, 2.0, 1.0),
        )
        objective_lens = ObjectiveLens(
            name="objective_lens",
            model="objective model",
            numerical_aperture=0.2,
            magnification=10.0,
        )  
        microscope = Microscope(
            name="microscope",
            model="Microscope model",
            microscopy_type="Two photon",
        )       
        self.nwbfile.add_device(indicator)
        self.nwbfile.add_device(optical_fiber)
        self.nwbfile.add_device(excitation_source)
        self.nwbfile.add_device(photodetector)
        self.nwbfile.add_device(dichroic_mirror)
        self.nwbfile.add_device(band_optical_filter)
        self.nwbfile.add_device(edge_optical_filter)
        self.nwbfile.add_device(opsin)
        self.nwbfile.add_device(objective_lens)
        self.nwbfile.add_device(microscope)

        with NWBHDF5IO(self.path, mode="w") as io:
            io.write(self.nwbfile)

        with NWBHDF5IO(self.path, mode="r", load_namespaces=True) as io:
            read_nwbfile = io.read()
            self.assertContainerEqual(
                self.nwbfile.devices["indicator"], read_nwbfile.devices["indicator"]
            )
            self.assertContainerEqual(
                self.nwbfile.devices["optical_fiber"], read_nwbfile.devices["optical_fiber"]
            )
            self.assertContainerEqual(
                self.nwbfile.devices["excitation_source"], read_nwbfile.devices["excitation_source"]
            )
            self.assertContainerEqual(
                self.nwbfile.devices["photodetector"], read_nwbfile.devices["photodetector"]
            )
            self.assertContainerEqual(
                self.nwbfile.devices["dichroic_mirror"], read_nwbfile.devices["dichroic_mirror"]
            )
            self.assertContainerEqual(
                self.nwbfile.devices["band_optical_filter"], read_nwbfile.devices["band_optical_filter"]
            )
            self.assertContainerEqual(
                self.nwbfile.devices["edge_optical_filter"], read_nwbfile.devices["edge_optical_filter"]
            )
            self.assertContainerEqual(
                self.nwbfile.devices["opsin"], read_nwbfile.devices["opsin"]
            )
            self.assertContainerEqual(
                self.nwbfile.devices["objective_lens"], read_nwbfile.devices["objective_lens"]
            )
            self.assertContainerEqual(
                self.nwbfile.devices["microscope"], read_nwbfile.devices["microscope"]
            )
