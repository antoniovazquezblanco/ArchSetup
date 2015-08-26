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

import subprocess
import os

class Font:
    def __init__(self):
        pass

    def list_console_fonts(self):
        fntlist=subprocess.check_output("(cd /usr/share/kbd/consolefonts/ && find . -type f -name '*.psf.gz' -o -name '*.psfu.gz') | sed 's/.\\/\\(.*\\).psf.gz/\\1/' | sed 's/.\\/\\(.*\\).psfu.gz/\\1/'", shell=True).decode().split('\n')
        fntlist.remove('')
        fntlist.sort()
        return fntlist

    def load_console_font(self, font):
        os.system("setfont " + font)
        #Now, if font is to big, the setup will crash -> check if we have a mimimum of
        # 22 lines and 42 cols
        try:
            cols = int(subprocess.check_output("echo -n $COLUMNS", shell=True).decode())
            lines= int(subprocess.check_output("echo -n $LINES"  , shell=True).decode())
        except:
            return
        if(cols < 42 or lines < 25):
            os.system("setfont") # load default
        else:
            return

    def set_console_font():
        print("[D] SetupTools.set_console_font(): Not implemented!")

