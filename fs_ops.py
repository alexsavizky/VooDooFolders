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


def normalize_extensions(exts: list[str]) -> set[str]:
    """
    Normalize a list of extensions to a lowercase set with leading dots.
    Example: ["mp3", ".WAV"] -> {".mp3", ".wav"}
    """
    norm = set()
    for e in exts:
        e = e.strip()
        if not e:
            continue
        if not e.startswith("."):
            e = "." + e
        norm.add(e.lower())
    return norm


def move_files_by_extension(
    root_dir: Path,
    extensions: list[str],
    target_folder_name: str,
) -> list[tuple[Path, Path]]:
    """
    Move all files under root_dir whose extension is in `extensions`
    into a folder named `target_folder_name` inside root_dir.

    Returns a list of (source_path, dest_path) for all moved files.
    """

    if not root_dir.exists() or not root_dir.is_dir():
        raise ValueError(f"root_dir is not a directory: {root_dir}")

    exts = normalize_extensions(extensions)

    target_folder = create_folder(root_dir, target_folder_name)
    moved: list[tuple[Path, Path]] = []

    for path in root_dir.rglob("*"):
        if not path.is_file():
            continue

        if path.suffix.lower() not in exts:
            continue

        # Don't try to move files that are already in the target folder
        if target_folder in path.parents:
            continue

        dest_before = path
        dest_after = move_file_to_folder(path, target_folder)
        moved.append((dest_before, dest_after))

    return moved
