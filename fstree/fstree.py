#! /usr/bin/env python

from pathlib import PurePath

import click
from fsspec.core import url_to_fs
from treelib import Tree


@click.command()
@click.argument("uri")
@click.option(
    "-L",
    "level",
    metavar="level",
    type=int,
    default=100,
    help="Descend only level directories deep.",
)
def cli(uri, level):
    fs, root = url_to_fs(uri)
    root = PurePath(root)
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
