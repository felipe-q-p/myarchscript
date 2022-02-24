import os

op = str(input("Are you using wifi?[S/N] ")).strip().upper()
if op == 'S':
  os.system('systemctl start NetworkManager')
  os.system('nmtui')
else:
  os.system('systemctl start NetworkManager')
user = str(input('Choose a user name: '))
os.system(f'useradd -m -G wheel {user}')
os.system(f'passwd {user}')
driver = str(input("Are you using Intel, AMD or Nvidia? ")).strip().upper()
if driver == 'INTEL':
  os.system('sudo pacman -S xf86-video-intel')
elif driver == 'AMD':
  os.system('sudo pacman -S xf86-video-amdgpu')
elif driver == 'NVIDIA':
  os.system('sudo pacman -S nvidia nvidia-utils')

os.system('sudo pacman -S xorg-server xorg-xinit')
os.system('sudo pacman -S --needed lightdm lightdm-gtk-greeter')
os.system('sudo pacman -S efl enlightenment')
os.system('pacman -S archlinux-wallpaper flatpak terminology kitty baobab gparted gtkhash ephoto rage ecrire')
os.system('flatpak install io.gitlab.librewolf-community')
os.system('systemctl enable lightdm')
os.system('nano /etc/sudoers')
os.system('nano /etc/locale.gen')
os.system('mv /myarchscript/kitty.conf .config/kitty')
reboot = str(input('Reboot now? [S/N]')).strip().upper()
if reboot == 'S':
  os.system('reboot')
