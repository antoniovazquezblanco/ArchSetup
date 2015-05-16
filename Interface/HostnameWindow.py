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

from Interface.SetupWindow import SetupWindow
from Interface.SpacerWidget import SpacerWidget
from Interface.TextWidget import TextWidget
from Interface.EntryWidget import EntryWidget

import gettext

class HostnameWindow(SetupWindow):
    def __init__(self, callback, setupconfig):
        super().__init__()

        # Init Translation
        trans = gettext.translation("archsetup", "locale", fallback=True)
        trans.install()

        self.setupconfig = setupconfig
        self.addwidget(TextWidget(1, 1, _('Please enter a hostname:'),  40))
        self.entry = self.addwidget(EntryWidget(3, 1, "hostname", 40, self.event, 40))
        self.addwidget(SpacerWidget(23, 1, 1))
        self.setnextcallback(callback, 'next')
        self.setprevcallback(callback, 'prev')

    def event(self, event, opt=''):
        if event == 'refresh':
            self.refresh()
            self.setupconfig.sethostname(self.entry.gettext())
        else:
            super().event(event)
