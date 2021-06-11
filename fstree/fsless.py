#! /usr/bin/env python3

import click
from fsspec.core import url_to_fs

@click.command()
@click.argument("path", type=str)
def cli(path):
    fs, root = url_to_fs(path)
    if fs.isdir(root):
        click.echo(f"{path} is a directory")
    else:
        click.echo_via_pager(fs[root])


if __name__ == "__main__":
    cli()