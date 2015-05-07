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

class Interface:
    def __init__(self, callback):
        self.callback = callback
        self._keep_running = True

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
            # Hide cursor...
            curses.curs_set(0)
            # Enter the main loop...
            self._loop()
            # Set everything back to normal
            curses.curs_set(1)
            self.screen.keypad(0)
            curses.echo()
            curses.nocbreak()
            curses.endwin()
        except:
            # In event of error, restore terminal to sane state.
            curses.curs_set(1)
            self.screen.keypad(0)
            curses.echo()
            curses.nocbreak()
            curses.endwin()
            # Print the exception...
            traceback.print_exc()

    def _loop(self):
        self.callback(event='init')
        self._refresh()
        while self._keep_running:
            event = self.screen.getch()
            if event == curses.KEY_RESIZE:
                self._resize()
            else:
                self.window.event(event)

    def exit(self):
        self._keep_running = False

    def _resize(self):
        (y, x) = self.screen.getmaxyx()
        if hasattr(self, 'window'):
            self.window.resize(y, x)
        self._refresh()

    def _refresh(self):
        self.screen.erase()
        self.screen.refresh()
        if hasattr(self, 'window'):
            self.window.refresh()

    def setbgattrs(self, bg=curses.COLOR_BLACK, fg=curses.COLOR_WHITE):
        curses.init_pair(1, fg, bg)
        self.screen.bkgdset(curses.color_pair(1))
        self._refresh()

    def addwin(self, window):
        if hasattr(self, 'window'):
            self.window.hide()
        self.window = window
        self.window.show()
        self.window.event(ord('\t'))
        self._resize()
