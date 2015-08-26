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

from Interface.Windows.SetupWindow import SetupWindow
from Interface.Widgets.TextWidget import TextWidget
from Interface.Widgets.ProgressWidget import ProgressWidget

from SetupTools.PreInstall import PreInstall

import gettext

class PreInstallWindow(SetupWindow):
    def __init__(self, callback, setupconfig):
        super().__init__()
        self.setupconfig = setupconfig
        self.callback    = callback

        self.has_runned = False # Make sure this window does only 'execute' once

        # Init Translation
        trans = gettext.translation("archsetup", "locale", fallback=True)
        trans.install()

        self.addwidget(TextWidget(1, 1, _('Please wait...'),  40))
        self.progress = self.addwidget(ProgressWidget(2, 1, 0, 40))
        self.status   = self.addwidget(TextWidget(3, 1, ' ', 40))

        self.next = self.setnextcallback(callback, '')


    def event(self, event, opt=''):
        if event == 'refresh':
            quit()
        elif event == 'showed':
            if self.has_runned == False:
                for x in PreInstall.run(self.setupconfig):
                    list = x.split(',')
                    self.progress.setvalue(int(list[0]))
                    self.status.settext(_(list[1]))
                    self.refresh()
            self.has_runned = True
            self.next.setcallback(self.callback, 'next')
            self.callback("next") # auto continue to next window
        else:
            super().event(event)
