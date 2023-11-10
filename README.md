# KodeKloud Engineer   -   THIS IS A WORK IN PROGRESS   -

Hello my name is Charles Vosloo 👋

- This repository contains scripts that helped me with KodeKloud Engineer question, KodeKloud course (like ultimate CKAD) and can be run on KodeKloud playgrounds.
- These are in the form of ansible playbooks. It is actually quite easy to install ansible on a remote server.
- The following TUI tools have helped me:
- For kubernetes questions, it is very useful to have k9s installed, particularly if you are doing a long question or doing any troubelshooting. And the why not just install some kubectl pluging that you are used to like ctx,ns or neat.   
- For git questions, I like lazygit, it cuts down on the need to memorizing commands.
- For writing ansible palybooks, the default vi editor doesn't cut it, so I insall vim and vim-essentials. Ansible syntax highlighting/suggestions is trciky: this requres a lengthy .virmrc complete with plugin manager. I like the helix editor, but I haven't found a quick way to instlal it on centos.          
- What's really cool, with having ansible installed, I am able to do many KodeKloud Engineer linux questions, using Anisble the way it was intended to be used.   



| Nautilus Servers         |      SSH                 | Easy One Command to SSH to Server (using sshpass)                             |
|--------------------------|--------------------------|:-----------------------------------------------------------------------------:|
| Stratos App 1            |  tony@stapp01            |  `sshpass -p Ir0nM@n ssh -o StrictHostKeyChecking=no tony@172.16.238.10`      |
| Stratos App 2            |  steve@stapp02           |  `sshpass -p Am3ric@ ssh -o StrictHostKeyChecking=no steve@172.16.238.11`     |
| Stratos App 3            |  banner@stapp03          |  `sshpass -p BigGr33n ssh -o StrictHostKeyChecking=no banner@172.16.238.12`   |
| Stratos Load Balancer    |  loki@stlb01             |  `sshpass -p Mischi3f ssh -o StrictHostKeyChecking=no loki@172.16.238.14`     |
| Stratos Database Server  |  peter@stdb01            |  `sshpass -p 'Sp!dy' ssh -o StrictHostKeyChecking=no peter@172.16.239.10`     |
| Stratos Storage Server   |  natasha@ststor01        |  `sshpass -p Bl@kW ssh -o StrictHostKeyChecking=no natasha@172.16.238.15`     |
| Stratos Backup Server    |  clint@stbkp01           |  `sshpass -p H@wk3y3 ssh -o StrictHostKeyChecking=no clint@172.16.238.16`     |
| Stratos Mail Server      |  groot@stmail01          |  `sshpass -p Gr00T123 ssh -o StrictHostKeyChecking=no groot@172.16.238.17`    |
| Jenkins Server           |  jenkins@jenkins         |  `sshpass -p 'j@rv!s' ssh -o StrictHostKeyChecking=no jenkins@172.16.238.19`  |

## Using Ansible to do Linux tasks

The best way to learn ansible is to use for all server configuration tasks as it was intended for. Many of the Linux KodeKloud Engineer questions can be done using ansible. I first leaned this from [Anh Nguyen](https://github.com/ntheanh201/kodekloud-engineer), where he provides solutions to KodeKloud Engineer linux challenges using ansible. So, instead here, I am going to provide my methodology here with an example. After installing and setting up ansible on jump host, a chatGPT prompt can help produce a sample playbook that might only need some tweaking.

1. The first step is to clone the repo on Jump Server 
```
git clone https://github.com/CharlesVosloo/kodekloud.git
```
2. Run this script to install ansible and copy ansible.cfg and ansible inventory hosts file from the repo to the default /etc/ansible/ location which means that ansible can be run from anywhere.
```
cd /home/thor/kodekloud 
sudo -s 
./install_ansible.sh  
```
```
#!/bin/bash
yum install epel-next-release -y
yum install ansible -y
cp /home/thor/kodekloud/ansible.cfg /etc/ansible/ansible.cfg
cp /home/thor/kodekloud/environments/hosts /etc/ansible/hosts
```

The ansible host file contains the following inventory items with the variables ansible_host, ansible_ssh_user and ansible_ssh_pass hard coded. The following ansible ad hoc commands should all work:  

 Nautilus Servers            | Ansible ad hoc command            | alias
|----------------------------|-----------------------------------|---------------|
| stapp01, stapp02, stapp03  |  ansible webservers -m ping       | webservers
| Stratos App 1              |  ansible stapp01 -m ping          | stapp01                                         |
| Stratos App 2              |  ansible stapp02 -m ping          | stapp02                                          |
| Stratos App 3              |  ansible atapp03 -m ping          | stapp03
| Stratos Load Balancer      |  ansible loadbalancer -m ping     | loadbalancer 
| Stratos Database Server    |  ansible database -m ping         | storage
| Stratos Backup Server      |  ansible backup -m ping           | backup
| Stratos Mail Server        |  ansible mail -m ping             | mail

3. You are now ready to write a playbook









# Getting Started

## On Jump host

- Clone the repository: `git clone https://github.com/CharlesVosloo/kodekloud-engineer.git`
- Go to folder: `cd kodekloud-engineer`
- Run this scipt as roor: `./install_ansible.sh`
- This scipt installs epel-release and ansible and then sets up ansible by copying the KodeKlode servers inventory file to ansible's default lcation /etc/ansible/anisble.cfg and configires /etc/anisible/hosts. 
- Ansible ad hoc cammands can be run from any location

## An example of how to solve linux problems with ansible

## Playbook 1: configure jump host for ansible devlepment questions
## Playbook 2: for git questions
## Playbook 3: for kubernetes questions
## Playbook 4  for ultimat CKAD 
