#/bin/bash
#
# Some useful Linux commands
# from https://omerkarabacak.medium.com/very-useful-and-not-much-known-linux-commands-that-you-probably-arent-using-in-your-daily-life-34f82a4a5eb2
#

nbMenu=$(grep "# MENU" $0 | grep -v grep | wc -l)
echo "nbMenu=$nbMenu"
grep "# MENU" $0 | grep -v grep | cut -d: -f2-

menu=10
echo "Choose one option"
read ans
if [ -n "$ans" ] && [ "$ans" -eq "$ans" ] 2>/dev/null; then
  if [ $ans -ge 1 ] && [ $ans -le $nbMenu ]; then
    menu=$ans
  else
    echo "should be between 1 and $nbMenu"
    exit
  fi
else
  echo "not a valid option"
  exit
fi

#NS#
#NS# redo the last command but as root
#NS# sudo !!
#NS#

#NS# Use the last command’s arguments
#NS# !$
#NS#

#NS# open an editor to run a command (probably a long one)
#NS# ctrl + x + e
#NS#

# MENU:1- create a super-fast disk for IO dependant task to run on it
if [ $menu = 1 ]; then
  mkdir -p /mnt/ramdisk && mount -t tmpfs tmpfs /mnt/ramdisk -o size=8192M
fi

#NS# don’t add the command to the history (add one space in front of the command)
#NS#  ls -l
#NS#

#NS# Fix or change a really long command that you run last with a text editor
#NS# fc
#NS#

#NS# create a tunnel with SSH to port that is not open to the public (local port 8080 -> remote host’s 127.0.0.1 on port 6070)
#NS# ssh -L 8080:127.0.0.1:6070 root@my-public-server.com -N
#NS#

#NS# Exit terminal but leave all processes running
#NS# disown -a && exit
#NS#

#NS# Clear your terminal without “clear” command
#NS# ctrl + l  # L
#NS#

#NS# Paste the arguments of the previous command
#NS# alt + -
#NS#

# MENU:2- completely clean and clear your terminal
if [ $menu = 2 ]; then
  reset
fi

# MENU:3- get CPU info quickly
if [ $menu = 3 ]; then
  cat /proc/cpuinfo
fi

# MENU:4- get memory info quickly
if [ $menu = 4 ]; then
  cat /proc/meminfo
fi

#NS# Find a text in a directory which has a lot of file in it recursively
#NS# grep -rn /etc/ -e text_to_find
#NS#

# MENU:5- find files bigger than 100 MB
if [ $menu = 5 ]; then
  find -type f -size +100M -exec ls -lah {} \;
fi

# MENU:6- create a webserver in the current directory to serve files in it
if [ $menu = 6 ]; then
  python -m SimpleHTTPServer
fi

# MENU:7- find your public IP
if [ $menu = 7 ]; then
  curl ifconfig.me
fi

# MENU:8- get a tree view of folders only 3 level
if [ $menu = 8 ]; then
  tree -L 3
fi

# MENU:9- get a tree view of processes
if [ $menu = 9 ]; then
  pstree
fi

# MENU:10- display other tips and tricks
if [ $menu = 10 ]; then
  grep "#NS#" $0 | grep -v "grep #NS#" | cut -c6-
fi
