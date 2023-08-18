---
layout: post
permalink: blog/blog7/
categories: [Machine Learning, Deployment]
---

![](https://cdn-images-1.medium.com/max/2000/1*lfsNq-qhWwOo-bzqwh7Igw.jpeg) <br>
<span class="figcaption_hack">(Source =
[https://image.slidesharecdn.com/slides-170512093121/95/deploying-machine-learning-models-to-production-8-638.jpg?cb=1507239367](https://image.slidesharecdn.com/slides-170512093121/95/deploying-machine-learning-models-to-production-8-638.jpg?cb=1507239367))</span>

<!--end_excerpt-->

# Flask and Heroku for online Machine Learning deployment

## Introduction

Thanks to libraries such as Pandas, scikit-learn and Matplotlib it is relatively
easy to start exploring datasets and making some first predictions using simple
Machine Learning (ML) algorithms in Python. Although, to make these trained
models useful in the real world it is necessary to share them and make them
accessible on the Web ready to make predictions. Only in this way Machine
Learning can be used to provide benefit to society.

I have recently been working with the [Blood Transfusion Service Center
dataset](https://www.openml.org/d/1464) by Prof. I-Cheng Yeh and I achieved a
prediction accuracy of 91.1% using a Random Forest Classifier. I, therefore,
decided to make this model available online on my [personal
website](https://ppiconsulting.dev/). To do so, I made use of Heroku and the
Python library Flask.

As a further development, I also decided to create an Android App for my
personal website using Android Studio making so my ML model also ready to run on
Android devices.

## Flask

![](https://cdn-images-1.medium.com/max/2000/1*0OD66Df9V6iylNEa3DgpeQ.png) <br>
<span class="figcaption_hack">(Source =
[https://kenya-tech.com/wp-content/uploads/2019/01/flask-python.png](https://kenya-tech.com/wp-content/uploads/2019/01/flask-python.png))</span>

Flask is a web framework used to create Web Apps for Python. In the case of
developing an online ML model, this can be done by using just three python
files:

1.  **model.py** = in this file the ML model should be implemented and trained. The
trained model should then be saved using the *Pickle library* in order to be
ready to be used to give real-time predictions when used on the Web.
1.  **app.py** = in this file Flask is used to handle *POST* requests we get from
request.py and then return the results. To do so, the trained ML model is
retrieved using the *Pickle library*.
1.  **request.py** = is used to request the feature to the server and retrieve the
results.

A basic example of **app.py** can be:

```python
import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)

# Code to load ML model

@app.route('/')
def home():    
        return render_template(
)

@app.route('/ml-model', methods=['POST'])
def run_model():
        # Code to use the trained model to make real time predictions
        return render_template(
)

if __name__ == '__main__':
        app.run()
```

If we want to add some HTML, CSS or any other type of content to improve the
online graphics of the model, it is possible to do so by creating a *templates*
folder in the same working directory where there are our **model.py**, **app.py** and **request.py** files and including these files there. These files have to
be included in the *templates* folder because when calling
**render_template(“filename.html”)** in **app.py**, Flask will by default look
just for files in the *templates* folder.

Using just Flask we can be able to run our model on our local machine using a
local server. If we want instead to make our model available on the Web, we can
deploy our Flask App to an online platform such as Heroku.

## Heroku
![](https://pbs.twimg.com/profile_images/689189555765784576/3wgIDj3j.png) <br>
<span class="figcaption_hack">(Source =
[https://pbs.twimg.com/profile_images/689189555765784576/3wgIDj3j.png](https://pbs.twimg.com/profile_images/689189555765784576/3wgIDj3j.png))</span>

Heroku is a cloud platform which can be used to deploy websites and other
services. In order to use Heroku, it is necessary to have: a [Heroku
account](https://signup.heroku.com/dc), the [Heroku CLI
tool](https://devcenter.heroku.com/articles/heroku-cli#download-and-install) and
git installed on your machine.

Successively, it is necessary to:

1.  Create a git repository in the directory where is our Flask App.
1.  Login into our Heroku account.
1.  Create a requirements.txt and Procfile.
1.  Add all the files in the directory to the repository.
1.  Push the app to the web!

The first three steps can be implemented by running sequentially the following
commands in the command prompt.

    git init
    heroku login
    heroku create

Creating a requirements.txt file it is necessary to inform Heroku of what
libraries are needed in order to run our Flask App. Therefore in the
requirements.txt file, we write one for each line just the names of all the
library used. For this application, the Procfile instead just need to contain
one line of text (as shown below). The Procfile is needed to let Heroku know
what type of application we desire to execute.

    web: gunicorn app:app

Steps five and six can then be executed by running sequentially the following
commands in the command line.

    git add .
    git commit -m "Committing all the directory files to Heroku"
    git push heroku master
    heroku open

Using the *heroku open* command should open the webpage where our Flask App has
been deployed. Alternatively, it is possible to find out the link where our
model is deployed by logging in online on our Heroku account. Visiting the
Heroku website can be particularly useful especially in the case any problem has
been registered during the lunch of our Flask App.

## Conclusion

This was a brief introduction on how to deploy your Machine Learning model
online. If you are looking to find out more about how to use Flask to code Web
Apps these are some useful references [1, 2, 3].

My online Machine Learning Model is available
[here](https://ppiconsulting.dev/Projects/flask.html) and all the code I used to
design it can be found on my [GitHub
page](https://github.com/pierpaolo28/Artificial-Intelligence-Projects/tree/master/ML-Deployement).

## Bibliography

[1] How to build a web application using Flask and deploy it to the cloud.
Salvador Villalon. Accessed at:
[https://www.freecodecamp.org/news/how-to-build-a-web-application-using-flask-and-deploy-it-to-the-cloud-3551c985e492/](https://www.freecodecamp.org/news/how-to-build-a-web-application-using-flask-and-deploy-it-to-the-cloud-3551c985e492/).

[2] Tutorial: Deploying a machine learning model to the web. Cambridge Spark,
Alexander Robertson. Accessed at:
[https://blog.cambridgespark.com/deploying-a-machine-learning-model-to-the-web-725688b851c7](https://blog.cambridgespark.com/deploying-a-machine-learning-model-to-the-web-725688b851c7).

[3] Deploy a machine learning model using flask. [Hemang
Vyas](https://hackernoon.com/@vyashemang?source=user_popover). Accessed at:
[https://hackernoon.com/deploy-a-machine-learning-model-using-flask-da580f84e60c](https://hackernoon.com/deploy-a-machine-learning-model-using-flask-da580f84e60c).
