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

# Container classes
LensPositioning = get_class("LensPositioning", "ndx-ophys-devices")
FiberInsertion = get_class("FiberInsertion", "ndx-ophys-devices")
ViralVector = get_class("ViralVector", "ndx-ophys-devices")
ViralVectorInjection = get_class("ViralVectorInjection", "ndx-ophys-devices")
Indicator = get_class("Indicator", "ndx-ophys-devices")
Effector = get_class("Effector", "ndx-ophys-devices")

# Model classes
OpticalFiberModel = get_class("OpticalFiberModel", "ndx-ophys-devices")
ExcitationSourceModel = get_class("ExcitationSourceModel", "ndx-ophys-devices")
PhotodetectorModel = get_class("PhotodetectorModel", "ndx-ophys-devices")
DichroicMirrorModel = get_class("DichroicMirrorModel", "ndx-ophys-devices")
OpticalFilterModel = get_class("OpticalFilterModel", "ndx-ophys-devices")
BandOpticalFilterModel = get_class("BandOpticalFilterModel", "ndx-ophys-devices")
EdgeOpticalFilterModel = get_class("EdgeOpticalFilterModel", "ndx-ophys-devices")
OpticalLensModel = get_class("OpticalLensModel", "ndx-ophys-devices")

# Device classes
OpticalFiber = get_class("OpticalFiber", "ndx-ophys-devices")
ExcitationSource = get_class("ExcitationSource", "ndx-ophys-devices")
PulsedExcitationSource = get_class("PulsedExcitationSource", "ndx-ophys-devices")
Photodetector = get_class("Photodetector", "ndx-ophys-devices")
DichroicMirror = get_class("DichroicMirror", "ndx-ophys-devices")
OpticalFilter = get_class("OpticalFilter", "ndx-ophys-devices")
BandOpticalFilter = get_class("BandOpticalFilter", "ndx-ophys-devices")
EdgeOpticalFilter = get_class("EdgeOpticalFilter", "ndx-ophys-devices")
OpticalLens = get_class("OpticalLens", "ndx-ophys-devices")
__all__ = [
    "LensPositioning",
    "FiberInsertion",
    "Indicator",
    "Effector",
    "OpticalFiberModel",
    "ExcitationSourceModel",
    "PhotodetectorModel",
    "DichroicMirrorModel",
    "OpticalFilterModel",
    "BandOpticalFilterModel",
    "EdgeOpticalFilterModel",
    "OpticalLensModel",
    "OpticalFiber",
    "ExcitationSource",
    "PulsedExcitationSource",
    "Photodetector",
    "DichroicMirror",
    "OpticalFilter",
    "BandOpticalFilter",
    "EdgeOpticalFilter",
    "OpticalLens",
]
del load_namespaces, get_class
