---
layout: post
date: 2020-06-09
---

# Anaconda Management

### Create environment with specific Python version

```
conda create --name {environment name} python={python version}
```
### List Environments

```
conda env list
```

### List Packages installed in an environment

```
conda list
```

### Copy all Packages from one environment to create a new environment

```
conda create --clone {name of env to copy} --name {name of env to create}
```

### Delete environment

```
conda env remove --name {name of env to delete}
```

### Update Anaconda

```
conda update conda
```

### Check conflicts between Packages

```
pip install pip-conflict-checker
pipconflictchecker
```

### Extras
Some additional features which can be added to Jupyter Lab and Jupyter Notebook in Anaconda are the addition of extensions and Kernels for coding in other programming languages apart from Python (eg. R, Julia, Scala).

- [Jupyter Lab Extensions Documentation](https://jupyterlab.readthedocs.io/en/stable/user/extensions.html)
- [Top Jupyter Lab Extensions](https://github.com/mauhai/awesome-jupyterlab)
- [Jupyter Kernels List](https://github.com/jupyter/jupyter/wiki/Jupyter-kernels)
