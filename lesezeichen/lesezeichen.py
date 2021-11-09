#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# SPDX-License-Identifier: MIT

import fnmatch
import json
import pathlib


class Lesezeichen:

    def __init__(self):
        self.loaded = False
        self.bookmarks = dict()

    @staticmethod
    def _file():
        return pathlib.Path.home() / ".lzn_lesezeichen"

    def load(self):
        self.bookmarks = json.load(self._file().open("r"))

    def save(self):
        if self.bookmarks is not None and any(self.bookmarks):
            json.dump(self.bookmarks, self._file().open("w"))

    def get(self, title: str):
        if title in self.bookmarks:
            return title

    def add(self, title: str, url: str):
        self.bookmarks[title] = url

    def search_by_id(self, search: str):
        return {k: v for k, v in self.bookmarks.items() if fnmatch.fnmatch(v, search)}

    def search(self, search: str):
        return {k: v for k, v in self.bookmarks.items() if search in v or search in k}
