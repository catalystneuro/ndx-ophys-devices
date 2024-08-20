from typing import Optional

from pynwb.testing.mock.utils import name_generator

import ndx_ophys_devices


def mock_DeviceModel(
    *,
    name: Optional[str] = None,
    description: str = "This is a mock instance of a DeviceModel type to be used for rapid testing.",
    manufacturer: str = "A fake manufacturer of the mock DeviceModel.",
    model: str = "A fake model of the mock DeviceModel.",
) -> ndx_ophys_devices.DeviceModel:
    device_model = ndx_ophys_devices.DeviceModel(
        name=name or name_generator("DeviceModel"),
        description=description,
        manufacturer=manufacturer,
        model=model,
    )
    return device_model


def mock_Indicator(
    *,
    name: Optional[str] = None,
    description: str = "This is a mock instance of a Indicator type to be used for rapid testing.",
    manufacturer: str = "A fake manufacturer of the mock indicator.",
    label: str = "A fake label of the indicator.",
    injection_brain_region: str = "A fake injection brain region of the indicator.",
    injection_coordinates_in_mm: list = [3.0, 2.0, 1.0],
) -> ndx_ophys_devices.Indicator:
    indicator = ndx_ophys_devices.Indicator(
        name=name or name_generator("Indicator"),
        description=description,
        manufacturer=manufacturer,
        label=label,
        injection_brain_region=injection_brain_region,
        injection_coordinates_in_mm=injection_coordinates_in_mm,
    )
    return indicator


def mock_Effector(
    *,
    name: Optional[str] = None,
    description: str = "This is a mock instance of a Effector type to be used for rapid testing.",
    manufacturer: str = "A fake manufacturer of the mock effector.",
    label: str = "A fake label of the effector.",
    injection_brain_region: str = "A fake injection brain region of the effector.",
    injection_coordinates_in_mm: list = [3.0, 2.0, 1.0],
) -> ndx_ophys_devices.Effector:
    effector = ndx_ophys_devices.Effector(
        name=name or name_generator("Effector"),
        description=description,
        manufacturer=manufacturer,
        label=label,
        injection_brain_region=injection_brain_region,
        injection_coordinates_in_mm=injection_coordinates_in_mm,
    )
    return effector


def mock_OpticalFiber(
    *,
    name: Optional[str] = None,
    description: str = "This is a mock instance of a OpticalFiber type to be used for rapid testing.",
    manufacturer: str = "A fake manufacturer of the mock an optical fiber.",
    model: str = "A fake model of the mock an optical fiber.",
    numerical_aperture: float = 0.2,
    core_diameter_in_um: float = 400.0,
) -> ndx_ophys_devices.OpticalFiber:
    optical_fiber = ndx_ophys_devices.OpticalFiber(
        name=name or name_generator("OpticalFiber"),
        description=description,
        manufacturer=manufacturer,
        model=model,
        numerical_aperture=numerical_aperture,
        core_diameter_in_um=core_diameter_in_um,
    )
    return optical_fiber


def mock_Photodetector(
    *,
    name: Optional[str] = None,
    description: str = "This is a mock instance of a Photodetector type to be used for rapid testing.",
    manufacturer: str = "A fake manufacturer of the mock an photodetector.",
    model: str = "A fake model of the mock an photodetector.",
    detector_type: str = "PMT",
    detected_wavelength_in_nm: float = 520.0,
    gain: float = 100.0,
    gain_unit: str = "A/W",
) -> ndx_ophys_devices.Photodetector:
    photodetector = ndx_ophys_devices.Photodetector(
        name=name or name_generator("Photodetector"),
        description=description,
        manufacturer=manufacturer,
        model=model,
        detector_type=detector_type,
        detected_wavelength_in_nm=detected_wavelength_in_nm,
        gain=gain,
        gain_unit=gain_unit,
    )
    return photodetector


def mock_DichroicMirror(
    *,
    name: Optional[str] = None,
    description: str = "This is a mock instance of a DichroicMirror type to be used for rapid testing.",
    manufacturer: str = "A fake manufacturer of the mock an dichroic mirror.",
    model: str = "A fake model of the mock an dichroic mirror.",
    cut_on_wavelength_in_nm: float = 470.0,
    cut_off_wavelength_in_nm: float = 500.0,
    reflection_bandwidth_in_nm: float = 50.0,
    transmission_bandwidth_in_nm: float = 50.0,
    angle_of_incidence_in_degrees: float = 45.0,
) -> ndx_ophys_devices.DichroicMirror:
    dichroic_mirror = ndx_ophys_devices.DichroicMirror(
        name=name or name_generator("DichroicMirror"),
        description=description,
        manufacturer=manufacturer,
        model=model,
        cut_on_wavelength_in_nm=cut_on_wavelength_in_nm,
        cut_off_wavelength_in_nm=cut_off_wavelength_in_nm,
        reflection_bandwidth_in_nm=reflection_bandwidth_in_nm,
        transmission_bandwidth_in_nm=transmission_bandwidth_in_nm,
        angle_of_incidence_in_degrees=angle_of_incidence_in_degrees,
    )
    return dichroic_mirror


def mock_OpticalFilter(
    *,
    name: Optional[str] = None,
    description: str = "This is a mock instance of a OpticalFilter type to be used for rapid testing.",
    manufacturer: str = "A fake manufacturer of the mock an optical filter.",
    model: str = "A fake model of the mock an optical filter.",
    filter_type: str = "Longpass",
) -> ndx_ophys_devices.EdgeOpticalFilter:
    optical_filter = ndx_ophys_devices.OpticalFilter(
        name=name or name_generator("OpticalFilter"),
        description=description,
        manufacturer=manufacturer,
        model=model,
        filter_type=filter_type,
    )
    return optical_filter


def mock_BandOpticalFilter(
    *,
    name: Optional[str] = None,
    description: str = "This is a mock instance of a BandOpticalFilter type to be used for rapid testing.",
    manufacturer: str = "A fake manufacturer of the mock an band optical filter.",
    model: str = "A fake model of the mock an band optical filter.",
    center_wavelength_in_nm: float = 505.0,
    bandwidth_in_nm: float = 30.0,  # 505±15nm
    filter_type: str = "Bandpass",
) -> ndx_ophys_devices.BandOpticalFilter:
    band_optical_filter = ndx_ophys_devices.BandOpticalFilter(
        name=name or name_generator("BandOpticalFilter"),
        description=description,
        manufacturer=manufacturer,
        model=model,
        center_wavelength_in_nm=center_wavelength_in_nm,
        bandwidth_in_nm=bandwidth_in_nm,
        filter_type=filter_type,
    )
    return band_optical_filter


def mock_EdgeOpticalFilter(
    *,
    name: Optional[str] = None,
    description: str = "This is a mock instance of a EdgeOpticalFilter type to be used for rapid testing.",
    manufacturer: str = "A fake manufacturer of the mock an edge optical filter.",
    model: str = "A fake model of the mock an edge optical filter.",
    cut_wavelength_in_nm: float = 585.0,
    slope_in_percent_cut_wavelength: float = 1.0,
    slope_starting_transmission_in_percent: float = 10.0,
    slope_ending_transmission_in_percent: float = 80.0,
    filter_type: str = "Longpass",
) -> ndx_ophys_devices.EdgeOpticalFilter:
    edge_optical_filter = ndx_ophys_devices.EdgeOpticalFilter(
        name=name or name_generator("EdgeOpticalFilter"),
        description=description,
        manufacturer=manufacturer,
        model=model,
        cut_wavelength_in_nm=cut_wavelength_in_nm,
        slope_in_percent_cut_wavelength=slope_in_percent_cut_wavelength,
        slope_starting_transmission_in_percent=slope_starting_transmission_in_percent,
        slope_ending_transmission_in_percent=slope_ending_transmission_in_percent,
        filter_type=filter_type,
    )
    return edge_optical_filter


def mock_ObjectiveLens(
    *,
    name: Optional[str] = None,
    description: str = "This is a mock instance of a ObjectiveLens type to be used for rapid testing.",
    manufacturer: str = "A fake manufacturer of the mock an objective lens.",
    model: str = "A fake model of the mock an objective lens.",
    numerical_aperture: float = 0.2,
    magnification: float = 10.0,
) -> ndx_ophys_devices.ObjectiveLens:
    objective_lens = ndx_ophys_devices.ObjectiveLens(
        name=name or name_generator("ObjectiveLens"),
        description=description,
        manufacturer=manufacturer,
        model=model,
        numerical_aperture=numerical_aperture,
        magnification=magnification,
    )
    return objective_lens


def mock_ExcitationSource(
    *,
    name: Optional[str] = None,
    description: str = "This is a mock instance of a ExcitationSource type to be used for rapid testing.",
    manufacturer: str = "A fake manufacturer of the mock excitation source.",
    model: str = "A fake model of the mock excitation source.",
    illumination_type: str = "Laser.",
    excitation_wavelength_in_nm: float = 500.0,
    power_in_W: float = 0.7,
    intensity_in_W_per_m2: float = 0.005,
    exposure_time_in_s: float = 2.51e-13,
) -> ndx_ophys_devices.ExcitationSource:
    excitation_source = ndx_ophys_devices.ExcitationSource(
        name=name or name_generator("ExcitationSource"),
        description=description,
        manufacturer=manufacturer,
        model=model,
        illumination_type=illumination_type,
        excitation_wavelength_in_nm=excitation_wavelength_in_nm,
        power_in_W=power_in_W,
        intensity_in_W_per_m2=intensity_in_W_per_m2,
        exposure_time_in_s=exposure_time_in_s,
    )
    return excitation_source


def mock_PulsedExcitationSource(
    *,
    name: Optional[str] = None,
    description: str = "This is a mock instance of a PulsedExcitationSource type to be used for rapid testing.",
    manufacturer: str = "A fake manufacturer of the mock excitation source.",
    model: str = "A fake model of the mock excitation source.",
    illumination_type: str = "Laser.",
    excitation_wavelength_in_nm: float = 500.0,
    peak_power_in_W: float = 0.7,
    peak_pulse_energy_in_J: float = 0.7,
    intensity_in_W_per_m2: float = 0.005,
    exposure_time_in_s: float = 2.51e-13,
    pulse_rate_in_Hz: float = 2.0e6,
) -> ndx_ophys_devices.PulsedExcitationSource:
    pulsed_excitation_source = ndx_ophys_devices.PulsedExcitationSource(
        name=name or name_generator("PulsedExcitationSource"),
        description=description,
        manufacturer=manufacturer,
        model=model,
        illumination_type=illumination_type,
        excitation_wavelength_in_nm=excitation_wavelength_in_nm,
        peak_power_in_W=peak_power_in_W,
        peak_pulse_energy_in_J=peak_pulse_energy_in_J,
        intensity_in_W_per_m2=intensity_in_W_per_m2,
        exposure_time_in_s=exposure_time_in_s,
        pulse_rate_in_Hz=pulse_rate_in_Hz,
    )
    return pulsed_excitation_source