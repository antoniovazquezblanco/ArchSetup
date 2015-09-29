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

from glob import glob
import subprocess

class Software:
    def __init__(self):
        pass

    def listPackages(self):
        return glob("software/*")

    def installPackages(self, pkglist):
        for pkg in pkglist:
            with open(pkg) as f:
                apps = f.readlines()
                cmds = []
                buff = apps[:]

                for entry in buff:
                    if(entry[:3] == '$: '):
                        apps.remove(entry)
                        cmds.append("".join(entry).replace('\n', '').replace('$: ', ''))

                applications = " ".join(apps).replace('\n', '')
                p = subprocess.Popen(["arch-chroot", "/mnt", "pacman", "--noconfirm", "-S"] + applications.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                for line in p.stdout:
                    yield line.decode("utf-8")

                for cmd in cmds:
                    pc = subprocess.Popen(["arch-chroot", "/mnt"] + cmd.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    for line in pc.stdout:
                        yield line.decode("utf-8")
