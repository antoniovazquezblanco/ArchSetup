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
    # locale.conf             [?] (not fully tested)
    # create time link        [x]
    # generate locales        [ ]
    # mkinitcpio              [?] Configuration?
    # set root password       [x]
    # save keyboard layout    [x]
    # save font               [x]
    # Install GRUB2           [x] (might chooseable in future?)
    # Installing basic deamons[ ] (config?)
    # Create User             [x]
    # Copy Mirrorlist list.txt[x]
    # -----> Soon: Xorg + Configuration


    def run(setupconfig):

        yield "2,Generating fstab"
        os.system("genfstab -p /mnt >> /mnt/etc/fstab")

        yield "4,Setting Hostname"
        os.system("echo " +setupconfig.hostname + " > /mnt/etc/hostname")

        yield "6,Setting up locale config"
        os.system("echo LANG=" +setupconfig.mainlocale + " > /mnt/etc/locale.conf")
        file= open("/etc/locale.gen", "r")
        x = file.readlines()
        file.close();
        out = open("/mnt/etc/locale.gen", "w")
        for line in x:
            for y in setupconfig.locales:
                if y in line:
                    out.write(y)
                    continue
            out.write(line)

        os.system("arch-chroot /mnt locale-gen > /dev/null 2> /dev/null")

        yield "8,Setting Timezone"

        os.system("ln /mnt/usr/share/zoneinfo/" +setupconfig.timezone + "/" + setupconfig.timesubzone + " /mnt/etc/localtime")

        yield "15,Setting Keymap"
        os.system("echo KEYMAP=" + setupconfig.keyboard + " > /mnt/etc/vconsole.conf")

        yield "16,Setting Font"
        os.system("echo FONT=" +setupconfig.font + " >> /mnt/etc/vconsole.conf")

        yield "25,Generating Boot Image"
        os.system("arch-chroot /mnt mkinitcpio -p linux > /dev/null 2> /dev/null")

        yield "28,Creating User"
        os.system("arch-chroot /mnt useradd -d " +setupconfig.homedir + " -c \'" +setupconfig.realname +"\' -s /bin/bash -m " +setupconfig.username)
        os.system("echo " +setupconfig.username + ":" + setupconfig.password + " >passlist")

        yield "30,Setting root password"
        os.system("echo root:" + setupconfig.rootpassword + " >> passlist")
        os.system("arch-chroot /mnt chpasswd < passlist")
        os.system("rm passlist") # it is import to clean up the password file

        yield "35,Updating package database"
        os.system("arch-chroot /mnt pacman-db-upgrade > /dev/null 2> /dev/null") # To prevent problems with older install ISOs

        yield "40,Updating Mirrorlist"
        os.system("cp list.txt /mnt/etc/pacman.d/mirrorlist")

        yield "45,Installing Bootloader"
        os.system("arch-chroot /mnt pacman -Sy grub --noconfirm > /dev/null 2>/dev/null")
        os.system("arch-chroot /mnt grub-install --recheck /dev/" + setupconfig.disk + "> /dev/null 2> /dev/null")
        os.system("arch-chroot /mnt grub-mkconfig -o /boot/grub/grub.cfg > /dev/null 2> /dev/null")







        yield "100,done!"
