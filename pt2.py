
import os

lang =  str(input("choose a language: "))
os.system(f'echo you entered {lang}')
os.system(f'echo LANG={lang} >> /etc/locale.conf')
os.system('pwd')
keymap =  str(input("choose a keymap: "))
os.system(f'echo you entered {keymap}')
os.system(f'echo KEYMAP={keymap} >> /etc/locale.conf')
hostname = str(input("choose a hostname: "))
os.system(f'echo you entered {hostname}')
os.system(f'echo {hostname} >> /etc/hostname')
os.system(f'''  echo "127.0.0.1      localhost
::1            localhost
127.0.1.1      {hostname}.localdomain      {hostname}" >> /etc/hosts''')
os.system('passwd')
os.system('pacman -S grub networkmanager network-manager-applet dialog wireless_tools wpa_supplicant os-prober mtools dosfstools linux-headers')
os.system('grub-install --target=i386-pc /dev/vda')
os.system('grub-mkconfig -o /boot/grub/grub.cfg')
print("Please exit and reboot your system")
