---
layout: post
date: 2020-06-09
---

# EC2 Amazon Web Services Set Up

## Creating an EC2 instance

1. Log in into AWS and on the dashboard menu select create instance (Amazon Linux AMI 2018.03.0 and t2.micro as specifics).
2. As part of the process to create the instance, go to the **Configure Security Group** tab and add a new custom TCP rule for the 8501 port range with Anywhere as source (this is the port the app is going to use). In case, we want to create multiple apps then create other additional custom TCP rules.
3. Finally, create a key-pair and save it as **.pem** file.
4. Now we can download Putty for Windows and use it to connect to our instance from our local machine.
5. In order to use Putty, we first need to convert our **.pem** file into a **.ppk** file. This can be easily done using Puttygen.
6. Now we can open Putty and put in the host name field the address of our instance (available on AWS console-> Public DNS field). In front of this address, we need additionally to add **ec2-user@**.
7. Finally we just need to add our **.ppk** file to SSH Category -> Auth, save the session with a name and lounch it.
8. At this point, a terminal for our Linux instance will open.

## Set up environment and maintain Streamlit app

We are now ready to install our Anaconda environment and required dependencies for our application. This can be easily done like in any other Linux environment. More information is available in the [Windows-Linux Subsystem](https://ppiconsulting.dev/blog/tips/Windows-Linux-Subsystem/) and [Anaconda Management](https://ppiconsulting.dev/blog/tips/Anaconda-Management/) guides. Additionally, if working both on the AWS EC2 (Elastic Compute Cloud) instance and a local machine, might be useful to set-up Github on both ends and use the [Basic Github Workflow](https://ppiconsulting.dev/blog/tips/Basic-Git-Workflow/) in order to easily move the updates from one machine to the other.

In order to keep our app running even if we close the SSH terminal connection, we need to set-up a TMUX session. TMUX can be easily installed using:

```
sudo apt-get install tmux
```

We can now start a new session:

```
tmux new -s example_session
```

At this point, we just need to run our Streamlit app and press **CTRL+B and right after D**. Once done than, we can close our terminal and the App instance will still be running on the provided external URL.

If finally we want at a later date to shut down our App, we can just run the following command:

```
tmux a -t example_session
```

Tmux useful commands:

```
# List active tmux sessions
tmux ls

# Attach to an open session to make updates
tmux attach -t stream
```


Additional information about tmux is available at [this link.](https://danielmiessler.com/study/tmux/#:~:text=Show%20existing%20sessions,shortcut%20ctrl%E2%80%93b%E2%80%93s.)

To automatically restart a Streamlit app if something fails, the following command can be used in the command line:
```
while true; do streamlit run src/main.py; done
```

## Additional References

[1] [Deploying Streamlit app to EC2 instance](https://medium.com/@pokepim/deploying-streamlit-app-to-ec2-instance-7a7edeffbb54)

[2] [How to Deploy a Streamlit App using an Amazon Free ec2 instance?](https://towardsdatascience.com/how-to-deploy-a-streamlit-app-using-an-amazon-free-ec2-instance-416a41f69dc3)
