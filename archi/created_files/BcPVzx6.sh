#!/bin/bash
clear

if [ $(tput colors) ]; then # Checks if terminal supports colors
	red="\e[31m"
	green="\e[32m"
	endcolor="\e[39m"
fi

echo ====================
echo "We are not responsible for any damages that may possibly occur while using Arrow"
echo ====================
echo "   "

sleep 2

sudo -s <<ARROW

# Update pacman
echo "Updating pacman (may take a while)"
(
pacman -Syy
) &> /dev/null && echo -e "$green OK $endcolor" || echo -e "$red FAILED $endcolor";
echo 'Installing google-chrome'
( 
yaourt -S google-chrome --needed
) &> /dev/null && echo -e "$green OK $endcolor" || echo -e "$red FAILED $endcolor"; 
echo 'Installing numix-themes'
( 
sudo pacman -S numix-themes --needed
) &> /dev/null && echo -e "$green OK $endcolor" || echo -e "$red FAILED $endcolor"; 
echo 'Installing FileZilla'
( 
sudo pacman -S filezilla --needed
) &> /dev/null && echo -e "$green OK $endcolor" || echo -e "$red FAILED $endcolor"; 
echo "Upgrading old packages"
(
pacman -Syu 
) &> /dev/null && echo -e "$green OK $endcolor" || echo -e "$red FAILED $endcolor";
ARROW
exit 0