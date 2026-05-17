from pathlib import Path


def create_chalkboard_tripod_project(root_folder: str) -> Path:
    """
    Create the chalkboard_tripod FreeCAD project structure.

    Example:
        create_chalkboard_tripod_project(
            "/home/igorwolfs/work/mechanics/chalkboard_tripod"
        )
    """

    project_root = Path(root_folder).expanduser().resolve()

    folders = [
        "00_parameters",
        "01_parts",
        "02_assemblies",
        "03_exports/step",
        "03_exports/stl",
        "03_exports/drawings",
        "03_exports/cut_list",
        "04_macros",
    ]

    files = [
        "00_parameters/tripod_parameters.FCStd",
        "01_parts/aluminium_profile_40x40.FCStd",
        "01_parts/connector_90deg.FCStd",
        "01_parts/connector_angle.FCStd",
        "01_parts/foot.FCStd",
        "01_parts/chalkboard_panel.FCStd",
        "02_assemblies/chalkboard_tripod_assembly.FCStd",
        "04_macros/regenerate_profiles.py",
        "04_macros/export_step.py",
        "04_macros/make_cut_list.py",
        "README.md",
    ]

    for folder in folders:
        (project_root / folder).mkdir(parents=True, exist_ok=True)

    for file in files:
        path = project_root / file
        path.parent.mkdir(parents=True, exist_ok=True)
        path.touch(exist_ok=True)

    return project_root


if __name__ == "__main__":
    root = "/home/igorwolfs/personal/mechanical/chalkboard-stand/CAD"

    created_path = create_chalkboard_tripod_project(root)

    print(f"Created project structure at: {created_path}")