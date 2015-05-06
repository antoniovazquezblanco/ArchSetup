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
from curses import panel
import logging

class Window:
    def __init__(self):
        logging.debug('Window.__init__()')
        win = curses.newwin(10, 10, 10, 10)
        self.panel = panel.new_panel(win)
        self.refresh()

    def show(self):
        logging.debug('Window.show()')
        self.panel.show()

    def hide(self):
        logging.debug('Window.hide()')
        self.panel.hide()

    def refresh(self):
        logging.debug('Window.refresh()')
        win = self.panel.window()
        win.box()
        win.refresh()

    def resize(self, y, x):
        logging.debug('Window.resize(y=' + str(y) + ', x=' + str(x) + ')')
