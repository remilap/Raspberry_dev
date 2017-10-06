#!/bin/sh

if [ "$1" = "" -o "$1" = "-h" ]; then
  echo "$0 [role_name]"
  exit 1
fi

role=$1
if [ -d roles/${role} ]; then
  echo "${role} already exists"
  exit 2
fi

mkdir -p roles/${role}/tasks roles/${role}/handlers roles/${role}/templates roles/${role}/vars

cat << EOF > roles/${role}/tasks/main.yml
---
# file: roles/${role}/tasks/main.yml
# This playbook contains ${role} plays that will be run on all nodes.

- name: ...
  template: src=wpa_supplicant.conf.j2 dest=/etc/wpa_supplicant/wpa_supplicant.conf
  notify: reboot

- name: ...
  apt: name={{ item }} state=installed update_cache={{ update_cache }}
  with_items: ...

- name: ...
  command: "/bin/bash -c 'curl -sLS https://apt.adafruit.com/add | sudo bash'"
  changed_when: "'python-apt is already the newest version.' not in aptget.stdout_lines"
  #changed_when:

EOF

cat << EOF > roles/${role}/handlers/main.yml
---
# file: roles/${role}/handlers/main.yml
# Handler to handle ${role} notifications. Handlers are called by other plays.
# See http://docs.ansible.com/playbooks_intro.html for more information about handlers.

- name: reboot
  command: shutdown -r -y now "Ansible updates triggered"
  async: 0
  poll: 0
  ignore_errors: true

- name: restart ntpd
  service: name=ntpd state=restarted

EOF

cat << EOF > roles/${role}/templates/example.conf.j2

driftfile /var/lib/ntp/drift

restrict 127.0.0.1 
restrict -6 ::1

server {{ ntpserver }}

includefile /etc/ntp/crypto/pw

keys /etc/ntp/keys

EOF

