
import os
from time import sleep

lang =  str(input("choose a language: "))
os.system(f'echo you entered {lang}')
os.system(f'echo LANG={lang} >> /etc/locale.conf')
os.system(f'echo LANG={lang} >> /etc/locale.gen')
os.system('pwd')
os.system('cat /etc/locale.conf')
sleep(5)
os.system('locale.gen')
sleep(5)
keymap =  str(input("choose a keymap: "))
os.system(f'echo you entered {keymap}')
os.system(f'echo KEYMAP={keymap} >> /etc/vconsole.conf')
os.system('cat /etc/vconsole.conf')
sleep(5)
hostname = str(input("choose a hostname: "))
os.system(f'echo you entered {hostname}')
os.system(f'echo {hostname} >> /etc/hostname')
os.system('cat /etc/hostname')
sleep(5)

os.system(f'''  echo "127.0.0.1      localhost
::1            localhost
127.0.1.1      {hostname}.localdomain      {hostname}" >> /etc/hosts''')
os.system('cat /etc/hosts')
sleep(5)

os.system('passwd')
os.system('pacman -S grub networkmanager network-manager-applet dialog wireless_tools wpa_supplicant os-prober mtools dosfstools linux-headers')
os.system('grub-install --target=i386-pc /dev/vda')
os.system('grub-mkconfig -o /boot/grub/grub.cfg')
restart = input("Restart now? [Y/N]").strip().upper
if restart == 'Y':
  os.system('reboot')
