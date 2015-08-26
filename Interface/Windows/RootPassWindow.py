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
from Interface.Widgets.PasswordWidget import PasswordWidget
from Interface.Widgets.ProgressWidget import ProgressWidget

import gettext

class RootPassWindow(SetupWindow):
    def __init__(self, callback, setupconfig):
        super().__init__()
        self.callback = callback

        # Init Translation
        trans = gettext.translation("archsetup", "locale", fallback=True)
        trans.install()

        self.setupconfig = setupconfig
        self.addwidget(TextWidget(1, 1, _('Please choose a root password:'),  40))
        self.entry = self.addwidget(PasswordWidget(3, 1, "", 40, self.event, 40, '*'))
        self.addwidget(TextWidget(5, 1, _('Please confirm:'), 40))
        self.conf  = self.addwidget(PasswordWidget(7, 1, "", 40, self.event, 40, '*'))
        self.addwidget(TextWidget(9, 1, _('Password safety:'), 40))
        self.pro   = self.addwidget(ProgressWidget(10, 1, 0, 40))
        self.matcherr = self.addwidget(TextWidget(12, 1, _('Passwords do not match!'),  40))
        self.matcherr.setvisibility(False)
        self.next = self.setnextcallback(callback, '')
        self.setprevcallback(callback, 'prev')

    def event(self, event, opt=''):
        if event == 'refresh':
            if self.entry.gettext() == self.conf.gettext() and len(self.entry.gettext()) > 0: # Passwords Match
                self.setupconfig.setrootpassword(self.entry.gettext())
                self.next.setcallback(self.callback, 'next')
                self.matcherr.setvisibility(False)
            else:
                self.matcherr.setvisibility(True)
                self.next.setcallback(self.callback, '')
            self.pro.setvalue(int(100 / 20 * len(self.entry.gettext())))
            self.refresh()
        else:
            super().event(event)
