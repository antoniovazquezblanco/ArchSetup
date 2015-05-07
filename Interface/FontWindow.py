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

from SetupTools.Font import Font
from Interface.SetupWindow import SetupWindow
from Interface.TextWidget import TextWidget
from Interface.RadioWidget import RadioWidget

class FontWindow(SetupWindow):
    def __init__(self, callback, setuptools):
        super().__init__()
        self.addwidget(TextWidget(1, 1, 'Please select a console font...',  40))
        font = Font()
        items = font.list_console_fonts()
        self.addwidget(RadioWidget(3, 1, 40, 20, items, self.event))
        self.setnextcallback(callback, 'next')
        self.setprevcallback(callback, 'prev')

    def event(self, event):
        if event == 'refresh':
            self.refresh()
        else:
            super().event(event)
