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

import os
import subprocess

class Keyboard:
    def __init__(self):
        pass

    def list_keyboard_layouts(self):
        kbdlist = []
        try:
            kbdlist=subprocess.check_output(["localectl", "list-keymaps"]).decode().split('\n')
            kbdlist.remove('')
        except subprocess.CalledProcessError:
            # This is a temporal fix while localectl bug is not fixed...
            kbdpath=subprocess.check_output(["find", "/usr/share/kbd/keymaps", "-name", "*.map*"]).decode().split('\n')
            kbdpath.remove('')
            for k in kbdpath:
                kbdlist.append(os.path.basename(k).split('.map')[0])
            kbdlist.sort()
        return kbdlist

    def load_keyboard_layout():
        #loadkeys layout
        print("[D] SetupTools.load_keyboard_layout(): Not implemented!")

    def set_keyboard_layout():
        print("[D] SetupTools.set_keyboard_layout(): Not implemented!")

