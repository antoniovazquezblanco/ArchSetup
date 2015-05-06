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

class Pane:
    def __init__(self, window, sizex, sizey):
        self.window = window
        self.sizex = sizex
        self.sizey = sizey
        self.pane =  self.window.newpane()
        self.pane.border()
        self.resize()

    def refresh(self):
        self.window.refresh()
        self.pane.refresh()

    def resize(self):
        self.window.resize()
        height, width =  self.window.getsize()
        self.pane.resize(self.sizey, self.sizex)
        self.pane.mvwin(int((height-4-self.sizey)/2), int((width-2-self.sizex)/2))
        self.refresh()

    def addwidget():
        print("[D] Pane.addwidget(): Not implemented!")

