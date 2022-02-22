echo "enter the name for the partition (ex: /dev/sdd): "
read disk
echo "you entered $disk"
cfdisk $disk
fdisk -l
mkfs.ext4 /dev/vda1
mount /dev/vda1 /mnt
pacstrap /mnt base linux linux-firmware base-devel nano
genfstab -U /mnt >> /mnt/etc/fstab
arch-chroot /mnt
nano /etc/locale.gen
echo "choose a language from the list above"
read lang
echo "you entered $lang"
echo LANG=$lang >> /etc/locale.conf
locale-gen
echo "choose a keymap from the list above"
read keymap
echo "you entered $keymap"
echo KEYMAP=$keymap>> /etc/vconsole.conf
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


