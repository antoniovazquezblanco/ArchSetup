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
from Interface.Widget import Widget

class ScrollWidget(Widget):
    def __init__(self, y, x, w, h, widget, callback):
        self.widget = widget
        self.callback = callback
        (sy, sx) = widget.size()
        self.pad = curses.newpad(sy, sx)
        self.padpos = 0
        self.curspos = 0
        super().__init__(y, x, h, w)

    def draw(self, window):
        self.widget.draw(self.pad)

    def refresh(self, window):
        (wposy, wposx) = window.getbegyx()
        (posy, posx) = self.position()
        (sy, sx) = self.size()
        self.pad.refresh(self.padpos, 0, wposy+posy, wposx+posx, wposy+sy+3, wposx+sx)

    def event(self, event):
        if event == curses.KEY_UP:
            self.curspos = self.curspos - 1
            if self.curspos < 0:
                self.curspos = 0
                self.padpos = self.padpos - 1
                if self.padpos < 0:
                    self.padpos = 0
            self.widget.event(event)
            self.callback('refresh')
        elif event == curses.KEY_DOWN:
            self.curspos = self.curspos + 1
            (sy, sx) = self.size()
            if self.curspos > sy:
                self.curspos = sy
                self.padpos = self.padpos + 1
                (wsy, wsx) = self.widget.size()
                if self.padpos > wsy-sy-1:
                    self.padpos = wsy-sy-1
            self.widget.event(event)
            self.callback('refresh')
        else:
            self.widget.event(event)
