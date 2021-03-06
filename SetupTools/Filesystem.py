#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This file is part of ArchSetup.
#
# ArchSetup is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# ArchSetup is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with ArchSetup.  If not, see <http://www.gnu.org/licenses/>.
import os

class Filesystem:
    def __init__(self):
        pass

    def list_filesystems(self):
        baselist = os.listdir("/usr/bin")
        fslist = []
        for file in baselist:
            if len(file) > 4:
                if file[:4] == "mkfs":
                    fslist.append(file)
        fslist.sort()
        return fslist

    def create_filesystem(self, drive, num):
        print("[D] create_filesystem() not implemented")

