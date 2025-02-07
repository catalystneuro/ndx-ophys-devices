from hdmf.utils import docval, popargs_to_dict, get_docval
from pynwb import register_class, get_class


extension_name = "ndx-ophys-devices"

DeviceModel = get_class("DeviceModel", extension_name)


def _check_excitation_mode_str(excitation_mode):
    if excitation_mode not in ("one-photon", "two-photon", "three-photon", "other"):
        raise ValueError(
            f"excitation_mode must be one of 'one-photon', 'two-photon', "
            f"'three-photon', 'other', not {excitation_mode}. "
            f"If you want to include a different excitation mode, please open an issue on GitHub at "
            f"https://github.com/CatalystNeuro/ndx-microscopy/issues"
        )


@register_class("ExcitationSource", extension_name)
class ExcitationSource(DeviceModel):
    """Excitation light path that illuminates an imaging space."""

    __nwbfields__ = (
        "excitation_wavelength_in_nm",
        "excitation_mode",
        "illumination_type",
        "power_in_W",
        "intensity_in_W_per_m2",
        "exposure_time_in_s",
    )

    @docval(
        *get_docval(DeviceModel.__init__, "name", "description", "model", "manufacturer"),
        {
            "name": "excitation_wavelength_in_nm",
            "type": float,
            "doc": "Excitation wavelength of the stimulation light (nanometers).",
        },
        {
            "name": "excitation_mode",
            "type": str,
            "doc": (
                "The type of excitation used in the light path (e.g., 'one-photon', "
                "'two-photon', 'three-photon', 'other')."
            ),
        },
        {
            "name": "illumination_type",
            "type": str,
            "doc": (
                "Type of illumination. Suggested values: LED, Gas Laser (e.g., Argon, Krypton), "
                "Solid-State Laser (e.g., Diode, DPSS)."
            ),
        },
        {
            "name": "power_in_W",
            "type": float,
            "doc": "Incident power of stimulation device (in Watts).",
            "default": None,
        },
        {
            "name": "intensity_in_W_per_m2",
            "type": float,
            "doc": "Intensity of the excitation in W/m^2, if known.",
            "default": None,
        },
        {
            "name": "exposure_time_in_s",
            "type": float,
            "doc": "Exposure time of the sample (in sec).",
            "default": None,
        },
    )
    def __init__(self, **kwargs):
        keys_to_set = (
            "excitation_wavelength_in_nm",
            "excitation_mode",
            "illumination_type",
            "power_in_W",
            "intensity_in_W_per_m2",
            "exposure_time_in_s",
        )
        args_to_set = popargs_to_dict(keys_to_set, kwargs)
        super().__init__(**kwargs)
        for key, val in args_to_set.items():
            setattr(self, key, val)
        _check_excitation_mode_str(args_to_set["excitation_mode"])
