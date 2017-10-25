#!/bin/bash

filelist=$(find . -name *.py)

pylint ArchSetup $filelist \
	--disable=all \
	--enable=E	\
	--disable=E0602

if [ "$?" == "127" ]
then
	echo "It looks like pylint is not installed, you should try the following:"
	echo
	echo ">> pip3 install pylint"
fi
