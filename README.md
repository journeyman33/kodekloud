

Hello 🖐️ <br>
My name is Charles Vosloo.<br><br> This is part of my <span style="color: red;">*journey*</span> learning DevOps while doing [KodeKloud Engineer](https://engineer.kodekloud.com/) challenges.
## Table of Contents
1. [Easy One Command to SSH to Nautilus Servers](##3.-Easy-One-Command-to-SSH-to-Nautilus-Servers)
1. [Scripts](##2.-Scripts)
1. [Using Ansible to do Linux tasks](##3.-Using-Ansible-to-do-Linux-tasks)
1. [How to Deploy applications to Kubernetes - Link to my Hugo Blog site](https://journeyman33.github.io/hugo-site/)
1.   


   


## 1. Easy One Command to SSH to Nautilus Servers
| Server         |      User                 |  SSH                             |
|--------------------------|--------------------------|:-----------------------------------------------------------------------------|
| jump_host                |  thor@jump_host          |  `sshpass -p mjolnir123 ssh -o StrictHostKeyChecking=no thor@jump_host`            |
| Stratos App 1            |  tony@stapp01            |  `sshpass -p Ir0nM@n ssh -o StrictHostKeyChecking=no tony@172.16.238.10`      |
| Stratos App 2            |  steve@stapp02           |  `sshpass -p Am3ric@ ssh -o StrictHostKeyChecking=no steve@172.16.238.11`     |
| Stratos App 3            |  banner@stapp03          |  `sshpass -p BigGr33n ssh -o StrictHostKeyChecking=no banner@172.16.238.12`   |
| Stratos Load Balancer    |  loki@stlb01             |  `sshpass -p Mischi3f ssh -o StrictHostKeyChecking=no loki@172.16.238.14`     |
| Stratos Database Server  |  peter@stdb01            |  `sshpass -p 'Sp!dy' ssh -o StrictHostKeyChecking=no peter@172.16.239.10`     |
| Stratos Storage Server   |  natasha@ststor01        |  `sshpass -p Bl@kW ssh -o StrictHostKeyChecking=no natasha@172.16.238.15`     |
| Stratos Backup Server    |  clint@stbkp01           |  `sshpass -p H@wk3y3 ssh -o StrictHostKeyChecking=no clint@172.16.238.16`     |
| Stratos Mail Server      |  groot@stmail01          |  `sshpass -p Gr00T123 ssh -o StrictHostKeyChecking=no groot@172.16.238.17`    |
| Jenkins Server           |  jenkins@jenkins         |  `sshpass -p 'j@rv!s' ssh -o StrictHostKeyChecking=no jenkins@172.16.238.19`  |

## 2. Scripts
After SSHing into the server I usually run one these scripts, depending on the task.
 
| /scripts (folder)        | What is does                                     | For  
|-------------------     |--------------------------------------------------|----------------------
|1.install_ansible.sh    |Installs ansible on jump host, copies  inventory file to jump host.     |Linux tasks: e.g. Configure Stratos App Severs
|2. install_lazygit.sh   |Installs lazygit                                  |Git tasks (on centos)
|3. webi_k9s.sh          |Installs vim nd k9d  using webi                   |Kubernetes tasks (on centos)
|4. webi_k9s_krew.sh     |Install k9s using webi, ctx and ns using krew     |Kubernetes tasks (on ubuntu)
|5.webi_vim_ansible.sh      | Install vim, configures .vimrc for for writing ansible playbooks in yaml    |Ansible tasks (centos)
|
1. install_ansible.sh .<br>
     See example in 3. [Using Ansible to do Linux tasks](##2.-Using-Ansible-to-do-Linux-tasks)
2. install_lazygit.sh .<br>
     My goto cli TUI tool for doing complicated tasks with git.   
   
3.  webi_k9s.sh .<br> 
    [webi](https://webinstall.dev/webi/) is an uncomplicated way to install development tools on remote servers, but setting up usually involves more steps than the advertised one line (hence  the above script):
 ```bash
   curl https://webi.sh/webi | sh
``` 


 The webi_k9s.sh script uses webi to install only k9s and vim-essentials and dnf to install vim and git (required by webi). But you could for example install some of the following additional packages with the now newly insalled webi command:
```bash
webi lf bat gh jq ripgrep zoxide brew 
```   
But expect to wait a long time, especially if you are installing brew.


4. webi_k9s_krew.sh .<br>
   I use this script on Kodekloud's Kubernetes Playgrounds and useful on the Kodekloud Ultimate CKAD course which runs on Ubuntu. 

## 3. Using Ansible to do Linux tasks

The best way to learn ansible is to use for all server configuration tasks as it was intended for. Many of the Linux KodeKloud Engineer questions can be done using ansible. I first leaned this from [Anh Nguyen](https://github.com/ntheanh201/kodekloud-engineer), where he provides solutions to KodeKloud Engineer linux challenges using ansible. So, instead here, I am going to provide my methodology here with an example. After installing and setting up ansible on jump host, a chatGPT prompt can help produce a sample playbook that might only need some tweaking :-).

1. The first step is to clone this repo on Jump Server 
```bash
git clone https://github.com/journeyman33/kodekloud.git
```
2. Then copy these lines Run to install the ansible install script on jump host. 
```bash
cd /home/thor/kodekloud 
sudo -s 
./scripts/install_ansible.sh  
```
 The ansible install script listed below will also copy ansible.cfg and the ansible inventory hosts file from the repo to the default /etc/ansible/hosts location on jump host which means that ansible can be run from anywhere and target the hostnames found in this file. 

```bash
#!/bin/bash
yum install epel-next-release -y
yum install ansible -y
cp /home/thor/kodekloud/ansible.cfg /etc/ansible/ansible.cfg
cp /home/thor/kodekloud/inventory/hosts /etc/ansible/hosts
```

Below is a table summarizing the usage of the ansible ping ad hoc command, which can now target all Nuatilus Servers using the hostnames (inventory aliases) listed below.  

 Nautilus Server(s)            | Ansible ad hoc command            | hostname
|----------------------------|-----------------------------------|---------------|
| stapp01, stapp02, stapp03  |  ansible webservers -m ping       | webservers
| Stratos App 1              |  ansible stapp01 -m ping          | stapp01                                         |
| Stratos App 2              |  ansible stapp02 -m ping          | stapp02                                          |
| Stratos App 3              |  ansible atapp03 -m ping          | stapp03
| Stratos Load Balancer      |  ansible loadbalancer -m ping     | loadbalancer 
| Stratos Database Server    |  ansible database -m ping         | storage
| Stratos Backup Server      |  ansible backup -m ping           | backup
| Stratos Mail Server        |  ansible mail -m ping             | mail 



3. Now, let's create a playbook!

Let's say the linux task is to<br>
``
   "install httpd and git on the hostname 'webservers' (all 3 Strtos Appserver), 
   and make sure Apache is listning on port 81" 
``<br>
The imperative way to think about this task would be:
```bash
ssh tony@stapp01 steve@stapp01 banner@stapp03
sudo -s;  yum install git -y; yum install httpd  -y 
sudo sed -i 's/^Listen 80/Listen 81/' /etc/httpd/conf/httpd.conf
systemctl start httpd
``````
[chatGpt](https://chat.openai.com/) will give you boilerplate yaml if you copy these command and ask for a comparable playbook.
You will see that the playbook requires 2 modules: the yum (or package) module and the lineinfile module.

However, the original word prompt, quoted above, gave me the answer right off the bat!
```yaml
cat > httpd.yaml <<EOF
---
- name: Install httpd and git on webservers
  hosts: webservers
  become: true  # Run tasks with elevated privileges (sudo)

  tasks:
    - name: Install httpd and git
      yum:
        name:
          - httpd
          - git
        state: present
      tags: 
        - install_packages

    - name: Update HTTPD port to 81
      lineinfile:
        path: /etc/httpd/conf/httpd.conf
        regexp: '^Listen 80'
        line: 'Listen 81'
      notify: Restart HTTPD
      tags: 
        - update_httpd_port

  handlers:
    - name: Restart HTTPD
      systemd:
        name: httpd
        state: restarted
EOF
```

Now, let's run the playbook  on jump_host
```bash
ansible-playbook httpd.yaml
```








