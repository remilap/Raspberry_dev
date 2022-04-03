#!/bin/sh

username=remi
if [ "$1" != "" ]; then
  username=$1
fi

#last_gid=$(grep -v nogroup /etc/group | cut -d: -f3 | sort -n | tail -n 1)
#new_gid=$((last_gid+1))
#last_id=$(grep -v nobody /etc/passwd | cut -d: -f3 | sort -n | tail -n 1)
#new_id=$((last_id+1))

sudo groupadd ${username}
[ $? = 0 ] || exit 1
new_gid=$(grep ${username} /etc/group | cut -d: -f3)
echo "New group ${username} is created with gid ${new_gid}"

sudo useradd -m -g ${username} ${username}
[ $? = 0 ] || exit 1
echo "New user ${username} is created with id "$(id -u ${username})

sudo adduser ${username} sudo
[ $? = 0 ] || exit 1
echo "User ${username} is allowed to use sudo"

echo "${username} ALL=(ALL) NOPASSWD: ALL" | sudo tee /etc/sudoers.d/010_${username}-nopasswd
[ $? = 0 ] || exit 1
echo "User ${username} is allowed to use sudo without password"

group_list="www-data docker"
for g in ${group_list}; do
  sudo adduser ${username} ${g}
  [ $? = 0 ] || exit 1
  echo "User ${username} is added in the ${g} group"
done

