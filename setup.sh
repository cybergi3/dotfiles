#!/bin/bash

sudo pacman -S python3 python-pip git nitrogen picom i3-gaps dmenu alacritty xorg-server xorg-xinit xorg-xrandr fish wget --needed --noconfirm

/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/JetBrains/JetBrainsMono/master/install_manual.sh)"

pip install i3ipc

git clone https://aur.archlinux.org/yay-bin
cd yay-bin
makepkg
sudo pacman -U yay-bin-*
cd ..
yay -S polybar-git
yay -S librewolf-bin
sudo mv /bin/alacritty /bin/alacritty-term
sudo cp alacritty /bin
sudo chmod +x /bin/alacritty

mkdir ~/.config/i3
mkdir ~/.config/polybar
mkdir ~/.config/alacritty

cp config ~/.config/i3/config
cp alacritty.yml ~/.config/alacritty
cp polybar-config.ini ~/.config/polybar/config.ini

sudo cp res /bin

