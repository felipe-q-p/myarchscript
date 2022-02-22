import os

op = str(input("Are you using wifi?[S/N] ")).strip().upper()
if op == 'S':
  os.system('systemctl enable NetworkManager')
  os.system('systemctl start NetworkManager')
  os.system('nmtui')
else:
  os.system('systemctl enable NetworkManager')
  os.system('systemctl start NetworkManager')
