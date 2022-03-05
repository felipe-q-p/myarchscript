import os
from time import sleep

op = str(input("\033[1;94mAre you using wifi?[S/N] ")).strip().upper()
if op == 'S':
  os.system('systemctl start NetworkManager')
  os.system('nmtui')
else:
  os.system('systemctl start NetworkManager')
user = str(input('Choose a user name: '))
os.system(f'useradd -m -G wheel {user}')
os.system(f'passwd {user}')
driver = str(input("\033[1;96mAre you using Intel, AMD or Nvidia? ")).strip().upper()
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
os.system('sudo pacman -S --needed lightdm lightdm-gtk-greeter')
os.system('sudo pacman -S efl enlightenment')
os.system('pacman -S archlinux-wallpaper flatpak terminology kitty baobab gparted gthumb rage ecrire')
os.system('flatpak install io.gitlab.librewolf-community')
os.system('systemctl enable lightdm')
os.system('sudo cp /myarchscript/kitty.conf /home/felipe/.config/kitty')
os.system('nano /etc/sudoers')
os.system('nano /etc/locale.gen')
reboot = str(input('Reboot now? [Y/N]')).strip().upper()
if reboot == 'Y':
  os.system('reboot')
