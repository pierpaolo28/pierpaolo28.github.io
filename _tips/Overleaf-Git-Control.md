---
layout: post
date: 2020-06-02
---

# Overleaf Git Control

First of all we need to make a folder which will contain our Overleaf project on our machine.
Once created and `cd` in it we can initialise our repository using `git init`.

At this point we can go to our Overleaf project online and get the clone link from the project settings. Now we can add our remote Overleaf project to our local folder:

```
git add remote overleaf {clone link}
```

We can now add also our remote Github repository so that to save project updates on it.

```
git add remote github {repository clone link}
```

In case we are interested in storing our Overleaf data on Github not on the repository master branch, we can then use `git fetch github` in order to get all the repository branches.

Now we are ready to get the data from Overleaf and store it locally:

```
git pull overleaf master
```

Finally, we can send the data to our desired Github branch using:

```
git push github master:{your preferred github branch name}
```

These last two steps can then be repeated iteratively everytime after having worked on Overleaf in order to update Github.

In case we make changes to our Overleaf project locally, we can then update both Github and Overleaf, using the following commands:

```
git add .
git commit -m "Commit Description"
git push overleaf master
git push github master:{your preferred github branch name}
```
