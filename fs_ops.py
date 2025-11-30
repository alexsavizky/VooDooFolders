from pathlib import Path
import shutil
from errors import FileNotFoundErrorCustom, NotAFileError, FolderCreationError


def create_folder(base_dir: Path, folder_name: str) -> Path:
    """
    Create a new folder inside base_dir with the given name.
    Returns the full Path to the created folder.
    Raises:
        FolderCreationError if the folder cannot be created.
    """
    target = base_dir / folder_name
    try:
        target.mkdir(parents=True, exist_ok=True)
    except Exception as e:
        raise FolderCreationError(f"Could not create folder: {target}") from e

    return target


def move_file_to_folder(file_path: Path, target_folder: Path) -> Path:
    """
    Move a single file to the target folder.
    Returns the new file path.

    Creates the target folder if it doesn't exist.
    """
    if not file_path.is_file():
        raise ValueError(f"Not a file: {file_path}")

    target_folder.mkdir(parents=True, exist_ok=True)

    dest = target_folder / file_path.name

    # If a file with same name already exists, you can decide what to do.
    # For now, we'll just overwrite.
    if dest.exists():
        # You could also choose to rename, or skip.
        dest.unlink()  # delete existing

    shutil.move(str(file_path), str(dest))
    return dest


create_folder(Path(r"C:\Users\alexs\codeProj\VooDooFolders"), "playground")
move_file_to_folder(
    Path(r"C:\Users\alexs\codeProj\VooDooFolders\test.py"),
    Path(r"C:\Users\alexs\codeProj\VooDooFolders\playground\test.py"),
)
