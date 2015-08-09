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

class PostInstall:
    def __init__(self):
        pass

    # Tasks:
    #
    # generate fstab          [x]
    # Hostname                [x]
    # locale.conf             [ ]
    # create time link        [x]
    # generate locales        [ ]
    # mkinitcpio              [?] Configuration?
    # set root password       [x]
    # save keyboard layout     [x]
    # save font               [x]
    # Install GRUB2           [x] (might chooseable in future?)
    # Installing basic deamons[ ]
    # Copy Mirrorlist list.txt[ ]
    # -----> Soon: Xorg + Configuration


    def run(setupconfig):

        yield "2,Generating fstab"
        os.system("genfstab -p /mnt >> /mnt/etc/fstab")

        yield "4,Setting Hostname"
        os.system("echo " +setupconfig.hostname + " > /mnt/etc/hostname")

        yield "6,Setting up locale config"
        #
        # TODO: setupconfig.locale is a list of many locales, but
        #       which should be used?


        yield "8,Setting Timezone"

        os.system("ln /mnt/usr/share/zoneinfo/" +setupconfig.timezone + "/" + setupconfig.timesubzone + " /mnt/etc/localtime")

        yield "15,Setting Keymap"
        os.system("echo KEYMAP=" + setupconfig.keyboard + " > /mnt/etc/vconsole.conf")

        yield "16,Setting Font"
        os.system("echo FONT=" +setupconfig.font + " >> /mnt/etc/vconsole.conf")

        yield "25,Generating Boot Image"
        os.system("arch-chroot /mnt mkinitcpio -p linux > /dev/null 2> /dev/null")

        yield "30,Setting root password"
        os.system("arch-chroot /mnt echo " + setupconfig.rootpassword + " \| passwd --stdin root")

        yield "40,Installing Bootloader"
        os.system("arch-chroot /mnt pacman -Sy grub --noconfirm > /dev/null 2>/dev/null")
        os.system("arch-chroot /mnt grub-install --recheck /dev/" + setupconfig.disk + "")
        os.system("arch-chroot /mnt grub-mkconfig -o /boot/grub/grub.cfg")





        yield "100,done!"
