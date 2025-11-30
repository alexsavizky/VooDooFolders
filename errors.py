class FileNotFoundErrorCustom(Exception):
    """Raised when the given file path does not exist."""

    pass


class NotAFileError(Exception):
    """Raised when the given path exists but is not a file."""

    pass


class FolderCreationError(Exception):
    """Raised when a directory cannot be created."""

    pass
