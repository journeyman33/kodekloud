#!/bin/bash

echo mjolnir123 | sudo -S yum install epel-next-release -y

echo mjolnir123 | sudo -S yum install ansible -y

echo  mjolnir123 | sudo -S cp /home/thor/kodekloud-engineer/ansible.cnf /etc/ansible/ansible.cfg
