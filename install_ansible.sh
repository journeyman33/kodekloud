#!/bin/bash

password="mjolnir123"

# Use sudo for the entire script
echo "$password" | sudo -S bash <<EOF
yum install epel-next-release -y
yum install ansible -y
cp /home/thor/kodekloud-engineer/ansible.cfg /etc/ansible/ansible.cfg
cp /home/thor/kodekloud-engineer/environments/hosts /etc/ansible/hosts
EOF

