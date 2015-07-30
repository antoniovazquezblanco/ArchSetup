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
import subprocess
from SetupTools.Disks import Disks

class PreInstall:
    def __init__(self):
        pass

    #Task to do:
    # > Install Requiered Software      [x]
    # > Recive Mirrorlists              [x]
    # > Part disk                       [x]
    # > Creates Filesystem              [x]
    # > mount datapart and swap         [x]
    def run(setupconfig):
        yield "1,installing requiered software"
        os.system("pacman -Sy reflector --noconfirm --needed 2> /dev/null > /dev/null")
        yield "10,fetching mirrorlist"
        # get the 50 >most up to date< servers and sort them by download speed
        os.system("reflector --verbose -l 50 -p http --sort rate --save list.txt 2>/dev/null > /dev/null")

        yield "33,partitioning disk"

        # Calculate Partition layout:
        #
        #   /dev/sdx1 = data = TOTALSIZE - SIZE OF RAM
        #   /dev/sdx2 = swap = SIZE OF RAM
        #   This should work for most cases
        cmd = str("blockdev --getsize64 /dev/" + setupconfig.disk)
        size = int(subprocess.check_output(cmd, shell=True).decode())
        ramsize = int(os.sysconf("SC_PAGE_SIZE") * os.sysconf("SC_PHYS_PAGES")) / 1000 / 1000
        data = (size / 1000 / 1000) - ramsize

        Disks().part_disk(setupconfig, data)

        yield "60,creating filesystems"
        # Create FS
        Disks().makefs(setupconfig)


        yield "80,mounting disk"
        # mount disk
        Disks().mount(setupconfig)

        yield "100,done!"
