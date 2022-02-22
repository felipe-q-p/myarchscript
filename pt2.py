import os

lang =  str(input("choose a language from the list above"))
os.system(f'echo you entered {lang}')
echo LANG=lang >> /etc/locale.conf
nano /etc/locale.gen
cd /mnt
locale-gen
pwd
echo "choose a keymap from the list above"
read keymap
echo "you entered $keymap"
echo KEYMAP=$keymap >> /etc/vconsole.conf
echo "choose a hostname"
read hostname
echo "you entered $hostname"
echo /etc/hostname $hostname
echo /etc/hosts "127.0.0.1      localhost
::1            localhost
127.0.1.1      $hostname.localdomain      $hostname"
passwd
pacman -S grub networkmanager network-manager-applet dialog wireless_tools wpa_supplicant os-prober mtools dosfstools linux-headers
grub-install --target=i386-pc /dev/vda
grub-mkconfig -o /boot/grub/grub.cfg
echo "Please exit and reboot your system"
