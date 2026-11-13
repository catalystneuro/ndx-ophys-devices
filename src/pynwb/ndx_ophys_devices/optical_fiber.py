from hdmf.utils import docval, get_docval, popargs
from pynwb import get_class, register_class

StereotacticPosition = get_class("StereotacticPosition", "ndx-ophys-devices")
FiberInsertion = get_class("FiberInsertion", "ndx-ophys-devices")
_GeneratedOpticalFiber = get_class("OpticalFiber", "ndx-ophys-devices")


@register_class("OpticalFiber", "ndx-ophys-devices")
class OpticalFiber(_GeneratedOpticalFiber):
    """OpticalFiber that also reads the deprecated FiberInsertion of files written with ndx-ophys-devices 0.3.x.

    Those files store a FiberInsertion under `fiber_insertion`, which holds a StereotacticPosition since 0.4.0.
    Reading keeps the FiberInsertion as written. New objects must use a StereotacticPosition.
    """

    @docval(
        *[
            dict(arg, type=(StereotacticPosition, FiberInsertion)) if arg["name"] == "fiber_insertion" else arg
            for arg in get_docval(_GeneratedOpticalFiber.__init__)
        ]
    )
    def __init__(self, **kwargs):
        fiber_insertion = popargs("fiber_insertion", kwargs)
        if not isinstance(fiber_insertion, FiberInsertion):
            super().__init__(fiber_insertion=fiber_insertion, **kwargs)
            return
        if not self._in_construct_mode:
            raise TypeError(
                "FiberInsertion was replaced by StereotacticPosition in ndx-ophys-devices 0.4.0 and is only read from "
                "files written with 0.3.x. Pass a StereotacticPosition with the position of the fiber tip as "
                "'fiber_insertion'."
            )
        super().__init__(**kwargs)
        self.fiber_insertion = fiber_insertion
