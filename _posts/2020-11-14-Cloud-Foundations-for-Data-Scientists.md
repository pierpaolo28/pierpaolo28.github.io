---
layout: post
permalink: blog/blog51/
categories: [Data Science]
---

![Photo by [C Dustin](https://unsplash.com/@dianamia?utm_source=medium&utm_medium=referral) on [Unsplash](https://unsplash.com?utm_source=medium&utm_medium=referral)](https://cdn-images-1.medium.com/max/11424/0*F3jWwKGoi184H73t)Photo by [C Dustin](https://unsplash.com/@dianamia?utm_source=medium&utm_medium=referral) on [Unsplash](https://unsplash.com?utm_source=medium&utm_medium=referral)

<!--end_excerpt-->


# Cloud Foundations for Data Scientists

### A guide through the foundations of cloud technology and its applications in Data Science

## Introduction

Nowadays, more and more companies are moving to developing and deploying applications in cloud-based environments. One of the main motivations for cloud computing is that it gets rid of all the problematics associated with setting up and managing the used hardware and software. This is accomplished by remotely renting computer resources available in data centres maintained by a Cloud provider.

In this way, companies and individuals can make use remotely of the hardware and software setups and workflows provided by different cloud providers without having to worry about buying the equipment, set up different environments and maintain them over time. Using this type of approach, makes therefore possible for users to focus just on developing and deploying their services (eg. website, database, apps, data analytics) without having to think about any possible overhead. Ultimately, this can lead to faster/continuous development and improved customer satisfaction, in line with common DevOps (Development-Operations) principles.

The main idea behind cloud services closely resembles any other type of utility and subscription-based system which has been developed in the past. For example, in these days, each of us makes use of utilities such as electricity/water/gas without having to worry about how these systems works and are delivered to us. What we care about is that our providers can give us a reliable service and that we have to pay just for how much we use or not all of these services.

Some of the main cloud providers in use are:

* **[Microsoft Azure](https://azure.microsoft.com/en-gb/)**

* **[Amazon Web Services (AWS)](https://aws.amazon.com/)**

* **[Google Cloud Platform (GCP)](https://cloud.google.com/)**

All of these different providers, have their own terminologies for the provided services but they all share the same principles outlined in this article.

## Cloud Concepts

Each different cloud provider is able to offer a wide variety of services and applications, these can be categorised into four main types:

* **Computing:** virtual machines, containers, etc…

* **Networking:** security services to make different services interact with each other.

* **Storage:** space to store any type of file or databases for applications.

* **Analytics:** data processing and visualization tools to analyse and create insights from the stored data.

In order to make resources renting costs low and make the best use out of the available hardware, cloud services heavily rely on virtualization techniques such as Virtual Machines and Containers.

### Virtual Machines (VMs)

Virtual Machines have been created in order to emulate computers hardware (Figure 1). Different instances of virtual machines can be created to run on a single computer simultaneously, each of them having a preferred operating system, memory and storage allocation. Once created a virtual machine, this can then be accessed remotely using a desktop client and used like any other physical computer (eg. install programs, run applications, etc…). In this way, hardware usage can be maximised by using a single computer as a collection of different computers.

![Figure 1: Virtual Machines Infrastructure](https://cdn-images-1.medium.com/max/2000/1*I4RJKhETwat916KcyzwAfw.png)

Another great advantage of using VMs in the cloud is that our system can become easily scalable. Therefore, if are need more resources than planned to complete a project, extra memory and storage capability can be provided on the fly by the cloud provider (reducing so any possible downtime in the deployment).

Additionally, if we want to make sure that our service is always running, it can also be possible to create a backup VMs that will automatically run in case any problem might arise with the original one. This can be particularly useful when adding new features on services such as websites or applications and we want to first make available the newer version of the service to just a subset of the audience so that to get some sort of feedback of if the change can bring a positive impact or not to the service (A/B testing).

### Containers

One problem with Virtual Machines is that each virtual machine has its own operating system. For example, if we have a complex application which needs Windows for some operations and Linux for some others then we would need to run two separate Virtual Machines and make the two communicate with each other. This, therefore, leads to an overhead of resources which could be avoided. Additionally, when developing in a team an application it then can be also possible that some packages dependencies conflicts might arise when moving from different environments (e.g. “It worked on my machine”).

In order to avoid these types of problem, Containers have been ideated. Containers, package together apps with their dependencies and deploys them to a container host (which acts as a service to abstract away the operating system). In this way, the overhead memory cost due to having multiple operating systems can now be avoided and more Containers can be able to run on a single machine than what it would have been possible to do on a single machine using Virtual Machines. Additionally, now our applications can now easily move between different operating systems without having to think about managing the underlying dependencies.
>  Virtual Machines virtualise the hardware, while Containers virtualise the operating system [1].

One of the most common services which can be used in order to create containers is [Docker](https://www.docker.com/) (Figure 2).

![Figure 2: Containers Infrastructure](https://cdn-images-1.medium.com/max/2000/1*6n2pJopaiJjMXavVMFh1PQ.png)

One of the most efficient ways to create complex systems is to divide them into different Container applications each having a distinguishable role. For example, if we are working on a website it could be a good idea to divide the website into three main containers: front-end, back-end and database. Every time we want to introduce new features, we can then update our Container of interest without having to touch the other ones. As we add more components to our application and its complexity increases more and more Containers might be needed. In order to efficiently maintain and organise Containers, services such as Kubernetes have been created.

Kubernetes, have been developed in order to make Container-based applications easily scale in Cloud-based environments. Some examples of services which Kubernetes can provide are:

* Optimising workload between Containers and scale the number of resources needed based on demand.

* In case there is any fault in a Container, a new instance can be created in order to replace it.

* If after the launch of a new feature, some problem arises it can be easily possible to go back to the previous version of our application.

Making use of Kubernetes to orchestrate our applications, can then allow us to follow DevOps practices such as **Continuous Integration (CI)** and **Continuous Delivery (CD)**. The main focus of Continuous Integration is to make sure that code changes perfectly integrates with the current code infostructure, while Continuous Delivery focuses on making the code base always ready for deployment (able to automatically pass any building and testing mechanism in place).

## Cloud Deployment and Services Types

Once created an application in the Cloud, this can then be deployed using three different cloud deployment methods:

* **Public Cloud:** in this scenario, all the used resources are managed and maintained by the cloud provider. This is currently the most cost-effective and common type of Cloud Deployment method.

* **Private Cloud:** is commonly used when working on tasks which require high security and strict legal compliance. In this case, a local cloud infostructure can be created by the business giving therefore less control to the cloud provider (this option requires the business to buy upfront their own hardware equipment).

* **Hybrid Cloud:** in this example, part of an application might be managed by our cloud provider while others by the private business (a mixture of the public and private cloud deployment methods).

Finally, there are three different types of services which are available on the cloud:

* **Infostructure as a service (IaaS):** in IaaS types of services we rent some hardware and configure it ourself in order to complete different tasks.

* **Platform as a service (PaaS):** in PaaS types of services we rent some pre-configured hardware and use it in order to either test and develop some applications or in order to store business data.

* **Software as a service (SaaS):** in SaaS the cloud provider develops and maintains some software applications which can then be distributed using a subscription model. Two examples of SaaS programs are Skype and Office 365.

Making use of this infrastructure can then be possible to easily move any type of software-based business in the cloud.

*I hope you enjoyed this article, thank you for reading!*

## Bibliography

[1] Microsoft Learn, Azure fundamentals. Accessed at: [https://docs.microsoft.com/en-gb/learn/paths/azure-fundamentals/](https://docs.microsoft.com/en-gb/learn/paths/azure-fundamentals/)
