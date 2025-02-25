---
jupyter:
  jupytext:
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.16.7
  kernelspec:
    display_name: teaching
    language: python
    name: python3
marp: true
author: Florian Schunck
title: Version control with git and collaborative software development
paginate: true
theme: uncover
footer: Florian Schunck, 2025-02-17
---

# Version control with git and collaborative software development

Florian Schunck

---
### Why do we want to do version control and collaborative software development?

* We can easily distribute code, and revise it, discuss changes, go back in time ⏱ 
* The power of many! Many people can build much better and more stable software than a single person
* **Free backups** 😎 No more loss of code (and manuscripts)
* **Versioning** of software

---
#### Basically the moment you are writing software that you would like to use more than once, you should start thinking about version control


![git_init.png](figures/git_init.png)

---
### How does git (version control) work?
<style scoped>
section {
  font-size: 24pt;
}
</style>
Transferring files between local and remote places, keeping **copies** of files and updating them incrementally, to have a history of file changes

<img src="figures/git_workfow.png" width="400">

---
### How does git (version control) work?

<style scoped>
section {
  font-size: 24pt;
}
</style>

+ `git` (https://git-scm.com) is by far the most common tool to do version control. It is usually, but not necessarily, coupled with remote repositories that act as a remote mirror of the local repository such as https://gitlab.uni-onsabrueck.de
+ `git` is a command line tool, this means it is used with the terminal (linux, mac), cmd or powershell (Windows). Whenever you need to understand how git works, it is **help**ful to consult `git --help`

---
### Practice 🛠️


Go to: https://github.com/flo-schu/collaborative-software-development and follow the README


---
<style scoped>
section {
  font-size: 16pt;
}
</style>

### 1. Install `git`

+ Windows: https://git-scm.com/downloads (and just keep all the default settings). This will also install SSH
+ Linux (debian): `sudo apt install git`
+ Mac: Install homebrew (see https://brew.sh/) and then install git with `brew install git`.

### 2. Become familiar with the tool

+ Open a commandline interface and type `git --help` to see if everything works. Then look at `git clone --help` to understand what happens when you clone a repository

### 3. Clone `mempyguts`

+ Visit https://github.com/flo-schu/collaborative-software-development and read the installation instructions

```bash 
git clone https://github.com/flo-schu/collaborative-software-development.git
cd collaborative-software-development
```
---

### Generate an SSH keypair with openssh and upload to your github account

`git` can be used via unsecured connections, but many applications require the use of encrypted, secure connections. SSH (*s*ecure *sh*ell) operates by exchanging a public and private key between yourself and the service that you want to connect to.

+ Linux: `sudo apt update && sudo apt upgrade` to update the package repositories, then `sudo apt install openssh-server openssh-client` to install ssh
+ Windows: SSH should be preinstalled on windows. You can verify it by typing `ssh` into the git bash


### Bonus 2:
