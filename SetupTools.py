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

class SetupTools:
    def __init__(self):
        if os.geteuid() != 0:
            print("[W] No root permissions...")

    def list_keyboard_layouts(self):
        kbdlist=subprocess.check_output(["localectl", "list-keymaps"]).decode().split('\n')
        kbdlist.remove('')
        return kbdlist

    def load_keyboard_layout():
        #loadkeys layout
        print("[D] SetupTools.load_keyboard_layout(): Not implemented!")

    def set_keyboard_layout():
        print("[D] SetupTools.set_keyboard_layout(): Not implemented!")

    def list_console_fonts(self):
        fntlist=subprocess.check_output("(cd /usr/share/kbd/consolefonts/ && find . -type f -name '*.psf.gz' -o -name '*.psfu.gz') | sed 's/.\\/\\(.*\\).psf.gz/\\1/' | sed 's/.\\/\\(.*\\).psfu.gz/\\1/'", shell=True).decode().split('\n')
        fntlist.remove('')
        return fntlist

    def load_console_font():
        #setfont $font
        print("[D] SetupTools.load_console_font(): Not implemented!")

    def set_console_font():
        print("[D] SetupTools.set_console_font(): Not implemented!")

    def generate_locale():
        #locale-gen
        print("[D] SetupTools.generate_locale(): Not implemented!")

    def check_internet():
        #ping -c 5 www.google.com > /dev/null
        print("[D] SetupTools.check_internet(): Not implemented!")

    def add_user():
        print("[D] SetupTools.add_user(): Not implemented!")

