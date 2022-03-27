import os
from time import sleep

print('\033[1;94m')
op = str(input("Are you using wifi?[S/N] ")).strip().upper()
if op == 'S':
  os.system('systemctl start NetworkManager')
  os.system('nmtui')
else:
  os.system('systemctl start NetworkManager')
user = str(input('Choose a user name: '))
os.system(f'useradd -m -G wheel {user}')
os.system(f'passwd {user}')
print('\033[1;96m')
driver = str(input("Are you using Intel, AMD or Nvidia? ")).strip().upper()
if driver == 'INTEL':
  print('\033[1;91mInstalling Intel drivers')
  sleep(2)
  os.system('sudo pacman -S xf86-video-intel')
elif driver == 'AMD':
  print('\033[1;91mInstalling AMD drivers')
  sleep(2)
  os.system('sudo pacman -S xf86-video-amdgpu')
elif driver == 'NVIDIA':
  print('\033[1;91mInstalling Nvidia drivers')
  sleep(2)
  os.system('sudo pacman -S nvidia nvidia-utils')
print('\033[1;92mInstalling Applications')
sleep(2)
os.system('sudo pacman -S xorg-server xorg-xinit')
de = str(input('Choose a Desktop Environment [Enlightenment, Gnome, Plasma, Xfce]')).strip().lower()
if de == 'enlightenment'
  os.system('sudo pacman -S --needed lightdm lightdm-gtk-greeter')
  os.system('sudo pacman -S efl enlightenment')
  os.system('pacman -S archlinux-wallpaper flatpak terminology kitty baobab evince gparted mpv neofetch htop thunderbird gnome-calculator gthumb libreoffice ecrire')
  os.system('flatpak install io.gitlab.librewolf-community')
  os.system('systemctl enable lightdm')
if de == 'gnome'
  os.system('sudo pacman -S gdm')
  os.system('sudo pacman -S gnome gnome-terminal nautilus gnome-tweaks gnome-layout-switcher gnome-control-center gnome-backgrounds adwaita-icon-theme')
  os.system('pacman -S archlinux-wallpaper flatpak kitty baobab evince gparted mpv neofetch htop thunderbird gnome-calculator gthumb libreoffice gedit')
  os.system('flatpak install io.gitlab.librewolf-community')
  os.system('systemctl enable gdm')
os.system('sudo cp /myarchscript/kitty.conf /home/felipe/.config/kitty')
os.system('nano /etc/sudoers')
os.system('nano /etc/locale.gen')
reboot = str(input('Reboot now? [Y/N]')).strip().upper()
if reboot == 'Y':
  os.system('reboot')
