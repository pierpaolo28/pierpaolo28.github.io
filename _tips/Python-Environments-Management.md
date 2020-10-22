---
layout: post
date: 2020-06-02
---

# Python Environments Management

In order to create a virtual environment in Python we need first of all to install the Python Virtualenv library.

```
pip install virtualenv
```

At this point we can create our environment using either `virtualenv .env` or `python -m venv .env` (where .env is our chosen local environment name).

Now we can anytime activate from Windows terminal the virtual environment using:

```
.env\Scripts\activate.bat
```

From now on we can then install all the libraries we need using `pip install {package name}`.

Once finished, we can then create a requirements.txt file containing all the libraries installed in our environment using:

```
pip freeze > requirements.txt
```

In this way, different collaborators/users can easily reproduce your same working environment by using the following command from their machine.

```
pip install -r requirements.txt
```

Once finished working with our environment, we can then simply deactivate it by typing `deactivate` in our command window.
