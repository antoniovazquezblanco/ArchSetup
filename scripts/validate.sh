#!/bin/bash
pylint ArchSetup \
	--disable=all \
	--enable=E		# Only enable Error

if [ "$?" == "127" ]
then
	echo "It looks like pylint is not installed, you should try the following:"
	echo
	echo ">> pip3 install pylint"
fi	


