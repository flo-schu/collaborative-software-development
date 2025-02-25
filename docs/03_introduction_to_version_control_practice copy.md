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

## **Version control** with `git`+`ssh` and **collaborative software development** with `conda`

Florian Schunck


---
### Practice 🛠️

Go to: https://github.com/flo-schu/collaborative-software-development and follow the README


---
### Explore the local repository

+ `pyproject.toml`: Defines the package, dependencies and makes it installable
+ `.gitignore`: Tells git which files to exclude
+ `main.py`: Here the entry point for the script
+ `csd/`: The package


---
### Explore the remote repository

+ issues
+ branches
+ tags
+ commits


--- 
### Handling an issue

<style scoped>
section {
  font-size: 24pt;
}
</style>

There is an open issue on github: https://github.com/flo-schu/collaborative-software-development/issues/1

By working through the steps in the issue, we will learn the basic concepts of

+ pull/push operations
+ branches
+ *testing*
+ commits
+ merge (pull request, PR)