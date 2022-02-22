import os

op = str(input("Are you using wifi?[S/N] ")).strip().upper()
if op == 'S':
  os.system('systemctl enable NetworkManager')
  os.system('systemctl start NetworkManager')
  os.system('nmtui')
else:
  os.system('systemctl enable NetworkManager')
  os.system('systemctl start NetworkManager')
user = str(input('Choose a user name: '))
os.system(f'useradd -m -G wheel {user}')
os.system(f'passwd {user}')
os.system('echo %wheel ALL=ALL(ALL:AL) ALL >> /etc/sudoers')
driver = str(input("Are you using Intel, AMD or Nvidia? ")).strip().upper()
if driver == 'INTEL':
  os.system('sudo pacman -S xf86-video-intel')
elif driver == 'AMD':
  os.system('sudo pacman -S xf86-video-amdgpu')
elif driver == 'NVIDIA':
  os.system('sudo pacman -S nvidia nvidia-utils')

os.system('sudo pacman -S xorg-server xorg-xinit')
os.system('sudo pacman -S ttf-linux-libertine noto-fonts-emoji')
os.system('pacman -S gdm')
os.system('systemctl enable gdm')
os.system('pacman -S gnome gnome-terminal nautilus gnome-tweaks gnome-control-center gnome-backgrounds adwaita-icon-theme')
os.system('pacman -S flatpak')
os.system('flatpak install io.gitlab.librewolf-community')
reboot = str(input('Reboot now? [S/N]')).strip().upper()
os.system('reboot')
