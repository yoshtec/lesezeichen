#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# SPDX-License-Identifier: MIT

from click.testing import CliRunner
from pathlib import Path

import lesezeichen.lesezeichen
from lesezeichen import lesezeichen, cli


runner = CliRunner()


def mockreturn(cls):
    with runner.isolated_filesystem():
        path = Path(".")
        return path


# monkeypatch the file function to return a temp dir
lesezeichen.Lesezeichen._file = mockreturn


class TestLesezeichen:

    def test_something(self):
        result = runner.invoke(cli.cli(), ["add", "test", "test"])
        print(result)

