---
title: GCP Streamlit App Deployment
layout: post
date: 2023-02-11
---

# GCP Streamlit App Deployment

## Dockerizing your Streamlit application

Once created an application with Streamlit it can be made available through Docker by creating a Dockerfile following the guidelines as in the template below:

```
FROM python:3.7
EXPOSE 8501
WORKDIR /app
COPY requirements.txt ./requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
CMD streamlit run src/main.py
```

In this example, the application is going to be exposed on port 8501. Additional info about Docker and the different commands can be found on [this page.](https://pierpaolo28.github.io/blog/tips/Docker-Commands/)

## Setting up GCP 

At this point we can then import the project in our GCP cloud sheel using git or any other forms of upload:

```
git clone -b gcp-2022 https://github.com/pierpaolo28/Epidemics-Modelling.git
cd Epidemics-Modelling
```

Finally we can initialize the gcloud and build & push our project in the GCP Container Registry:

```
gcloud init
export PROJECT=$(gcloud config get-value project)
docker build -t eu.gcr.io/$PROJECT/app_name:v1 .
docker push eu.gcr.io/$PROJECT/app_name:v1
```

In order to run the docker push command we additionally need to make sure to have enabled the GCP Container Regestry API (which can be found at [this link](https://console.developers.google.com/apis/api/containerregistry.googleapis.com)).

## Setting Up Cloud Run

Cloud Run is the main serverless cloud service available on GCP to deploy pre-build applications. Now that our application is available in the GCP Container registry we can just go through the following steps in order to lunch it:

1. Search Cloud Run between the different applications available on GCP.
2. Click on Create Service.
3. Add the Container Image URL we just created.
4. Specifiy the name for your application and its location.
5. Specify the amount of resources to provide for running the application (e.g. 1GB of Memory, 2VCPUs).
6. Once created the service and waited for the deployment to finish, the url of the application should then become available.
7. If we want to apply any change in the code once the application is running, can then just build & push again the updated project in the container registry, click to edit the existing service configuration and select the new container image URL.

Finally, if preferred, it can also be possible to deploy your Streamlit application also on other services such as Compute Engine and App Engine (which can provide more granular control on access, etc...).
