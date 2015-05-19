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
# along with ArchSetup.  If not, see <http://www.gnu.org/license

from Interface.Windows.SetupWindow import SetupWindow
from Interface.Widgets.SpacerWidget import SpacerWidget
from Interface.Widgets.TextWidget import TextWidget
from Interface.Widgets.EntryWidget import EntryWidget

import gettext

class HostnameWindow(SetupWindow):
    def __init__(self, callback, setupconfig):
        super().__init__()
        self.callback = callback

        # Init Translation
        trans = gettext.translation("archsetup", "locale", fallback=True)
        trans.install()

        self.setupconfig = setupconfig
        self.addwidget(TextWidget(1, 1, _('Please enter a hostname:'),  40))
        self.entry = self.addwidget(EntryWidget(3, 1, "hostname", 40, self.event, 40))
        self.addwidget(SpacerWidget(23, 1, 1))
        self.next = self.setnextcallback(callback, '')
        self.setprevcallback(callback, 'prev')

    def event(self, event, opt=''):
        if event == 'refresh':
            self.refresh()
            if len(self.entry.gettext()) > 0:
                self.setupconfig.sethostname(self.entry.gettext())
                self.next.setcallback(self.callback, 'next')
            else:
                self.next.setcallback(self.callback, '')
        else:
            super().event(event)
