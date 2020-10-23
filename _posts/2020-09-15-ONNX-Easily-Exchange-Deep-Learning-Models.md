---
layout: post
permalink: blog/blog47/
categories: [Deep Learning]
---

![Photo by [noodle kimm](https://unsplash.com/@noodlekim?utm_source=medium&utm_medium=referral) on [Unsplash](https://unsplash.com?utm_source=medium&utm_medium=referral)](https://cdn-images-1.medium.com/max/7300/0*inljZli6_6SNIVKX)Photo by [noodle kimm](https://unsplash.com/@noodlekim?utm_source=medium&utm_medium=referral) on [Unsplash](https://unsplash.com?utm_source=medium&utm_medium=referral)

<!--end_excerpt-->

# ONNX: Easily Exchange Deep Learning Models

## A practical walkthrough on ONNX (Open Neural Network Exchange Format) and its potential applications

### Introduction

[ONNX (Open Neural Network Exchange Format)](https://onnx.ai/) is a format designed to represent any type of Machine Learning and Deep Learning model.

Some example of supported frameworks are: PyTorch, TensorFlow, Keras, SAS, Matlab, and many more. In this way, ONNX can make easier to convert models from one framework to another. Additionally, using ONNX.js we can then easily deploy online any model which has been saved in an ONNX format.

In Figure 1, is available a simple example of a Variational Autoencoder PyTorch model deployed online using ONNX.js in order to make inference on demand. A complete working example of this deployed model is available at [this link on my personal website](https://pierpaolo28.github.io/Projects/ONNX/home.html).

![Figure 1: Online VAE using ONNX.js](https://cdn-images-1.medium.com/max/2168/1*w7zv_HHG8lS5r2-U7wlzAQ.gif)Figure 1: Online VAE using ONNX.js

The main goal of ONNX is to bring together all the different AI frameworks and make as easy as possible to make them communicate with each other in order to build better models which can be supported on any type of platform or hardware.

### Converting a model to ONNX

Converting a model in the ONNX format a relatively easy. All we have to do is, make sure our trained model is in evaluation mode and create a simple dummy input of the same shape our model would expect.

A simple example in PyTorch is available below. In this simple example, we instantiate a Variational Autoencoder model, load its pre-trained weights, put it in evaluation mode and create an example input. Using these parameters, we can then create our ONNX file.

    import torch

    pre_trained = VAE(encoder, decoder)
    pre_trained.load_state_dict(torch.load('trained.pt'))
    pre_trained.eval()

    ex_input = torch.zeros(1, 28, 28)

    torch.onnx.export(pre_trained, ex_input, "onnx_model.onnx")

Our ONNX file will then be constituted by a graph representation of our model which can be used in order to convert our model to other types of frameworks (by recreating the instructions in the graph) or to use our trained model to make inference online. One current limitation of ONNX is that not all operations (eg. custom loss functions, specific neural network layers, etc…) are supported for all frameworks. A list of all the supported operators for PyTorch is available at [this link.](https://pytorch.org/docs/stable/onnx.html)

During the development of the ONNX library, different operation sets versions (**opset_version)** have been developed. Therefore, by specifying our favourite **opset_version** as argument of the export function we can decide which set of operations we want to have available by default.

### Deploying a model using ONNX.js

Some of the benefits of having a model online are:

* We reduce latency because the data doesn’t have to be sent back and forth from the server.

* Not sending data to a server also increase privacy since user data is not accessed remotely.

* Websites can be set up with just static files, making scalability, not an issue.

There are different techniques which can be used in order to deploy models online such as Tensorflow.js and ONNX.js. One of the main advantages of using Tensorflow.js is that it makes possible to train models online (using ONNX.js this is instead not an available option). On the other hand, ONNX.js is more efficient and therefore faster than Tensorflow.js in order to do inference online.

A simple template which can be used to get started with ONNX.js, is shown below. In this case, is assumed the existence of a function called **getInputs()** able to automatically create input data for our model.

    <html>
      <head> </head>
      <body>
        <!-- Loading ONNX.js library -->
        <script src="https://cdn.jsdelivr.net/npm/onnxjs/dist/onnx.min.js">
        </script>
        <script>
          // Creating a session
          const sess = new onnx.InferenceSession();
          // Loading the created ONNX file
          sess.loadModel("onnx_model.onnx").then(() => {
          // Getting an imput for our model from an example function
          const input_data = getInputs();
          // Feeding the input to our model and fetching the output
          sess.run(input_data).then((output) => {
          // Storing and displaying the output prediction
          const outputTensor = output.values().next().value;
          console.log(`Model prediction: ${outputTensor.data}.`);
            });
          });
        </script>
      </body>
    </html>

Starting from this example template, using standard Javascript functionalities, complex applications can then be developed.

If you are looking for a full example of creating a model, converting it to ONNX and then deploying it online is available in [this my Github repository. ](https://github.com/pierpaolo28/Artificial-Intelligence-Projects/tree/master/Online%20Learning/ONNX)Additionally, a collection of example models deployed using ONNX.js is available on the official ONNX.js website at [this link.](https://microsoft.github.io/onnxjs-demo/#/)
