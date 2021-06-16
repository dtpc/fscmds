from typing import Optional, Tuple

import click
from fsspec.core import url_to_fs
from fsspec.spec import AbstractFileSystem


class FSPath(click.ParamType):
    """A click param for any fsspec path."""

    name = "FSPath"

    def __init__(
        self, exists: bool = False, dir_okay: bool = True, file_okay: bool = True
    ):
        self.exists = exists
        self.dir_okay = dir_okay
        self.file_okay = file_okay

    def convert(
        self, value: str, param: Optional[click.Parameter], ctx: Optional[click.Context]
    ) -> Tuple[AbstractFileSystem, str]:
        """Convert uri to fsspec filesystem and root str."""
        try:
            fs, root = url_to_fs(value)
        except ImportError as e:
            raise click.ClickException(str(e))

        if self.exists:
            try:
                fs.info(root)
            except FileNotFoundError:
                raise click.ClickException(f"{value} does not exist")
            except Exception as e:
                raise click.ClickException(str(e))

        if not self.dir_okay and fs.isdir(root):
            raise click.ClickException(f"{value} is a directory")

        if not self.file_okay and fs.isfile(root):
            raise click.ClickException(f"{value} is a file")

        return fs, root
