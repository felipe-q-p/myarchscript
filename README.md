# Myarchscript
## Important: This script only works for DOS machines. UEFI is not supported yet
Myarchscript is a project which helps users to install Arch Linux. This project is not an entirely new distribution and mantains the majority of the Arch Linux standard settings, such as the command line based installation, however easier due to the automation scripts, written in python and shell script. Some programs, such as the enlightenment window manager, flatpak, leafpad and librewolf browser are included.
## Instructions (pt 0):
1. Firstly, you need the Arch Linux ISO, which can be downloaded on Arch Linux official site.
2. After this, you need to create a bootable usb device (if you want to install in your machine). For VM this is not necessary.
3. When you boot for the first time is important to check your connection using the ping command (ex:'ping archlinux.org') and, if you are using wifi, connect using 'nmtui' command.
4. Now you have to upgrade your system (pacman -Syu) and install git (pacman -S git).
5. With git installed, you can now clone this repository, with 'git clone https://github.com/felipe-q-p/myarchscript/' and a new directory called myarchscript will be created. Go to this directory and source the first part ('source pt1.sh'). The installation will start.
## Instructions (pt 1):
1. Now you have to create a DOS partition on your disk
2. You do not need to create a /boot or a /home partition
3. In this script the swap partition is not created. (you can do this latter, if you prefer)
4. Ok. Now your partitions are mounted and you are on your /mnt partition (where the programs is going to be installed)
## Instructions (pt 2):
1. Now, because you are in another directory, you have to clone again this repository and source /myarchscript/pt2.sh
