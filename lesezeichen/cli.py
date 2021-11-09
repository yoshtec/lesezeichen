#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# SPDX-License-Identifier: MIT

import click

@click.group()
def cli():
    """ Organize and start bookmarks """


@cli.command
@click.argument("id")
@click.argument("url")
def add(
        id: str,
        url: str
):
    pass

