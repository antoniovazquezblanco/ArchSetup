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

class SetupConfig:
    def __init__(self):
        pass

    def setkeyboard(self, layout):
        self.keyboard = layout

    def setfont(self, font):
        self.font = font

    def gettimezone(self):
        return self.timezone

    def settimezone(self, zone):
        self.timezone = zone

    def settimesubzone(self, subzone):
        self.timesubzone = subzone

    def sethostname(self, hostname):
        self.hostname = hostname

    def setdisk(self, disk):
        self.disk = disk;
