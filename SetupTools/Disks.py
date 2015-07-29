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
import os

class Disks:
    def __init__(self):
        pass

    def list_disks(self):
        disklist=subprocess.check_output(["ls /dev | grep sd[[:alpha:]]$ "], shell=True).decode().split('\n')
        disklist.remove('')
        return disklist

    def part_disk(self, setupconfig, size_data):
        os.system("parted -s " + setupconfig.disk + " mklabel msdos mkpart primary 1 " +size_data +"M mkpart primary " + size_data + "M 100%% set 1 boot on")



        pass
