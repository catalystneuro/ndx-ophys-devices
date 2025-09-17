# v0.4.0 (Upcoming)

## New Features
- Added auto-publish.yml GitHub Action to automatically publish new versions to PyPI upon GitHub Release.

# v0.3.0 (September 17, 2025)

### New Features
- Added `ViralVector` and `ViralVectorInjection` classes to hold metadata about viral vectors used for gene delivery [PR #14](https://github.com/catalystneuro/ndx-ophys-devices/pull/14)
- Updated `injection_date` in `ViralVectorInjection` to plain text [PR #18](https://github.com/catalystneuro/ndx-ophys-devices/pull/18)

### Changes
- Added extra optional attributes to `OpticalFiberModel` [PR #13](https://github.com/catalystneuro/ndx-ophys-devices/pull/13)
- Switched to core pynwb `DeviceModel` and `Device` classes now that they are available in pynwb 3.1.0 [PR #20](https://github.com/catalystneuro/ndx-ophys-devices/pull/20)

# v0.2.0 (Jun 3, 2025)

## Deprecations and Changes
### Major Refactoring:
- Implemented a clear distinction between device models and device instances:
  - Added ``DeviceModel`` as a base class for all device model classes
  - Added ``DeviceInstance`` as a base class for all device instance classes
  - Refactored all device classes into model and instance pairs (e.g., ``OpticalFiberModel`` and ``OpticalFiber``)
  - Renamed ``ObjectiveLens`` to ``OpticalLens`` for consistency

### New Features:
- Added new neurodata types:
  - ``LensPositioning``: Extends ``NWBContainer`` to hold metadata on the positioning of a lens relative to the brain.
  - ``FiberInsertion``: Extends ``NWBContainer`` to hold metadata on the insertion of a fiber into the brain.

### Changes:
- Changed ``illumination_type`` to ``source_type`` in ``ExcitationSourceModel`` for better clarity.
- Removed ``excitation_wavelength_in_nm`` from ``ExcitationSourceModel`` as it's often redundant with filter specifications.
- Removed ``detected_wavelength_in_nm`` from ``PhotodetectorModel`` as it's often redundant with filter specifications.
- Added ``wavelength_range_in_nm`` to ``ExcitationSourceModel`` and ``PhotodetectorModel`` to specify the range of wavelengths.

## Bug Fixes

## Features

## Improvements

# v0.1.1 (Feb 25, 2025)

## Deprecations and Changes
* Add excitation mode as a required field for `ExcitationSource`, and internal check for `excitation_mode` argument ([PR#7](https://github.com/catalystneuro/ndx-ophys-devices/pull/7))

## Bug Fixes

## Features

## Improvements
* Add example notebook ([PR#8](https://github.com/catalystneuro/ndx-ophys-devices/pull/8))
