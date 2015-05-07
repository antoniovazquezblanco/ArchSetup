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

import signal
import logging
import curses
from curses import panel

class Window:
    def __init__(self):
        win = curses.newwin(0, 0, 0, 0)
        self.panel = panel.new_panel(win)
        self.widgets = []
        self._compute()
        self.refresh()

    def addwidget(self, widget):
        self.widgets.append(widget)
        self._compute()

    def _compute(self):
        ymax = 0
        xmax = 0
        for widget in self.widgets:
            (ypos, xpos) = widget.position()
            (ysize, xsize) = widget.size()
            if ypos+ysize > ymax:
                ymax = ypos+ysize
            if xpos+xsize > xmax:
                xmax = xpos+xsize
        self.sizey = ymax+1
        self.sizex = xmax+1
        win = self.panel.window()
        win.resize(self.sizey, self.sizex)
        self.resize()

    def refresh(self):
        win = self.panel.window()
        win.erase()
        win.box()
        for widget in self.widgets:
            widget.draw(win)
        win.refresh()

    def show(self):
        self.panel.show()

    def hide(self):
        self.panel.hide()

    def resize(self, y=-1, x=-1):
        if y != -1:
            self.screeny = y
        if x != -1:
            self.screenx = x
        if not hasattr(self, 'screeny') or not hasattr(self, 'screenx'):
            return
        posy = int((self.screeny-self.sizey)/2)
        posx = int((self.screenx-self.sizex)/2)
        self.panel.move(posy, posx)
        curses.panel.update_panels()

    def size(self):
        return self.panel.window().getmaxyx()

    def event(self, event):
        if event == ord('\t'):
            # On tab highligh widgets iteratively...
            high = False
            for widget in self.widgets:
                if high == True:
                    if widget.highlight(True):
                        self.refresh()
                        return
                high = widget.ishighlighted()
                if high == True:
                    widget.highlight(False)
            for widget in self.widgets:
                if widget.highlight(True):
                    self.refresh()
                    return
        else:
            for widget in self.widgets:
                if widget.ishighlighted():
                    widget.event(event)
                    return
