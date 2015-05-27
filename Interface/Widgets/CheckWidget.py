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

class CheckWidget(Widget):
    def __init__(self, y, x, w, items, callback):
        self.items = items
        self.callback = callback
        self.selected = 0
        self.activated = []
        self.callback('selection', [])
        super().__init__(y, x, len(items), w)

    def __selection_changed(self):
        ret = []
        for x in self.activated:
            ret.append(self.items[int(x)])
        self.callback('selection', ret)

    def draw(self, window):
        (posy, posx) = self.position()
        (sy, sx) = self.size()
        i = 0
        ch = '  '
        for item in self.items:
            if i in self.activated:
                ch = '> '
            else:
                ch = '  '
            if self.selected == i:
                if self.ishighlighted():
                    window.addstr(posy + i, posx, ch + item, curses.A_STANDOUT)
                else:
                    window.addstr(posy + i, posx, ch + item)
            else:
                window.addstr(posy + i, posx, ch + item)
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
            return
        elif event == curses.KEY_DOWN:
            self.selected = self.selected + 1
            (sy, sx) = self.size()
            if self.selected > len(self.items)-1:
                self.selected = len(self.items)-1
            self.callback('refresh')
            return
        elif event == ord(' '):
            if self.selected not in self.activated:
                self.activated.append(self.selected)
            else:
                self.activated.remove(self.selected)
            self.__selection_changed()
            self.callback('refresh')
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
