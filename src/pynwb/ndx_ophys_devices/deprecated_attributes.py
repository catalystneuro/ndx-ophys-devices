from hdmf.utils import docval, get_docval
from pynwb import get_class, register_class

_GeneratedPhotodetectorModel = get_class("PhotodetectorModel", "ndx-ophys-devices")
_GeneratedViralVectorInjection = get_class("ViralVectorInjection", "ndx-ophys-devices")


def _reject_deprecated_attributes(container, kwargs, attribute_names, replacement):
    passed_names = [name for name in attribute_names if kwargs[name] is not None]
    if passed_names and not container._in_construct_mode:
        raise TypeError(
            f"Attributes removed in ndx-ophys-devices 0.4.0 were passed to {type(container).__name__}: "
            f"{', '.join(passed_names)}. They are only read from files written with 0.3.x. {replacement}"
        )


@register_class("PhotodetectorModel", "ndx-ophys-devices")
class PhotodetectorModel(_GeneratedPhotodetectorModel):
    """PhotodetectorModel that accepts the deprecated gain and gain_unit only when reading files written with 0.3.x."""

    @docval(*get_docval(_GeneratedPhotodetectorModel.__init__))
    def __init__(self, **kwargs):
        _reject_deprecated_attributes(
            self, kwargs, ("gain", "gain_unit"), "Set 'gain' and 'gain_unit' on the Photodetector."
        )
        super().__init__(**kwargs)


@register_class("ViralVectorInjection", "ndx-ophys-devices")
class ViralVectorInjection(_GeneratedViralVectorInjection):
    """ViralVectorInjection that accepts the deprecated coordinates only when reading files written with 0.3.x."""

    @docval(*get_docval(_GeneratedViralVectorInjection.__init__))
    def __init__(self, **kwargs):
        _reject_deprecated_attributes(
            self,
            kwargs,
            (
                "location",
                "hemisphere",
                "reference",
                "ap_in_mm",
                "ml_in_mm",
                "dv_in_mm",
                "pitch_in_deg",
                "yaw_in_deg",
                "roll_in_deg",
                "stereotactic_rotation_in_deg",
                "stereotactic_tilt_in_deg",
            ),
            "Pass a StereotacticPosition as 'viral_injection_coordinates'.",
        )
        super().__init__(**kwargs)
