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
import logging
from Interface.Widgets.Widget import Widget

class ButtonWidget(Widget):
    def __init__(self, y, x, text):
        super().__init__(y, x, 1, len(text))
        self.text = text

    def draw(self, window):
        (posy, posx) = self.position()
        if not self.ishighlighted():
            window.addstr(posy, posx, self.text)
        else:
            window.addstr(posy, posx, self.text, curses.A_REVERSE | curses.A_UNDERLINE)

    def setcallback(self, callback, event):
        self.callback = callback
        self.event_param = event

    def event(self, event):
        if event == ord('\n'):
            self.callback(self.event_param)
