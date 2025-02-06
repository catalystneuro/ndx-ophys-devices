from typing import Optional

from pynwb.testing.mock.utils import name_generator

import ndx_ophys_devices


def mock_DeviceModel(
    *,
    name: Optional[str] = None,
    manufacturer: str = "A fake manufacturer",
    model_number: Optional[str] = "MODEL-123",
    description: Optional[str] = "This is a mock instance of a DeviceModel type.",
) -> ndx_ophys_devices.DeviceModel:
    device_model = ndx_ophys_devices.DeviceModel(
        name=name or name_generator("DeviceModel"),
        manufacturer=manufacturer,
        model_number=model_number,
        description=description,
    )
    return device_model


def mock_DeviceInstance(
    *,
    name: Optional[str] = None,
    description: Optional[str] = "This is a mock instance of a DeviceInstance type.",
    serial_number: Optional[str] = "SN-123456",
    model: Optional[ndx_ophys_devices.DeviceModel] = None,
) -> ndx_ophys_devices.DeviceInstance:
    device_instance = ndx_ophys_devices.DeviceInstance(
        name=name or name_generator("DeviceInstance"),
        description=description,
        serial_number=serial_number,
        model=model,
    )
    return device_instance


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


def mock_OpticalFiberModel(
    *,
    name: Optional[str] = None,
    manufacturer: str = "A fake manufacturer",
    model_number: Optional[str] = "OF-123",
    description: Optional[str] = "This is a mock instance of an OpticalFiberModel type.",
    numerical_aperture: float = 0.2,
    core_diameter_in_um: float = 400.0,
) -> ndx_ophys_devices.OpticalFiberModel:
    optical_fiber_model = ndx_ophys_devices.OpticalFiberModel(
        name=name or name_generator("OpticalFiberModel"),
        manufacturer=manufacturer,
        model_number=model_number,
        description=description,
        numerical_aperture=numerical_aperture,
        core_diameter_in_um=core_diameter_in_um,
    )
    return optical_fiber_model


def mock_OpticalFiber(
    *,
    name: Optional[str] = None,
    description: Optional[str] = "This is a mock instance of an OpticalFiber type.",
    serial_number: Optional[str] = "OF-SN-123456",
    model: Optional[ndx_ophys_devices.OpticalFiberModel] = None,
) -> ndx_ophys_devices.OpticalFiber:  # TODO: Update return type when core types are updated
    if model is None:
        model = mock_OpticalFiberModel()
    optical_fiber = ndx_ophys_devices.OpticalFiber(
        name=name or name_generator("OpticalFiber"),
        description=description,
        serial_number=serial_number,
        model=model,
    )
    return optical_fiber


def mock_PhotodetectorModel(
    *,
    name: Optional[str] = None,
    manufacturer: str = "A fake manufacturer",
    model_number: Optional[str] = "PD-123",
    description: Optional[str] = "This is a mock instance of a PhotodetectorModel type.",
    detector_type: str = "PMT",
    wavelength_range_in_nm: list = [400.0, 800.0],
    gain: float = 100.0,
    gain_unit: str = "A/W",
) -> ndx_ophys_devices.PhotodetectorModel:
    photodetector_model = ndx_ophys_devices.PhotodetectorModel(
        name=name or name_generator("PhotodetectorModel"),
        manufacturer=manufacturer,
        model_number=model_number,
        description=description,
        detector_type=detector_type,
        wavelength_range_in_nm=wavelength_range_in_nm,
        gain=gain,
        gain_unit=gain_unit,
    )
    return photodetector_model


def mock_Photodetector(
    *,
    name: Optional[str] = None,
    description: Optional[str] = "This is a mock instance of a Photodetector type.",
    serial_number: Optional[str] = "PD-SN-123456",
    model: Optional[ndx_ophys_devices.PhotodetectorModel] = None,
    detected_wavelength_in_nm: float = 520.0,
) -> ndx_ophys_devices.Photodetector:  # TODO: Update return type when core types are updated
    if model is None:
        model = mock_PhotodetectorModel()
    photodetector = ndx_ophys_devices.Photodetector(
        name=name or name_generator("Photodetector"),
        description=description,
        serial_number=serial_number,
        model=model,
        detected_wavelength_in_nm=detected_wavelength_in_nm,
    )
    return photodetector


def mock_DichroicMirrorModel(
    *,
    name: Optional[str] = None,
    manufacturer: str = "A fake manufacturer",
    model_number: Optional[str] = "DM-123",
    description: Optional[str] = "This is a mock instance of a DichroicMirrorModel type.",
    cut_on_wavelength_in_nm: float = 470.0,
    cut_off_wavelength_in_nm: float = 500.0,
    reflection_band_in_nm: list = [460.0, 480.0],
    transmission_band_in_nm: list = [490.0, 520.0],
    angle_of_incidence_in_degrees: float = 45.0,
) -> ndx_ophys_devices.DichroicMirrorModel:
    dichroic_mirror_model = ndx_ophys_devices.DichroicMirrorModel(
        name=name or name_generator("DichroicMirrorModel"),
        manufacturer=manufacturer,
        model_number=model_number,
        description=description,
        cut_on_wavelength_in_nm=cut_on_wavelength_in_nm,
        cut_off_wavelength_in_nm=cut_off_wavelength_in_nm,
        reflection_band_in_nm=reflection_band_in_nm,
        transmission_band_in_nm=transmission_band_in_nm,
        angle_of_incidence_in_degrees=angle_of_incidence_in_degrees,
    )
    return dichroic_mirror_model


def mock_DichroicMirror(
    *,
    name: Optional[str] = None,
    description: Optional[str] = "This is a mock instance of a DichroicMirror type.",
    serial_number: Optional[str] = "DM-SN-123456",
    model: Optional[ndx_ophys_devices.DichroicMirrorModel] = None,
) -> ndx_ophys_devices.DichroicMirror:  # TODO: Update return type when core types are updated
    if model is None:
        model = mock_DichroicMirrorModel()
    dichroic_mirror = ndx_ophys_devices.DichroicMirror(
        name=name or name_generator("DichroicMirror"),
        description=description,
        serial_number=serial_number,
        model=model,
    )
    return dichroic_mirror


def mock_OpticalFilterModel(
    *,
    name: Optional[str] = None,
    manufacturer: str = "A fake manufacturer",
    model_number: Optional[str] = "OF-123",
    description: Optional[str] = "This is a mock instance of an OpticalFilterModel type.",
    filter_type: str = "Longpass",
) -> ndx_ophys_devices.OpticalFilterModel:
    optical_filter_model = ndx_ophys_devices.OpticalFilterModel(
        name=name or name_generator("OpticalFilterModel"),
        manufacturer=manufacturer,
        model_number=model_number,
        description=description,
        filter_type=filter_type,
    )
    return optical_filter_model


def mock_OpticalFilter(
    *,
    name: Optional[str] = None,
    description: Optional[str] = "This is a mock instance of an OpticalFilter type.",
    serial_number: Optional[str] = "OF-SN-123456",
    model: Optional[ndx_ophys_devices.OpticalFilterModel] = None,
) -> ndx_ophys_devices.OpticalFilter:  # TODO: Update return type when core types are updated
    if model is None:
        model = mock_OpticalFilterModel()
    optical_filter = ndx_ophys_devices.OpticalFilter(
        name=name or name_generator("OpticalFilter"),
        description=description,
        serial_number=serial_number,
        model=model,
    )
    return optical_filter


def mock_BandOpticalFilterModel(
    *,
    name: Optional[str] = None,
    manufacturer: str = "A fake manufacturer",
    model_number: Optional[str] = "BOF-123",
    description: Optional[str] = "This is a mock instance of a BandOpticalFilterModel type.",
    filter_type: str = "Bandpass",
    center_wavelength_in_nm: float = 505.0,
    bandwidth_in_nm: float = 30.0,  # 505±15nm
) -> ndx_ophys_devices.BandOpticalFilterModel:
    band_optical_filter_model = ndx_ophys_devices.BandOpticalFilterModel(
        name=name or name_generator("BandOpticalFilterModel"),
        manufacturer=manufacturer,
        model_number=model_number,
        description=description,
        filter_type=filter_type,
        center_wavelength_in_nm=center_wavelength_in_nm,
        bandwidth_in_nm=bandwidth_in_nm,
    )
    return band_optical_filter_model


def mock_BandOpticalFilter(
    *,
    name: Optional[str] = None,
    description: Optional[str] = "This is a mock instance of a BandOpticalFilter type.",
    serial_number: Optional[str] = "BOF-SN-123456",
    model: Optional[ndx_ophys_devices.BandOpticalFilterModel] = None,
) -> ndx_ophys_devices.BandOpticalFilter:  # TODO: Update return type when core types are updated
    if model is None:
        model = mock_BandOpticalFilterModel()
    band_optical_filter = ndx_ophys_devices.BandOpticalFilter(
        name=name or name_generator("BandOpticalFilter"),
        description=description,
        serial_number=serial_number,
        model=model,
    )
    return band_optical_filter


def mock_EdgeOpticalFilterModel(
    *,
    name: Optional[str] = None,
    manufacturer: str = "A fake manufacturer",
    model_number: Optional[str] = "EOF-123",
    description: Optional[str] = "This is a mock instance of an EdgeOpticalFilterModel type.",
    filter_type: str = "Longpass",
    cut_wavelength_in_nm: float = 585.0,
    slope_in_percent_cut_wavelength: float = 1.0,
    slope_starting_transmission_in_percent: float = 10.0,
    slope_ending_transmission_in_percent: float = 80.0,
) -> ndx_ophys_devices.EdgeOpticalFilterModel:
    edge_optical_filter_model = ndx_ophys_devices.EdgeOpticalFilterModel(
        name=name or name_generator("EdgeOpticalFilterModel"),
        manufacturer=manufacturer,
        model_number=model_number,
        description=description,
        filter_type=filter_type,
        cut_wavelength_in_nm=cut_wavelength_in_nm,
        slope_in_percent_cut_wavelength=slope_in_percent_cut_wavelength,
        slope_starting_transmission_in_percent=slope_starting_transmission_in_percent,
        slope_ending_transmission_in_percent=slope_ending_transmission_in_percent,
    )
    return edge_optical_filter_model


def mock_EdgeOpticalFilter(
    *,
    name: Optional[str] = None,
    description: Optional[str] = "This is a mock instance of an EdgeOpticalFilter type.",
    serial_number: Optional[str] = "EOF-SN-123456",
    model: Optional[ndx_ophys_devices.EdgeOpticalFilterModel] = None,
) -> ndx_ophys_devices.EdgeOpticalFilter:  # TODO: Update return type when core types are updated
    if model is None:
        model = mock_EdgeOpticalFilterModel()
    edge_optical_filter = ndx_ophys_devices.EdgeOpticalFilter(
        name=name or name_generator("EdgeOpticalFilter"),
        description=description,
        serial_number=serial_number,
        model=model,
    )
    return edge_optical_filter


def mock_ObjectiveLensModel(
    *,
    name: Optional[str] = None,
    manufacturer: str = "A fake manufacturer",
    model_number: Optional[str] = "OL-123",
    description: Optional[str] = "This is a mock instance of an ObjectiveLensModel type.",
    numerical_aperture: float = 0.2,
    magnification: float = 10.0,
) -> ndx_ophys_devices.ObjectiveLensModel:
    objective_lens_model = ndx_ophys_devices.ObjectiveLensModel(
        name=name or name_generator("ObjectiveLensModel"),
        manufacturer=manufacturer,
        model_number=model_number,
        description=description,
        numerical_aperture=numerical_aperture,
        magnification=magnification,
    )
    return objective_lens_model


def mock_ObjectiveLens(
    *,
    name: Optional[str] = None,
    description: Optional[str] = "This is a mock instance of an ObjectiveLens type.",
    serial_number: Optional[str] = "OL-SN-123456",
    model: Optional[ndx_ophys_devices.ObjectiveLensModel] = None,
) -> ndx_ophys_devices.ObjectiveLens:  # TODO: Update return type when core types are updated
    if model is None:
        model = mock_ObjectiveLensModel()
    objective_lens = ndx_ophys_devices.ObjectiveLens(
        name=name or name_generator("ObjectiveLens"),
        description=description,
        serial_number=serial_number,
        model=model,
    )
    return objective_lens


def mock_ExcitationSourceModel(
    *,
    name: Optional[str] = None,
    manufacturer: str = "A fake manufacturer",
    model_number: Optional[str] = "ES-123",
    description: Optional[str] = "This is a mock instance of an ExcitationSourceModel type.",
    illumination_type: str = "Laser",
    excitation_mode: str = "one-photon",
    wavelength_range_in_nm: list = [400.0, 800.0],
) -> ndx_ophys_devices.ExcitationSourceModel:
    excitation_source_model = ndx_ophys_devices.ExcitationSourceModel(
        name=name or name_generator("ExcitationSourceModel"),
        manufacturer=manufacturer,
        model_number=model_number,
        description=description,
        illumination_type=illumination_type,
        excitation_mode=excitation_mode,
        wavelength_range_in_nm=wavelength_range_in_nm,
    )
    return excitation_source_model


def mock_ExcitationSource(
    *,
    name: Optional[str] = None,
    description: Optional[str] = "This is a mock instance of an ExcitationSource type.",
    serial_number: Optional[str] = "ES-SN-123456",
    model: Optional[ndx_ophys_devices.ExcitationSourceModel] = None,
    excitation_wavelength_in_nm: float = 500.0,
    power_in_W: float = 0.7,
    intensity_in_W_per_m2: float = 0.005,
    exposure_time_in_s: float = 2.51e-13,
) -> ndx_ophys_devices.ExcitationSource:  # TODO: Update return type when core types are updated
    if model is None:
        model = mock_ExcitationSourceModel()
    excitation_source = ndx_ophys_devices.ExcitationSource(
        name=name or name_generator("ExcitationSource"),
        description=description,
        serial_number=serial_number,
        model=model,
        excitation_wavelength_in_nm=excitation_wavelength_in_nm,
        power_in_W=power_in_W,
        intensity_in_W_per_m2=intensity_in_W_per_m2,
        exposure_time_in_s=exposure_time_in_s,
    )
    return excitation_source


def mock_PulsedExcitationSource(
    *,
    name: Optional[str] = None,
    description: Optional[str] = "This is a mock instance of a PulsedExcitationSource type.",
    serial_number: Optional[str] = "PES-SN-123456",
    model: Optional[ndx_ophys_devices.ExcitationSourceModel] = None,
    excitation_wavelength_in_nm: float = 500.0,
    peak_power_in_W: float = 0.7,
    peak_pulse_energy_in_J: float = 0.7,
    intensity_in_W_per_m2: float = 0.005,
    exposure_time_in_s: float = 2.51e-13,
    pulse_rate_in_Hz: float = 2.0e6,
) -> ndx_ophys_devices.PulsedExcitationSource:  # TODO: Update return type when core types are updated
    if model is None:
        model = mock_ExcitationSourceModel()
    pulsed_excitation_source = ndx_ophys_devices.PulsedExcitationSource(
        name=name or name_generator("PulsedExcitationSource"),
        description=description,
        serial_number=serial_number,
        model=model,
        excitation_wavelength_in_nm=excitation_wavelength_in_nm,
        peak_power_in_W=peak_power_in_W,
        peak_pulse_energy_in_J=peak_pulse_energy_in_J,
        intensity_in_W_per_m2=intensity_in_W_per_m2,
        exposure_time_in_s=exposure_time_in_s,
        pulse_rate_in_Hz=pulse_rate_in_Hz,
    )
    return pulsed_excitation_source
