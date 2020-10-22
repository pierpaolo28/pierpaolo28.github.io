---
layout: post
date: 2020-10-04
---

# Docker Commands

## Introduction

Docker is a program which can be used to run applications in isolated environments (it takes the concept of virtual machines a step further). In this way an application created by different developers can always run in a same environment, avoiding the risk that an application might run on some machine but not another. When using Docker, applications runs in containers:

> Containers are an abstraction at the app layer that packages code and dependencies together. Multiple containers can run on the same machine and share the OS kernel with other containers, each running as isolated processes in user space.
-- [Amigoscode](https://www.youtube.com/watch?v=bhBSlnQcq2k&list=WL&index=1&t=37s)

![Figure 1: Containers Infrastructure](https://cdn-images-1.medium.com/max/2000/1*6n2pJopaiJjMXavVMFh1PQ.png)<br>
Figure 1: Containers Infrastructure

Using containers is therefore more efficient than virtual machines, which can instead be defined as:

> Virtual machines (VMs) are an abstraction of physical hardware turning one server into many servers. The hypervisor allows multiple VMs to run on a single machine. Each VM includes a full copy of an operating system, the application, necessary binaries and libraries - taking up tens of GBs. VMs can also be slow to boot.
-- [Amigoscode](https://www.youtube.com/watch?v=bhBSlnQcq2k&list=WL&index=1&t=37s)

![Figure 2: Virtual Machines Infrastructure](https://cdn-images-1.medium.com/max/2000/1*I4RJKhETwat916KcyzwAfw.png)<br>
Figure 2: Virtual Machines Infrastructure

Summarising, some of the benefits of using containers is that:
- Containers can run in seconds instead of minutes.
- They need less resources and memory to run (no full OS required).
- We can test our application locally to then deploy it just once sure that is able to run smoothly.

### Images vs Containers

In Docker, containers are running instances of images. An Image is a base template which is then used to build your application on (e.g. Ubuntu). Once fetched a base image (e.g. from Docker Hub), we can then update it by adding our application (therefore creating different versions of an Image enabling version control in case of bugs). Our Image will then have everything we need to run our App (e.g. OS, Software, Code).

### Exposing a container

When we run Docker on our computer (host), we can then access a container running an App by mapping the TCP Port the container exposes to (default Port=80) with a localhost address (e.g. localhost:8080).

### Volumes

Volumes allows us to share data (e.g, files and folders) between our computer (host) and containers or between containers themselves.

### Dockerfiles
Dockerfiles can allow us to create our own images (which are then used to run containers) instead of just making use of pre-made Images available on Docker Hub. This is done by creating a Dockerfile, in this file are then listed the steps to set up our Image (we can either create an image from scratch or building on top of an image available on Docker Hub).
One example workflow why we might want to create a Dockerfile to generate an image is:
1. We get a base image from Docker Hub (e.g. Ubuntu, nginx).
2. We run it as a container and add a volume (e.g. local files or from another container) to it which we then use to develop locally our application.
3. Once we finish creating our application and make sure it runs smoothly locally, we can then create a Dockerfile to package everything in a single new image which we can freely distribute to colleagues and users (e.g. publish on Docker Hub).

A Dockerfile should be created in the root of the project we are currently working on. An example Dockerfile is available below:
```
FROM <image-name>:<tag-name>
ADD <Files From this path> <To this path>
```

Defying a Dokerfile efficiently can then allow for good use of how the different layers of the image are constructed and take advantage of caching (speeding up execution).

### .Dockerfileignore
If we have some files/folders which we want to keep in our working directory but that are not necessary to have when creating a new Image using a Dockerfile (e.g. .git, node_modules, etc..), we can then ignore them listing them in a **.dockerignore** file.

### Alpine
If we have memory constrains, it is possible for many Images on Docker Hub to make use of an Alphine version (tag) instead of for example the Latest version. Alphine is a Linux distribution designed to be memory efficient, therefore reducing the overall size of the constructed images (e.g. nginx:alpine).

### Tags, Versioning and Tagging
Tags and Versioning allow us to get control of the image version (therefore avoiding versioning and dependencies problems). This can be done by specifying which version of an image we want to get from Docker Hub instead of just using the latest tag (which downloads the latest version available). Once modified a container image locally, we can then change its tag value to reflect which one has been created first.

### Docker Registries
Docker Registries are a type of server side applications which can be used in order to store and distribute Docker Images to other users. This can be done through either public or private repositories. Docker Registries are commonly used in CD/CI pipelines. Docker Hub is currently the most used Docker Registry.

## Commands

- Get an image from Docker Hub:
```
docker pull <image-name>
```
- See list of images available locally:
```
docker images
```
- Run container from Image:
```
docker run <image-name>:<tag-name>
# or optionally assign also a name to the container
docker run --name <preferred container name> <image-name>:<tag-name>
# Run container in detach mode
docker run -d <image-name>:<tag-name>
# Mapping Localhost to container TCP port
docker run -p <4-digit local host number>:<2-digit TPC port> <image-name>:<tag-name>
# Adding local files/folders to container
docker run -v <full path local computer folder>:<container path where we to add files> <image-name>:<tag-name>
# Adding files from a container to another container
docker run --volumes-from <container names containing files> <image-name>:<tag-name>
# Information such as the tag-name, 2-digit TPC port, etc..
# can be found by listing all containers
```
- List all running containers:
```
docker container ls
# alternatively
docker ps
```
- Stop Container:
```
docker stop <container ID>
# alternatively
docker stop <names>
```
- Start Container (once a container has been run from an image and stopped we can restart it):
```
docker start <container ID>
# alternatively
docker start <names>
```
- List all containers:
```
docker ps -a
```
- Delete containers:
```
docker rm <container ID>
# alternatively
docker rm <names>
# To delete all containers at the same time:
docker rm $(docker ps -aq)
# In order to delete images, use rmi instead
```
- Modify files inside of a container in shell (if a host volume is connected, changes will also reflect on the host files):
```
docker exec -it <names> <cmd command of container distribution>
# or alternatively
docker exec -it <container ID> <cmd command of container distribution>
# In order to come back from the container terminal to the host terminal type exit
# The CMD command of the used container distribution can be found by using
# the docker inspect command and look at the CMD path specified.
```
- Build Image from Dockerfile:
```
# Make sure to be in the same directory the Dockerfile is stored in then:
docker build --tag <preferred name>:<chosen tag version> .
# After built an image it can then be run like any other image using the run command
```
- Updating the tag of an image after creation:
```
docker tag <image-name>:<tag-name> <image-name>:<new-tag-name>
```
- Publishing Docker Image on Docker Hub:
```
# First make sure to be signed-in your Docker Hub account (docker login)
# Then you need to go on Docker Hub on a browser and create a repository
# Finally to upload your container run:
docker push <user-name>/<repository-name>:<preferred-tag-name>
```
- Inspecting a Docker container:
```
docker inspect <container ID>
# or alternatively
docker inspect <names>
```
- Read a Docker container logs:
```
docker logs <container ID>
# or alternatively
docker logs <names>
```

## Useful Links
- [Docker Hub](https://hub.docker.com/)
- [Dockerfile Reference](https://docs.docker.com/engine/reference/builder/)
