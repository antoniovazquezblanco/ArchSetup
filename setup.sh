#
#   Start script for ArchSetup
#   check if python is installed and handles ArchSetup start
#
python ArchSetup 2> /dev/null #dont print errors
x="$?"
if [ "$x" != "0" ]
then
    if [ "$x" == "1" ]
    then
        echo "Keyboard interupt!"
        exit 130
    fi
    if [ "$x" != "127" ]
    then
        echo "Unknown error :("
        exit 1
    fi
    echo "Startup failed."
    echo "It looks like the install medium is missing python..."
    echo "  >> installing Python >= 3.4.X:"
    pacman -S python --noconfirm
    clear
    echo "  >> Done!"
    echo "Now trying to restart..."
    python ArchSetup
    if [ "$?" != "0" ]
    then
        echo "Failed again..."
        echo "  >> No way to fix error..."
        echo "  >> Suggestions:"
        echo "      >> redownload the Install ISO/Setup"
        echo "      >> If using development version"
        echo "          >> Report bug (!)"
        echo "          >> use stable release (if available)"
        exit 1
    fi
    echo "Worked on second try!"
fi
