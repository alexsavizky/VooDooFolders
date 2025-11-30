from pathlib import Path
from fs_ops import create_folder, move_file_to_folder, move_files_by_extension


def execute_instructions(instructions: str, base_dir: Path):
    """
    Execute AI-generated Python instructions in a controlled sandbox.
    Only exposes safe functions and the base_dir variable.
    """

    # Sandbox environment (ONLY these names exist)
    allowed_globals = {
        "create_folder": create_folder,
        "move_file_to_folder": move_file_to_folder,
        "move_files_by_extension": move_files_by_extension,
        "base_dir": base_dir,
        "Path": Path,
    }

    try:
        exec(instructions, allowed_globals, {})
    except Exception as e:
        raise RuntimeError(
            f"Error while executing instructions:\n{instructions}\n\n{e}"
        )
