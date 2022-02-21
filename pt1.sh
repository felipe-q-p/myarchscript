echo "enter the name for the partition (ex: /dev/sdd): "
read disk
echo "you entered $disk"
cfdisk $disk
mkfs.ext4 /dev/vda1
mount /dev/vda1 /mnt
pacstrap /mnt base linux linux-firmware base-devel nano
genfstab -U /mnt >> /mnt/etc/fstab
arch-chroot /mnt
cat /etc/locale.gen
nano /etc/locale.gen
locale-gen
echo "choose a language from the list above"
read lang
echo "you entered $lang"
echo LANG=$lang >> /etc/locale.conf
cat /etc/vconsole.conf
echo "choose a keymap from the list above"
read keymap
echo "you entered $keymap"
echo KEYMAP=$keymap>> /etc/vconsole.conf
