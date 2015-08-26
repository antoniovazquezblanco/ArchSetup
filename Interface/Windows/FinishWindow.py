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

import gettext

class FinishWindow(SetupWindow):
    def __init__(self, callback):
        super().__init__()

        # Init Translation
        trans = gettext.translation("archsetup", "locale", fallback=True)
        trans.install()

        self.addwidget(TextWidget(1, 1, _('All done!'),  40))
        self.addwidget(TextWidget(3, 1, _('Archlinux is setup in your computer. The program will exit when you click in the next button.'), 40))
        self.setnextcallback(callback, 'next')
        self.setprevcallback(callback, 'prev')
