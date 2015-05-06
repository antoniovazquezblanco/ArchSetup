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

class Interface:
    def __init__(self, callback):
        logging.debug('Interface.__init__()')
        self.callback = callback

    def loop(self):
        try:
            # Initialize curses
            self.screen = curses.initscr()
            # Initialize colors
            curses.start_color()
            self.colors_enabled = curses.has_colors()
            # Turn off echoing of keys, and enter cbreak mode,
            # where no buffering is performed on keyboard input.
            curses.noecho()
            curses.cbreak()
            # In keypad mode, escape sequences for special keys
            # (like the cursor keys) will be interpreted and
            # a special value like curses.KEY_LEFT will be returned
            self.screen.keypad(1)
            # Default attributes...
            self.setbgattrs()
            # Enter the main loop...
            self._loop()
            # Set everything back to normal
            self.screen.keypad(0)
            curses.echo()
            curses.nocbreak()
            curses.endwin()
        except:
            # In event of error, restore terminal to sane state.
            self.screen.keypad(0)
            curses.echo()
            curses.nocbreak()
            curses.endwin()
            # Print the exception...
            traceback.print_exc()

    def _loop(self):
        logging.debug('Interface._loop()')
        self.callback(event='init')
        self._refresh()
        while True:
            event = self.screen.getch()
            logging.debug('Interface._getch(' + str(int(event)) + ')')
            if event == curses.KEY_RESIZE:
                self._resize()
            elif event == ord("q"):
                break

    def _resize(self):
        logging.debug('Interface._resize()')
        (y, x) = self.screen.getmaxyx()
        if hasattr(self, 'window'):
            self.window.resize(y, x)
        self._refresh()

    def _refresh(self):
        logging.debug('Interface._refresh()')
        self.screen.erase()
        self.screen.refresh()
        if hasattr(self, 'window'):
            self.window.refresh()

    def setbgattrs(self, bg=curses.COLOR_BLACK, fg=curses.COLOR_RED):
        curses.init_pair(1, fg, bg)
        self.screen.bkgdset(curses.color_pair(1))
        self._refresh()

    def addwin(self, window):
        logging.debug('Interface.addwin()')
        if hasattr(self, 'window'):
            self.window.hide()
        self.window = window
        self.window.show()
        self._refresh()
