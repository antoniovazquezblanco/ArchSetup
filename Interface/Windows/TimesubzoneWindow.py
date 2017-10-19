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

from SetupTools.Timezone import Timezone
from Interface.Windows.SetupWindow import SetupWindow
from Interface.Widgets.SpacerWidget import SpacerWidget
from Interface.Widgets.TextWidget import TextWidget
from Interface.Widgets.ScrollWidget import ScrollWidget
from Interface.Widgets.RadioWidget import RadioWidget

import gettext

class TimesubzoneWindow(SetupWindow):
    def __init__(self, callback, setupconfig):
        super().__init__()

        # Init Translation
        trans = gettext.translation("archsetup", "locale", fallback=True)
        trans.install()

        # Init setup tools
        self.timezone = Timezone()
        self.setupconfig = setupconfig

        # Add widgets and setup callbacks...
        self.addwidget(TextWidget(1, 1, _('Please select a subzone...'),  40))

        # Loading subzones with '*' loads every available subzone, this makes
        # sure that the pad will be large enough to hold every subset
        self.radiowidget = RadioWidget(0, 0, 40, self.timezone.list_subzones('*'), self.event)

        self.scroller = ScrollWidget(3, 1, 40, 20, self.radiowidget, self.event)
        self.addwidget(self.scroller)
        self.addwidget(SpacerWidget(23, 1, 1))
        self.setnextcallback(callback, 'next')
        self.setprevcallback(callback, 'prev')

    def event(self, event, opt=''):
        if event == 'show':
            self.radiowidget.setlist(self.timezone.list_subzones(self.setupconfig.gettimezone()))
            self.radiowidget.select(0)
            self.scroller.setPos(0)
            self.refresh()
        elif event == 'refresh':
            self.refresh()
        elif event == 'selection':
            self.setupconfig.settimesubzone(opt)
        else:
            super().event(event)
