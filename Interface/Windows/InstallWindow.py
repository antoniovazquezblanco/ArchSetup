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

from SetupTools.Pacstrap import Pacstrap
from Interface.Windows.SetupWindow import SetupWindow
from Interface.Widgets.SpacerWidget import SpacerWidget
from Interface.Widgets.TextWidget import TextWidget
from Interface.Widgets.ScrollWidget import ScrollWidget
from Interface.Widgets.RadioWidget import RadioWidget

import gettext

class InstallWindow(SetupWindow):
    def __init__(self, callback, setupconfig):
        super().__init__()

        # Init Translation
        trans = gettext.translation("archsetup", "locale", fallback=True)
        trans.install()

        self.has_runned = False

        self.setupconfig = setupconfig
        self.callback = callback
        self.addwidget(TextWidget(1, 1, _('Installing base system'),  40))
        self.status_label = TextWidget(3,1,"Install Log:", 40)
        self.addwidget(self.status_label)
        self.addwidget(SpacerWidget(23, 1, 1))
        self.next = self.setnextcallback(callback, '')

    def event(self, event, opt=''):
        if event == 'refresh':
            self.refresh()
        elif event == 'showed':
            if self.has_runned == False:
                for x in Pacstrap().run():
                    self.status_label.settext(str(x))
                    self.refresh()
            self.has_runned = True
            self.next.setcallback(self.callback, 'next')
        else:
            super().event(event)
