echo "enter the name for the partition (ex: /dev/sdd): "
read disk
echo "you entered $disk"
cfdisk $disk
fdisk -l
mkfs.ext4 /dev/vda1
mount /dev/vda1 /mnt
pacstrap /mnt base linux linux-firmware base-devel nano git
genfstab -U /mnt >> /mnt/etc/fstab
arch-chroot /mnt

