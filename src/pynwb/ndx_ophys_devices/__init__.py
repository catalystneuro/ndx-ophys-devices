import os
from pynwb import load_namespaces, get_class

try:
    from importlib.resources import files
except ImportError:
    # TODO: Remove when python 3.9 becomes the new minimum
    from importlib_resources import files

# Get path to the namespace.yaml file with the expected location when installed not in editable mode
__location_of_this_file = files(__name__)
__spec_path = __location_of_this_file / "spec" / "ndx-ophys-devices.namespace.yaml"

# If that path does not exist, we are likely running in editable mode. Use the local path instead
if not os.path.exists(__spec_path):
    __spec_path = __location_of_this_file.parent.parent.parent / "spec" / "ndx-ophys-devices.namespace.yaml"

# Load the namespace
load_namespaces(str(__spec_path))

from .ndx_ophys_devices import ExcitationSource, DeviceModel

Indicator = get_class("Indicator", "ndx-ophys-devices")
OpticalFiber = get_class("OpticalFiber", "ndx-ophys-devices")
PulsedExcitationSource = get_class("PulsedExcitationSource", "ndx-ophys-devices")
Photodetector = get_class("Photodetector", "ndx-ophys-devices")
DichroicMirror = get_class("DichroicMirror", "ndx-ophys-devices")
OpticalFilter = get_class("OpticalFilter", "ndx-ophys-devices")
BandOpticalFilter = get_class("BandOpticalFilter", "ndx-ophys-devices")
EdgeOpticalFilter = get_class("EdgeOpticalFilter", "ndx-ophys-devices")
ObjectiveLens = get_class("ObjectiveLens", "ndx-ophys-devices")
Effector = get_class("Effector", "ndx-ophys-devices")

__all__ = [
    "Indicator",
    "OpticalFiber",
    "ExcitationSource",
    "PulsedExcitationSource",
    "Photodetector",
    "DichroicMirror",
    "OpticalFilter",
    "BandOpticalFilter",
    "EdgeOpticalFilter",
    "ObjectiveLens",
    "Effector",
]

del load_namespaces, get_class
