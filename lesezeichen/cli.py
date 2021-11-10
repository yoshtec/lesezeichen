#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# SPDX-License-Identifier: MIT

import click
from click.shell_completion import CompletionItem
from lesezeichen.lesezeichen import Lesezeichen


lzn = Lesezeichen()


class UrlName(click.ParamType):
    def shell_complete(self, ctx, param, incomplete):
        return [
            CompletionItem(name, help=url)
            for name, url in lzn.search_by_id(search=incomplete).items()
        ]


@click.group()
@click.version_option()
def cli():
    """Organize and start bookmarks"""


@cli.command()
@click.argument("name", type=UrlName())
def open(name: str):
    """Open url with the name"""
    lzn.open(name)


@cli.command()
@click.argument("name")
@click.argument("url")
def add(name: str, url: str):
    """add"""
    lzn.add(name, url)
    lzn.save()


@cli.command()
@click.argument("name", type=UrlName())
def delete(name: str):
    """delete entry with name"""
    if lzn.delete(name):
        lzn.save()

