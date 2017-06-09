# -*- coding: utf-8 -*-

import click

from {{ cookiecutter.project_slug }} import __version__


@click.command(context_settings=dict(
    help_option_names=['-h', '--help']
))
@click.version_option(version=__version__)
def main():
    """Console script for {{cookiecutter.project_slug}}"""
    click.echo("Replace this message by putting your code into "
               "{{cookiecutter.project_slug}}.cli.main")
    click.echo("See click documentation at http://click.pocoo.org/")


if __name__ == "__main__":
    main()
