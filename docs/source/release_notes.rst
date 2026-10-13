Release Notes
=============
Version 0.4.0 (upcoming)
------------------------
New Features:
- Added new neurodata types:
  - ``StereotacticPosition``: Extends ``NWBContainer`` to hold metadata about the stereotactic position of a device relative to the brain.
- Added realistic configuration examples notebook.
- Added optional ``pulse_width_in_s`` to ``PulsedExcitationSource``.

Changes:
- Renamed `OpticalLens` to `ObjectiveLens`
- Replaced ``FiberInsertion`` with ``StereotacticPosition``
- Replaced ``LensPositioning`` with ``StereotacticPosition``
- Replaced ``ViralVectorInjection`` fields related to coordinates and angles with ``StereotacticPosition`` group
- Moved ``gain`` and ``gain_unit`` from ``PhotodetectorModel`` to ``Photodetector``, since gain is set per session
- Made ``OpticalFiber.fiber_insertion`` optional, so that fibers that are not implanted (e.g., patch cords) can be described
- Clarified that ``ExcitationSource.power_in_W`` is the power delivered to the sample, and that ``PulsedExcitationSource.pulse_rate_in_Hz`` is the laser repetition rate
- ``StereotacticPosition`` coordinates describe the target (device tip or injection site); angles describe the approach, with all angles equal to 0 meaning a vertical approach

Reading files written with earlier versions:
Files written with ndx-ophys-devices 0.3.x cannot be read in a Python session that has imported ndx-ophys-devices 0.4.0,
or an extension that imports it, because the installed namespace takes precedence over the one cached in the file.
To read such files, open them in a session that does not import these packages; pynwb then loads the cached namespaces.

Version 0.3.1 (Sept 19, 2025)
-----------------------------

New Features
- Added `ViralVector` and `ViralVectorInjection` classes to hold metadata about viral vectors used for gene delivery
- Updated `injection_date` in `ViralVectorInjection` to plain text

Changes
- Added extra optional attributes to `OpticalFiberModel`
- Switched to core pynwb `DeviceModel` and `Device` classes now that they are available in pynwb 3.1.0 

Version 0.2.0 (Jun 3, 2025)
---------------------------

Major Refactoring:
- Implemented a clear distinction between device models and device instances:
  - Added ``DeviceModel`` as a base class for all device model classes
  - Added ``DeviceInstance`` as a base class for all device instance classes
  - Refactored all device classes into model and instance pairs (e.g., ``OpticalFiberModel`` and ``OpticalFiber``)
  - Renamed ``ObjectiveLens`` to ``OpticalLens`` for consistency

New Features:
- Added new neurodata types:
  - ``LensPositioning``: Extends ``NWBContainer`` to hold metadata on the positioning of a lens relative to the brain.
  - ``FiberInsertion``: Extends ``NWBContainer`` to hold metadata on the insertion of a fiber into the brain.

Changes:
- Changed ``illumination_type`` to ``source_type`` in ``ExcitationSourceModel`` for better clarity.
- Removed ``excitation_wavelength_in_nm`` from ``ExcitationSourceModel`` as it's often redundant with filter specifications.
- Removed ``detected_wavelength_in_nm`` from ``PhotodetectorModel`` as it's often redundant with filter specifications.
- Added ``wavelength_range_in_nm`` to ``ExcitationSourceModel`` and ``PhotodetectorModel`` to specify the range of wavelengths.

Version 0.1.0 (Initial Release)
-------------------------------

- Initial release of the ndx-ophys-devices extension.
- Introduced neurodata types for optical experimental setups:
  - ``Indicator``, ``Effector``
  - ``OpticalFiber``, ``ExcitationSource``, ``PulsedExcitationSource``
  - ``Photodetector``, ``DichroicMirror``
  - ``OpticalFilter``, ``BandOpticalFilter``, ``EdgeOpticalFilter``
  - ``ObjectiveLens``
