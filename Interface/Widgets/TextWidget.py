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

import textwrap
import curses
from Interface.Widgets.Widget import Widget

class TextWidget(Widget):
    def __init__(self, y, x, text, n, maxheight=10):
        self.lines = textwrap.wrap(text, width=n)
        self.n = n
        height = len(self.lines)
        self.maxheight = maxheight
        if height > maxheight:
            self.lines = self.lines[:maxheight - 1]
            self.lines.append("...")
            height = maxheight
        super().__init__(y, x, height, n)

    def draw(self, window):
        if not self.isvisible():
            return

        (posy, posx) = self.position()
        i = 0
        for line in self.lines:
            try: # I don't know why the pacstrap script fails here, but this should be a workaround until I found a fix...
                if self.ishighlighted():
                    window.addstr(posy + i, posx, line, curses.A_STANDOUT)
                else:
                    window.addstr(posy + i, posx, line)

                i = i+1
            except:
                pass

    def focus(self, focus):
        return False

    def settext(self, text):
        self.lines = textwrap.wrap(text, width=self.n)
        height = len(self.lines)

        if height > self.maxheight:
            self.lines = self.lines[:self.maxheight - 1]
            self.lines.append("...")
            height = self.maxheight

        self.resize(height, self.n)

    def append(self, text):
        pass
