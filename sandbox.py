from pathlib import Path
from fs_ops import move_files_by_extension

if __name__ == "__main__":
    root = Path(r"C:\Users\alexs\codeProj\VooDooFolders\playground")

    moved = move_files_by_extension(
        root_dir=root,
        extensions=["mp3", ".wav"],
        target_folder_name="Music",
    )

    print("Moved files:")
    for src, dst in moved:
        print(f"- {src}  ->  {dst}")
