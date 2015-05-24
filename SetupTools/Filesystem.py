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

import subprocess

class Filesystem:
    def __init__(self):
        pass

    def list_filesystems(self):
        fslist=subprocess.check_output("ls /bin/ | grep \"mkfs\"").decode().split('\n')
        fslist.remove('')
        return fslist

    def create_filesystem(self, drive, num):
        print("[D] create_filesystem() not implemented")

