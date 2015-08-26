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

class Locale:
    def __init__(self):
        pass

    def list_locales(self):
        llist=subprocess.check_output("cat /etc/locale.gen", shell=True).decode().split('\n')
        # First 23 lines are just instructions
        llist=llist[23:len(llist)-1]
        tmplist = llist[:]
        llist.clear()
        for x in tmplist:
            x = x.replace('#', '')
            llist.append(x)
        llist.sort()
        return llist

