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

class Timezone:
    def __init__(self):
        pass

    def list_zones(self):
        zonelist=subprocess.check_output("(cd /usr/share/zoneinfo/ && find -maxdepth 1 ! -path . -type d -printf '%f\n') | sed 's/[a-zA-Z0-9_\-]*/& &/'", shell=True).decode().split('\n')
        zonelist.remove('')
        return zonelist

    def list_subzones(self, zone):
        szonelist=subprocess.check_output("(cd /usr/share/zoneinfo/"+zone+"/ && find -maxdepth 1 ! -path . -printf '%f\n') | sed 's/[a-zA-Z0-9_\-]*/& &/')", shell=True).decode().split('\n')
        szonelist.remove('')
        return szonelist
	
