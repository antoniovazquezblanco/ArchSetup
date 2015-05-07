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

import logging
import curses
from curses import panel
from Interface.TextWidget import TextWidget

class Window:
    def __init__(self):
        win = curses.newwin(0, 0, 0, 0)
        self.panel = panel.new_panel(win)
        self.widgets = []
        self._compute()
        self.refresh()
        self.addwidget(TextWidget(1, 1, 'Very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very long text...', 150))

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

    def resize(self, y, x):
        logging.debug('Window.resize(y='+str(y)+', x='+str(x)+')')
        posy = int((y-self.sizey)/2)
        posx = int((x-self.sizex)/2)
        self.panel.move(posy, posx)
