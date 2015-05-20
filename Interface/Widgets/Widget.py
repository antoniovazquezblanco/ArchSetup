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

class Widget:
    def __init__(self, y, x, sy, sx):
        self.posy = y
        self.posx = x
        self.sizey = sy
        self.sizex = sx
        self.focused = False
        self.highlighted = False

    def position(self):
        return (self.posy, self.posx)

    def size(self):
        return (self.sizey, self.sizex)

    def resize(self, sy, sx):
        self.sizey = sy
        self.sizex = sx

    def draw(self, window):
        pass

    def refresh(self, window):
        pass

    def highlight(self, highligh):
        self.highlighted = highligh
        return highligh

    def ishighlighted(self):
        return self.highlighted

    def focus(self, focus):
        self.highlight(focus)
        self.focused = focus
        return focus

    def isfocused(self):
        return self.focused

    def event(self, event):
        pass
