pacman -S git
echo "enter the name for the partition (ex: /dev/sdd): "
read disk
echo "you entered $disk"
cfdisk $disk
