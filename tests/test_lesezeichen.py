# -*- coding: utf-8 -*-
# SPDX-License-Identifier: MIT

from click.testing import CliRunner
from pathlib import Path
from lesezeichen import lesezeichen, cli


runner = CliRunner()


def mock_file(cls):
    with runner.isolated_filesystem():
        path = Path() / ".lzn_tmp"
        return path


# monkeypatch the file function to return a temp dir
lesezeichen.Lesezeichen._file = mock_file


class TestLesezeichen:

    def test_something(self):
        result = runner.invoke(cli.add, ["test", "test"])
        print(result)
        result = runner.invoke(cli.open, ["test"])
        print(result)

