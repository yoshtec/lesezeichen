#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# SPDX-License-Identifier: MIT

import json
import pathlib
import subprocess
import platform


class Lesezeichen:
    def __init__(self, file=None):
        self.bookmarks = dict()
        self.file = file
        self.load()

    def _file(self):
        if self.file is None:
            self.file = pathlib.Path.home() / ".lzn_lesezeichen"
        return self.file

    def load(self):
        file = self._file()
        if file.exists():
            self.bookmarks = json.load(file.open("r"))

    def save(self):
        if self.bookmarks is not None and any(self.bookmarks):
            json.dump(self.bookmarks, self._file().open("w"))

    def delete(self, name: str):
        if name in self.bookmarks:
            print(f"deleted: {name} - {self.bookmarks[name]}")
            del self.bookmarks[name]
            return True
        else:
            print(f"no bookmark with name: {name}")
            return False

    def get_url(self, name: str):
        if name in self.bookmarks:
            return self.bookmarks[name]

    def add(self, name: str, url: str):
        if name in self.bookmarks:
            print(f"overwrite current bookmark name={name}, url='{self.bookmarks[name]}'")
        self.bookmarks[name] = url

    def search_by_id(self, search: str):
        return {k: v for k, v in self.bookmarks.items() if k.startswith(search)}

    def search(self, search: str):
        return {k: v for k, v in self.bookmarks.items() if search in v or search in k}

    def open(self, name: str):
        url = self.get_url(name)

        cmd = "xdg-open"
        if platform.system() == "Darwin":
            cmd = "open"
        elif platform.system() == "Windows":
            cmd = "start"

        if url is not None:
            subprocess.check_call([cmd, url])
        else:
            print(f"no url with name={name}")
