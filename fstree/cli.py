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
def main(uri, level):
    fs, root = url_to_fs(uri)
    root = PurePath(root)
    t = Tree()

    def walk(path, level, parent=None):
        t.create_node(path.name, str(path), parent=parent)
        if level and fs.isdir(path):
            contents = sorted(map(PurePath, fs.ls(path)))
            for s in contents:
                if s != path:
                    walk(s, parent=str(path), level=level - 1)

    walk(root, level=level)
    t.show()


if __name__ == "__main__":
    main()
