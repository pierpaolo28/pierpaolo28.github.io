---
layout: post
date: 2020-06-09
---

# Windows Linux Subsystem

In order to get ready to install a Linux Subsystem on Windows it is first necessary to make sure we have activated the developer mode on the Windows settings. Finally, we need to go to **"Turn Windows Features on or off"** and make sure the **"Windows Subsystem for Linux"** option is ticked. At this point, we can now go to the Windows Store and install our preferred Linux distribution (eg. Ubuntu).

Activating the app, we will then be presented with our Linux terminal. We will first need to set up an username and password and then we are now ready to install Anaconda and Python (For the latest Anaconda versions available look [here]( https://repo.continuum.io/archive)).

```
wget https://repo.continuum.io/archive/Anaconda3-5.2.0-Linux-x86_64.sh
```
The installation script can then be run by using:

```
bash Anaconda3-5.2.0-Linux-x86_64.sh
```

To test if everything went fine we can then run the following command. **Make sure to see if Anaconda is part of the path, otherwise it would have to be added to the system path by using the export PATH Linux command**.

```
which python
```

Now we are ready to activate Anaconda.

```
source ~anaconda3/bin/activate
```

In case our Anaconda version is not the latest we can then run the folling command:

```
conda update --all
```

Now we can also add all our packages of choice and extensions.

```
pip install {example package}
```

At this point, we are ready to lunch Jupyter Lab using the following command:

```
jupyter-lab --no-browser
```

Our notebook is now active at the following link: [http://localhost:8888/lab](http://localhost:8888/lab).

We can now manage our Anaconda environment like in any other settings, more information are available in [Anaconda Management](https://ppiconsulting.dev/blog/tips/Anaconda-Management/).

We can now additionally set up Git on the Linux Subsystem.

```
sudo apt install git
git --version
git config --global credential.helper store
git config --global user.name "example"
git config --global user.email "example"
git config --global user.password "example"
git config --list --show-origin
```

In some cases, it might be additionally necessary to use an SSH key instead of HTTPS. More information is available [here](https://medium.com/faun/how-to-use-git-and-other-linux-tools-in-wsl-on-windows-4c0bffb68b35) and [here](https://peteoshea.co.uk/setup-git-in-wsl/).

More information on the Git Workflow are available at [this link](https://ppiconsulting.dev/blog/tips/Basic-Git-Workflow/).

If additionally, we are interested to use Visual Code Studio, we can just run the following command to open it:

```
code .
```

In order to make Visual Code Studio work in the Linux Subsystem we need to make sure to have it installed on our Windows machine and that we have set up the [Remote WSL extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-wsl).

If we want to move files from the Linux Subsystem to Windows (or viceversa) we can simple open our Linux Subsystem directory using the following command:

```
explorer.exe .
```

In case you can be interested in running some more graphics intensive tasks while using the Subsystem, using Xmining X server for Windows can be a great solution. More information is available at [this link.](https://dibranmulder.github.io/2019/09/06/Running-an-OpenAI-Gym-on-Windows-with-WSL/)
