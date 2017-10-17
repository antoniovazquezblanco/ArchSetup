#!/usr/bin/env python3
import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from SetupTools.SetupConfig import SetupConfig
from Interface.Interface import Interface
import importlib
import logging

class Previewer:
    def __init__(self):
        logging.basicConfig(filename='ArchSetup.preview.log', level=logging.DEBUG, format='%(asctime)s - [%(relativeCreated)6d] - %(name)s - %(levelname)s - %(message)s')
        self.setupconfig = SetupConfig()
        self.interface = Interface(self.callback)
        self.interface.loop()

    def callback(self, event):
        if event == 'init':
            self.windows = []
            self.window_index = 0

            for x in sys.argv[1:]:
                i = importlib.import_module("Interface.Windows."+x)
                cl = getattr(i, x)
                self.windows.append(cl(self.callback, self.setupconfig))

            self.interface.addwin(self.windows[self.window_index])

        elif event == 'prev':
            self.window_index -= 1
            self.interface.addwin(self.windows[self.window_index])

        elif event == 'next':
            self.window_index += 1

            if self.window_index == len(self.windows):
                self.interface.exit()
                return

            self.interface.addwin(self.windows[self.window_index])

if __name__ == "__main__":
    Previewer()
