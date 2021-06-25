#! /usr/bin/env python3

import click

from .utils import FSPath


@click.command()
@click.argument("fspath", metavar="PATH", type=FSPath(exists=True, dir_okay=False))
def cli(fspath):
    """Display contents of a file."""
    fs, root = fspath
    with fs.open(root, "r") as f:
        click.echo_via_pager(f.read())


if __name__ == "__main__":
    cli()
