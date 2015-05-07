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
        button = ButtonWidget(1, 1, 'Next >')
        button.setcallback(self._callback, 'button')
        self.addwidget(button)

    def _callback(self, event):
        logging.debug('SetupWindow._callback(event=' + event + ')')
        self.addwidget(TextWidget(3, 1, 'Short text...', 40))
        self.refresh()
