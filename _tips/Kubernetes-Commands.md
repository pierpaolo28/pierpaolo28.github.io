---
layout: post
date: 2020-10-05
---

# Kubernetes Commands

## Introduction

Once learned how to create and manage containers, we can then create complex applications with many containers interacting each other to create a complex system. These containers would therefore have to be deployed across different servers in a distributed way. Managing such a complex system could then turn up to be quite complicated if we are not provided with any form of automation tool (e.g. if one of the containers stop working we would have to manually fix the system). In order to solve these type of problems, open-source container orchestration tools such as Kubernetes have been created.
Some advantages of using orchestration tools to manage applications are:
- High Availability (no downtime)
- Scalability (high performance)
- Disaster Recovery (backup and restore)


### Kubernetes Architecture
A Kubernetes cluster is composed by at least a master node connected to some worker nodes. Each node then has a **kubelet** process which makes possible for the different parts of the cluster to talk to each other and execute tasks. Each worker node has then different Docker containers deployed in it (different nodes might have different number of container running depending on the preferred workload distribution). Therefore, the worker nodes are where our whole application is running. Our master node runs instead all the important Kubernetes processes necessary to make the cluster function:
- **API server**: works as the entrypoint to the Kubernetes cluster (that's how we can communicate from outside to the cluster through CLI, APIs or UI).
- **Controller manager**: keeps track of the activities in the cluster (e.g. restart container if dies).
- **Scheduler**: instantiate containers on different nodes depending on workload and availability (Pods placement).
- **etcd**: key value storage, which is used in case we need to backup and recover our Kubernetes cluster.

From the point of view of the master node, all the worker nodes can be seen as a unified machine by connecting them all through a virtual network. Each worker node is typically much bigger and powerful than the master node.

### Pods, service & ingress
The smallest unit in Kubernetes is a pod. A pod can be considered to be an abstraction of a container (a layer on top of a container so to make easier to replace containers in a cluster). Usually, there is only one container running per pod. In Kubernetes, each pod comes with its own internal IP address which makes possible for different pods to communicate each other. One problem of pods in Kubernetes is that they are ephemeral (they can die quite easily if they run out of resources, or the application crash). If a pod crash, it gets then automatically replaced with a new one. The problem is that each new pod comes with a different IP address and therefore if the crashed pod is connected with other pods, that other pods needs to be informed of the change of IP address. One solution in order to solve this problem is to attach a service to each pod, this would then make the IP address of the pod permanent and not dependent on their lifespan.

Finally, if we want to make a pod (e.g. website frontend) available outside of the cluster to the open-web, we can then make use of an ingress (external) service.

### Config map and secrets
A ConfigMap can be used in order to set-up externally the configuration of our application (e.g. specify some properties of our application without having to rebuild the different containers). If some variables we want to store externally are security sensitive (e.g. username and password of a database), we can then use a Secret instead of a ConfigMap (secrets are not stored in plain text but in an encoded format).

### Volumes
Volumes are used to attach storage to a pod, in this way if a pod which holds data dies, its data can be saved in the attached volume. This can be thought as some form of external storage which makes sure to keep the data safe in case anything happens within the cluster.

### Deployment stateful set
Kubernetes allow us to replicate every service composing our application across different service, thanks to this, if any pods fails the traffic can immediately be redirected to another replica. The replicas are in fact connected to the same Service used by the pods which where "live". In this way a Service can also act as a load balancer and redirect traffic between different replicas in order to optimise the workload distribution. The replicas of the pods composing an application are creating through a **deployment** (abstraction of pods). Deployments are used for stateLESS applications, while **StatefulSets** are used for stateFUL applications and databases (in this case we need to make sure that data read/write is synchronised in order to avoid duplicate/missing data in the application). StatefulSets can be difficult to create and maintain and that's why, it is usually best to try to avoid having stateful pods in a Kubernetes cluster in the first place.

## Commands

Minikube (for start-up/deleting clusters) and Kubeclt (configuring Minikube clusters) are the two most common tools to create Kubernetes applications locally.

- Start/stop Kubernetes cluster:
```
minikube start
minikube stop
```

- Get status of Kubernetes cluster:
```
minikube status
```

- Delete Kubernetes cluster:
```
minikube delete
```

- Get cluster nodes/pods/Services/deployments/replicasets/secrets:
```
kubeclt get nodes
kubectl get pod
kubectl get services
kubectl get deployment
kubeclt get replicaset
kubeclt get secret
```

- Create/delete a deployment (and associated pods):
```
kubeclt create deployment <NAME> --image=<Image Name>
kubeclt delete deployment <NAME>
```

- Debugging pods:
```
kubeclt logs <Pod Name>
kubeclt describe pod <Pod Name>
# Access terminal of application container
kubeclt exect -it <Pod Name> -- bin/bash
```

- Create/delete a deployment through configuration (YAML) file:
```
kubeclt apply -f <YAML file name>
kubeclt delete -f <YAML file name>
# If using secrets, these also needs to be created in this way
```

- Secret (YAML) file example:
```
apiVersion: v1
kind: Secret
metadata:
    name: <chosen preferred secret name>
type: Opaque
data:
    username: # base 64 string
    password: # base 64 string
```

- ConfigMap (YAML) file example:
```
# ConfigMaps and Secrets should be put in the K8s cluster
# before referencing them in a deployment file.
apiVersion: v1
kind: ConfigMap
metadata:
    name: <chosen preferred ConfigMap name>
data:
    <chosen variables names and values (key-value pair)>
```

- Basic configuration (YAML) file example:
    ```
  apiVersion: apps/v1
  kind: Deployment
  metadata:
      name: example-deployment
      labels:
          app: image_name
  # Specification for the deployment
  spec:
      replicas: 1
      selector:
          matchLabels:
              app: image_name
      template:
          metadata:
              labels:
                  app: image_name
  # Specification for the pods
          spec:
              containers:
              - name: image_name
                image: image_name:tag
                ports:
                  - containerPort: 80
  # At this point here, can be specified environment variables
  # through a secret file (valueFrom -> sectretKeyRef) or
  # ConfigMap (valueFrom -> configMapKeyRef).

  # In YAML can be included multiple configuration files at the
  # same time if separated by a --- line
    ```

- Basic Service Configuration File (YAML):
```
apiVersion: v1
kind: Service
metadata:
    name: <chosen preferred service name>
spec:
# The selector allow us to connect to a pod through a label
    selector:
        app: image_name
    # A service can be made available externally by adding:
    # type: LoadBalancer
    # and a nodePort in the ports section
    ports:
        - protocol: TCP
          port: <service port>
          targetPort: <connecting container port>
          # nodePort: 30000
```

- Create an external IP Address for a service:
```
minikube service <Service Name>
```

## Useful Links
- [Docker and Kubernetes Tutorial Full Course](https://www.youtube.com/watch?v=bhBSlnQcq2k&list=WL&index=1&t=37s)
