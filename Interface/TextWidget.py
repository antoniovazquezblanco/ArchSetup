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
from Interface.Widget import Widget

class TextWidget(Widget):
    def __init__(self, y, x, text, n):
        self.lines = textwrap.wrap(text, width=n)
        super().__init__(y, x, len(self.lines), n)

    def draw(self, window):
        (posy, posx) = self.position()
        i = 0
        for line in self.lines:
            if self.ishighlighted():
                window.addstr(posy + i, posx, line, curses.A_STANDOUT)
            else:
                window.addstr(posy + i, posx, line)
            i = i+1
