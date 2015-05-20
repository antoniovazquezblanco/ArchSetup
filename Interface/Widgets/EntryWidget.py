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
import curses.ascii
import logging
from Interface.Widgets.Widget import Widget

class EntryWidget(Widget):
    def __init__(self, y, x, text, cols, callback, maxwidth):
        super().__init__(y, x, 1, maxwidth)
        self.text = text
        self.cols = cols
        self.callback = callback
        self.maxwidth = maxwidth

    def draw(self, window):
        (posy, posx) = self.position()
        if not self.ishighlighted():
            window.addstr(posy, posx, self.text.center(self.cols), curses.A_REVERSE)
        else:
            window.addstr(posy, posx, (self.text + '_').center(self.cols), curses.A_REVERSE | curses.A_UNDERLINE)

    def event(self, event):
        if event == curses.KEY_BACKSPACE or event == curses.ascii.DEL:
            self.text = self.text[:-1]
            self.callback("refresh")
            return
        elif len(self.text) < self.maxwidth-1 and curses.ascii.isprint(event):
            self.text = self.text + chr(event)
            self.callback("refresh")
            return
        elif event == ord('\n'):
            self.callback(ord('\t'))
            return
        else:
            super().event(event)

    def gettext(self):
        return self.text

    def settext(self, text):
        self.text = text
        self.callback("refresh")
