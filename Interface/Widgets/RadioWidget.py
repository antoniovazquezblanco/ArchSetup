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
from Interface.Widgets.Widget import Widget

class RadioWidget(Widget):
    def __init__(self, y, x, w, items, callback):
        self.items = items
        self.callback = callback
        self.selected = 0
        self.callback('selection', self.items[self.selected])
        super().__init__(y, x, len(items), w)

    def draw(self, window):
        (posy, posx) = self.position()
        (sy, sx) = self.size()
        i = 0
        for item in self.items:
            if self.selected == i:
                if self.ishighlighted():
                    window.addstr(posy + i, posx, '> ' + item, curses.A_STANDOUT)
                else:
                    window.addstr(posy + i, posx, '> ' + item)
            else:
                window.addstr(posy + i, posx, '  ' + item)
            i = i + 1

    def setlist(self, items):
        self.items = items
        (sy, sx) = self.size()
        self.resize(len(items), sx)
        self.callback('refresh')

    def __getindex(self, char, default):
        char = char.upper()
        for i in range(len(self.items)):
            if self.items[i][0].upper() == char:
                return i
        return default

    def event(self, event):
        if event == curses.KEY_UP:
            self.selected = self.selected - 1
            if self.selected < 0:
                self.selected = 0
            self.callback('refresh')
            self.callback('selection', self.items[self.selected])
            return
        elif event == curses.KEY_DOWN:
            self.selected = self.selected + 1
            (sy, sx) = self.size()
            if self.selected > len(self.items)-1:
                self.selected = len(self.items)-1
            self.callback('refresh')
            self.callback('selection', self.items[self.selected])
            return
        elif event == ord('\n'):
            self.callback(ord('\t'))
            return
        elif curses.ascii.isprint(event):
            offset = self.__getindex(chr(event), self.selected)-self.selected
            if offset > 0:
                for i in range(offset):
                    self.callback(curses.KEY_DOWN)
            else:
                for i in range(-offset):
                    self.callback(curses.KEY_UP)
            return
        else:
            super().event(event)
