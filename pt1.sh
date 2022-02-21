echo "enter the name for the partition (ex: /dev/sdd): "
read disk
echo "you entered $disk"
cfdisk $disk
mkfs.ext4 /dev/vda1
mount /dev/vda1 /mnt
