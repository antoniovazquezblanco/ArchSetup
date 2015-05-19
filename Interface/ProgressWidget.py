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

class ProgressWidget(Widget):
    def __init__(self, y, x, percent, length):
        self.percent = percent
        self.length = length
        super().__init__(y, x, 1, length)

    def draw(self, window):
        (posy, posx) = self.position()
        if self.ishighlighted():
            window.addstr(posy, posx, '[' + '#' * int(((self.length - 6) / 100 * self.percent)) + ' ' * int(self.length - 6 - int(((self.length - 6)) / 100 * self.percent)) + ']' + str(self.percent) + '%', curses.A_STANDOUT)
        else:
            window.addstr(posy, posx, '[' + '#' * int(((self.length - 6) / 100 * self.percent)) + ' ' * int(self.length - 6 - int(((self.length - 6)) / 100 * self.percent)) + ']' + str(self.percent) + '%')


    def setvalue(self, value):
        if value > 100:
            self.percent = 100
        else:
            self.percent = value


    def focus(self, focus):
        return False
