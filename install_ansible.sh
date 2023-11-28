#!/bin/bash

# Check if the script is running as root
if [ "$EUID" -ne 0 ]
  then echo "Please run as root"
  exit
fi

yum install epel-next-release -y
yum install ansible -y
cp /home/thor/kodekloud/ansible.cfg /etc/ansible/ansible.cfg
cp /home/thor/kodekloud/inventory/hosts /etc/ansible/hosts

