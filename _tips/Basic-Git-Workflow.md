---
layout: post
date: 2016-06-02
---

# Basic Git Workflow

1) Get repository from remote:

```
git clone {link}
```

2) Create local branch:

```
git checkout -b {branch name}
```

3) Add branch to remote repository:

```
git push origin {branch name}
```

4) Add files to local branch:

```
git add .
```

5) Save locally the added files:

```
git commit -m {"commit description"}
```

6) Send updates to remote repository:

```
git push origin {branch name}
```

From there onward to keep adding updates from local branch to master:

```
git checkout -b {branch name}
git add .
git commit -m {"commit description"}
git push origin {branch name}
```

To add branch updates from local branch to master, do `git checkout master` and then `git merge {branch name}`.

To get updates from remote to your branch, use `git pull origin {branch name}`. If the local repository is not updated with all the branches created on remote need first to use `git fetch origin`.
