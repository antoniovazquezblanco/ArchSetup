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
        os.system("parted -s /dev/" + setupconfig.disk + " mklabel msdos mkpart primary 1 " +str(size_data) +"M mkpart primary " + str(size_data) + "M 100% set 1 boot on")

    def makefs(self, setupconfig):
        cmd = str(setupconfig.filesystem +" /dev/" +setupconfig.disk +"1 -F > /dev/null")
        os.system(cmd)
        cmd = str("mkswap /dev/" +setupconfig.disk +"2 > /dev/null")
        os.system(cmd)

    def mount(self, setupconfig):
        cmd = str("mount /dev/" +setupconfig.disk +"1 /mnt")
        os.system(cmd)
        cmd = str("swapon /dev/" +setupconfig.disk +"2")
        os.system(cmd)

        pass
