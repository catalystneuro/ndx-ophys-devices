"""Generate the NWB file read by test_read.py, with every type and attribute that ndx-ophys-devices 0.4.0 changed.

Run with ndx-ophys-devices 0.3.1 and pynwb 3.1 installed:

    pip install "ndx-ophys-devices==0.3.1" "pynwb==3.1.*"
    python generate_data_0.3.1.py
"""

import tempfile
from datetime import datetime, timezone
from pathlib import Path

from ndx_ophys_devices import (
    FiberInsertion,
    LensPositioning,
    OpticalFiber,
    OpticalFiberModel,
    OpticalLens,
    OpticalLensModel,
    Photodetector,
    PhotodetectorModel,
    ViralVector,
    ViralVectorInjection,
)
from pynwb import NWBHDF5IO, NWBFile, get_class, load_namespaces
from pynwb.spec import NWBGroupSpec, NWBNamespaceBuilder

# ViralVector and ViralVectorInjection cannot be added to an NWB file directly, so a test-only LabMetaData holds them.
namespace_name = "ndx-ophys-devices-back-compat"
spec_dir = Path(tempfile.mkdtemp())
builder = NWBNamespaceBuilder(
    doc="Test-only namespace", name=namespace_name, version="0.1.0", author="test", contact="test"
)
builder.include_type("LabMetaData", namespace="core")
builder.include_type("ViralVector", namespace="ndx-ophys-devices")
builder.include_type("ViralVectorInjection", namespace="ndx-ophys-devices")
builder.add_spec(
    f"{namespace_name}.extensions.yaml",
    NWBGroupSpec(
        neurodata_type_def="MolecularToolsMetadata",
        neurodata_type_inc="LabMetaData",
        doc="Holds molecular tool containers for testing.",
        groups=[
            NWBGroupSpec(neurodata_type_inc="ViralVector", doc="ViralVector objects.", quantity="*"),
            NWBGroupSpec(neurodata_type_inc="ViralVectorInjection", doc="ViralVectorInjection objects.", quantity="*"),
        ],
    ),
)
builder.export(f"{namespace_name}.namespace.yaml", outdir=str(spec_dir))
load_namespaces(str(spec_dir / f"{namespace_name}.namespace.yaml"))
MolecularToolsMetadata = get_class("MolecularToolsMetadata", namespace_name)

nwbfile = NWBFile(
    session_description="ndx-ophys-devices 0.3.1 types",
    identifier="ndx-ophys-devices-0.3.1",
    session_start_time=datetime(2000, 1, 1, tzinfo=timezone.utc),
)

viral_vector = ViralVector(
    name="ViralVector",
    construct_name="AAV1-hSyn-GCaMP6f",
    manufacturer="Addgene",
    titer_in_vg_per_ml=1.0e12,
)
injection = ViralVectorInjection(
    name="ViralVectorInjection",
    location="Dorsal CA1",
    hemisphere="left",
    reference="Bregma at the cortical surface",
    ap_in_mm=-2.0,
    ml_in_mm=-1.5,
    dv_in_mm=-1.25,
    pitch_in_deg=10.0,
    yaw_in_deg=0.0,
    roll_in_deg=0.0,
    stereotactic_rotation_in_deg=5.0,
    stereotactic_tilt_in_deg=2.0,
    volume_in_uL=0.45,
    viral_vector=viral_vector,
)
nwbfile.add_lab_meta_data(
    MolecularToolsMetadata(
        name="molecular_tools",
        viral_vectors=[viral_vector],
        viral_vector_injections=[injection],
    )
)

optical_fiber_model = OpticalFiberModel(
    name="OpticalFiberModel",
    manufacturer="Doric Lenses",
    numerical_aperture=0.48,
    core_diameter_in_um=400.0,
)
nwbfile.add_device_model(optical_fiber_model)
nwbfile.add_device(
    OpticalFiber(
        name="OpticalFiber",
        model=optical_fiber_model,
        fiber_insertion=FiberInsertion(
            name="fiber_insertion",
            insertion_position_ap_in_mm=-3.0,
            insertion_position_ml_in_mm=-1.0,
            insertion_position_dv_in_mm=0.0,
            depth_in_mm=4.0,
            position_reference="Bregma at the cortical surface",
            hemisphere="left",
            insertion_angle_yaw_in_deg=0.0,
            insertion_angle_pitch_in_deg=0.0,
            insertion_angle_roll_in_deg=10.0,
        ),
    )
)

optical_lens_model = OpticalLensModel(
    name="OpticalLensModel",
    manufacturer="Inscopix",
    numerical_aperture=0.5,
    magnification=2.0,
)
nwbfile.add_device_model(optical_lens_model)
nwbfile.add_device(
    OpticalLens(
        name="OpticalLens",
        model=optical_lens_model,
        lens_positioning=LensPositioning(
            name="lens_positioning",
            positioning_type="inserted",
            target_position_ap_in_mm=1.0,
            target_position_ml_in_mm=1.5,
            target_position_dv_in_mm=-2.0,
            depth_in_mm=2.0,
            working_distance_in_mm=0.1,
            position_reference="Bregma at the cortical surface",
            hemisphere="right",
            optical_axis_angle_yaw_in_deg=0.0,
            optical_axis_angle_pitch_in_deg=0.0,
            optical_axis_angle_roll_in_deg=0.0,
        ),
    )
)

photodetector_model = PhotodetectorModel(
    name="PhotodetectorModel",
    manufacturer="Hamamatsu",
    detector_type="PMT",
    gain=100.0,
    gain_unit="V/W",
)
nwbfile.add_device_model(photodetector_model)
nwbfile.add_device(Photodetector(name="Photodetector", model=photodetector_model))

with NWBHDF5IO(Path(__file__).parent / "0.3.1_changed_types.nwb", "w") as io:
    io.write(nwbfile)
