# v0.2.0 (Upcoming)

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
