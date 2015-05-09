#!/bin/bash

#German Language
mkdir -p locale/de/LC_MESSAGES/
msgfmt translations/german.pot --output-file=locale/de/LC_MESSAGES/archsetup.mo

#English Language
mkdir -p locale/en/LC_MESSAGES/
msgfmt translations/english.pot --output-file=locale/en/LC_MESSAGES/archsetup.mo
