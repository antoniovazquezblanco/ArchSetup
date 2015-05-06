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

import curses

class Win:
    def __init__(self, screen):
        self.screen = screen
        self.win = curses.newwin(1, 0)
        self.resize()

    def refresh(self):
        self.win.border(' ', ' ', 0, 0, ' ', ' ', ' ', ' ')
        self.screen.refresh()
        self.win.refresh()

    def resize(self):
        self.screen.clear()
        self.screen.refresh()
        self.screen.addstr(" Archlinux Setup")
        height, width = self.screen.getmaxyx()
        self.win.resize(height-1, width)
        self.win.mvwin(1, 0)
        self.refresh()

    def getsize(self):
        height, width = self.win.getmaxyx()
        return (height, width)

    def newpane(self):
        return self.win.subwin(1, 1)

    def addpane():
        print("[D] Pane.addwidget(): Not implemented!")

