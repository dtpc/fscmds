#! /usr/bin/env python

from pathlib import PurePath

import click
from treelib import Tree

from .utils import FSPath


@click.command()
@click.argument("fspath", metavar="PATH", type=FSPath(exists=True, file_okay=False))
@click.option(
    "-L",
    "level",
    metavar="level",
    type=int,
    default=100,
    help="Descend only level directories deep.",
)
def cli(fspath, level):
    """List contents of directories in a tree-like format."""
    fs, root = fspath
    t = Tree()

    def walk(path: str, level: int, parent: str = None) -> None:
        name = PurePath(path).name
        t.create_node(name, path, parent=parent)
        if level and fs.isdir(path):
            for s in sorted(fs.ls(path)):
                if s != path:
                    walk(s, parent=path, level=level - 1)

    walk(root, level=level)
    t.show()


if __name__ == "__main__":
    cli()
