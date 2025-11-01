# 🧑‍💻 KodeKloud Engineer Journey
![KodeKloud Rank](https://img.shields.io/badge/KodeKloud_Rank-5th_–_363955_Points-blue?style=for-the-badge&logo=kubernetes)

![Update KodeKloud Stats](https://github.com/journeyman33/kodekloud/actions/workflows/update-kodekloud-stats.yml/badge.svg)

## 🏆 Live KodeKloud Leaderboard Status
<!-- KK_STATS_START -->
Fetching latest ranking...
<!-- KK_STATS_END -->
---
Hello 🖐️  
My name is **Charles Vosloo** — this repository is part of my *journey* learning **DevOps** while completing [KodeKloud Engineer](https://engineer.kodekloud.com/) challenges.

> **Note:**  
> “*KodeKloud Engineer tasks*” refer to the hands-on challenges offered by **Mumshad Mannambeth’s [KodeKloud educational platform](https://kodekloud.com/)** — one of the best environments for real-world DevOps practice.

---

## 📚 Table of Contents
1. [Easy One Command to SSH to Nautilus Servers](#1-easy-one-command-to-ssh-to-nautilus-servers)
2. [Scripts](#2-scripts)
3. [Using Ansible to do Linux tasks](#3-using-ansible-to-do-linux-tasks)
4. [How to Deploy Applications to Kubernetes — Blog Post](https://journeyman33.github.io/hugo-site/)

---

## 1. 🧩 Easy One Command to SSH to Nautilus Servers

| Server | User | SSH Command |
|--------|------|-------------|
| Jump Host | thor@jump_host | `sshpass -p mjolnir123 ssh -o StrictHostKeyChecking=no thor@jump_host` |
| Stratos App 1 | tony@stapp01 | `sshpass -p Ir0nM@n ssh -o StrictHostKeyChecking=no tony@172.16.238.10` |
| Stratos App 2 | steve@stapp02 | `sshpass -p Am3ric@ ssh -o StrictHostKeyChecking=no steve@172.16.238.11` |
| Stratos App 3 | banner@stapp03 | `sshpass -p BigGr33n ssh -o StrictHostKeyChecking=no banner@172.16.238.12` |
| Load Balancer | loki@stlb01 | `sshpass -p Mischi3f ssh -o StrictHostKeyChecking=no loki@172.16.238.14` |
| Database Server | peter@stdb01 | `sshpass -p 'Sp!dy' ssh -o StrictHostKeyChecking=no peter@172.16.239.10` |
| Storage Server | natasha@ststor01 | `sshpass -p Bl@kW ssh -o StrictHostKeyChecking=no natasha@172.16.238.15` |
| Backup Server | clint@stbkp01 | `sshpass -p H@wk3y3 ssh -o StrictHostKeyChecking=no clint@172.16.238.16` |
| Mail Server | groot@stmail01 | `sshpass -p Gr00T123 ssh -o StrictHostKeyChecking=no groot@172.16.238.17` |
| Jenkins Server | jenkins@jenkins | `sshpass -p 'j@rv!s' ssh -o StrictHostKeyChecking=no jenkins@172.16.238.19` |

---

## 2. ⚙️ Scripts

After SSHing into the server, I typically run one of these helper scripts from the `/scripts` folder depending on the task:

| Script | Description | Used For |
|--------|--------------|----------|
| `install_ansible.sh` | Installs Ansible on jump host, copies inventory file | Linux tasks (e.g. configure Stratos App servers) |
| `install_lazygit.sh` | Installs [Lazygit](https://github.com/jesseduffield/lazygit) | Git-related tasks |
| `webi_k9s.sh` | Installs Vim and [k9s](https://k9scli.io/) via [webi](https://webinstall.dev/webi/) | Kubernetes tasks |
| `webi_k9s_krew.sh` | Installs k9s with ctx and ns plugins via krew | Kubernetes (Ubuntu) tasks |
| `webi_vim_ansible.sh` | Installs and configures Vim for Ansible YAML editing | Ansible on CentOS |

Example command:
```bash
curl https://webi.sh/webi | sh
> 💡 *Tip:*  
> Webi can also install utilities like `lf`, `bat`, `jq`, `ripgrep`, and `zoxide`.  
> Just expect longer setup time, especially if you really want to install brew.
```
---

## 3. 🧠 Using Ansible to do Linux Tasks

The best way to learn **Ansible** is to **use it daily** for configuration management.  
Many Linux [KodeKloud Engineer](https://kodekloud-engineer.com/) tasks can be automated via playbooks.

> I first learned this approach from [Anh Nguyen’s repository](https://github.com/ntheanh201/kodekloud-engineer),  
> where he provides elegant Ansible-based solutions to KodeKloud challenges.

---

### 🪜 Step 1: Clone the Repo
```bash
git clone https://github.com/journeyman33/kodekloud.git
```
### 🧰 Step 2: Install and Configure Ansible
```bash
cd /home/thor/kodekloud
sudo -s
./scripts/install_ansible.sh

This script also copies:
  - ansible.cfg → /etc/ansible/ansible.cfg
  - inventory/hosts → /etc/ansible/hosts
```
Now Ansible can be executed from anywhere and can target hosts using the aliases defined in the inventory file.

---

## 📡 Example — Ping All Nautilus Servers

| Nautilus Server(s) | Ansible ad hoc command | Hostname |
|--------------------|------------------------|-----------|
| stapp01, stapp02, stapp03 | `ansible webservers -m ping` | webservers |
| Stratos App 1 | `ansible stapp01 -m ping` | stapp01 |
| Stratos App 2 | `ansible stapp02 -m ping` | stapp02 |
| Stratos App 3 | `ansible stapp03 -m ping` | stapp03 |
| Stratos Load Balancer | `ansible loadbalancer -m ping` | loadbalancer |
| Stratos Database Server | `ansible database -m ping` | storage |
| Stratos Backup Server | `ansible backup -m ping` | backup |
| Stratos Mail Server | `ansible mail -m ping` | mail |

---

## 🧩 Example Playbook

Let's say the Linux task is to:

> “Install httpd and git on the hostname *webservers* (all 3 Stratos App servers) and ensure Apache listens on port 81.”

### 🧱 Imperative (Manual) Way
```bash
ssh tony@stapp01 steve@stapp02 banner@stapp03
sudo -s; yum install git -y; yum install httpd -y
sudo sed -i 's/^Listen 80/Listen 81/' /etc/httpd/conf/httpd.conf
systemctl start httpd

```
Declarative (Ansible) Way:
```
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
Run the Playbook:
ansible-playbook httpd.yaml


“Yes, ChatGPT wrote that YAML… before i tested it 😅  🧙‍♂️ 📜”



---

