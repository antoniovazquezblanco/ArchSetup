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
from Interface.Window import Window
from Interface.TextWidget import TextWidget
from Interface.ButtonWidget import ButtonWidget

class SetupWindow(Window):
    def __init__(self):
        super().__init__()

    def setnextcallback(self, callback, event):
        (y, x) = self.size()
        if hasattr(self, 'button_prev'):
            y = y - 2
        self.button_next = ButtonWidget(y, x-8, 'Next >')
        self.button_next.setcallback(callback, event)
        self.addwidget(self.button_next, True)

    def setprevcallback(self, callback, event):
        (y, x) = self.size()
        if hasattr(self, 'button_next'):
            y = y - 2
        self.button_prev = ButtonWidget(y, 2, '< Prev')
        self.button_prev.setcallback(callback, event)
        self.addwidget(self.button_prev, True)

    def addwidget(self, widget, skip=False):
        if not skip and (hasattr(self, 'button_prev') or hasattr(self, 'button_next')):
            raise Exception('Cannot add content after setting up callbacks...')
        super().addwidget(widget)
