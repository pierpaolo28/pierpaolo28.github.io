---
layout: post
permalink: blog/blog17/
categories: [Extra]
---

![](https://cdn-images-1.medium.com/max/2560/1*FeSc_WWKBHW1JJ9WlC94JQ.jpeg)
<span class="figcaption_hack">(Source: <https://fsmedia.imgix.net/7b/5e/73/1d/0b6f/4146/9e58/67b0faf61bf5/ready-player-one-tech-might-already-be-here.jpeg?rect=0%2C0%2C2632%2C1314&auto=format%2Ccompress&dpr=2&w=650>) </span>

<!--end_excerpt-->

# Getting Started with Augmented and Virtual Reality

## An introduction to the different types of Augmented and Virtual Reality with practical examples.

### Augmented Reality (AR)

> Augmented Reality is a technology that takes the world around you and adds virtual content on top such that it looks like it's actually there in the real world.

> --- Zappar [1]

The main idea behind Augmented Reality (AR) is to superimpose virtual objects and information over a real-world environment in real-time so that to make the user experience more immersive [2]. 

Some commonly employed applications examples of Augmented Reality are: 

-   [Training medical students](https://www.youtube.com/watch?v=h4M6BTYRlKQ)
-   [Military training](https://jasoren.com/augmented-reality-military/)
-   [Gaming](https://www.ericsson.com/en/trends-and-insights/consumerlab/consumer-insights/reports/ready-steady-game)
-   [Museums/Art Galeries Tours](https://www.museumnext.com/article/how-museums-are-using-augmented-reality/)

![](https://cdn-images-1.medium.com/max/1200/1*t7VCdVxPgAdLOMgRd71X3Q.jpeg)<br>
<span class="figcaption_hack"> Figure 1: Augmented Reality in action [3] </span>

Use of Augmented Reality is projected to increase in the next few years and companies such as Google and Apple already developed tools such as [ARCore](https://developers.google.com/ar/distribute/) and [ARKit](https://developer.apple.com/augmented-reality/) to make easier for developers to create AR apps respectively on for the Play Store and App Store.

Artificial Intelligence is nowadays being commonly integrated into both AR and VR applications in order to optimize the customer experience (eg. Computer Vision).

There are different types of Augmented Reality applications, these are [4]:

1.  **Marker Based Augmented Reality** = makes use of a camera and a virtual marker (eg. QR Code), to activate some AR components just when the marker is identified by the camera.
2.  **Markerless Augmented Reality** = Uses GPS, accelerometers and digital compasses embedded in a device (eg. smartphone) to offer AR content based on the user location. This can be used for example to make mapping systems more interactive.
3.  **Projection Based Augmented Reality** = light is sent on a real-world object to create a user interface on which the user can interact with (the user interaction with the surface is detected by examining how the projected area is altered by this interaction).
4.  **Superposition Based Augmented Reality** = this type of AR uses object recognition to either partially or completely change the view of an object. For instance, Ikea ideated an app to make users place virtual Ikea furniture in their houses to help them decide which piece of furniture to buy.

Augmented reality can be used in many different contexts and applications. For example, this summer I decided to create a personal AR Business Card since this is going to be my last year of studies at the University of Southampton. 

<div>
  <iframe align="middle" width="650" height="500" src="https://www.youtube.com/embed/-vswyZpXOtE?rel=0"
          frameborder="0" allowfullscreen>
  </iframe>
</div>

This AR application was created using [AR.js](https://github.com/jeromeetienne/AR.js), a Javascript library made by Jerome Etienne.

If you are interested in developing your own AR application, this is possible to do also using [Unity Vuforia](https://www.youtube.com/watch?v=MtiUx_szKbI&list=WL&index=93&t=0s) or A-Frame (as shown in a practical example at the end of this article).

### Virtual Reality (VR)

At times, the terms Augmented Reality (AR) and Virtual Reality (VR) gets mistakenly confused. The main difference between the two is that VR creates a completely artificial environment in which the user gets fully immersed while AR aims to enhance our real-world environment using artificial effects.

In order to experience VR, it is typically made use of equipment such as Head Mounted Displays (HMDs) and input devices.

-   **Head-Mounted Display** = a device which contains a display mounted in front of the user's eyes (in some cases also a smartphone can be used).
-   **Input devices** = Data Gloves, Trackpads, Joysticks.

![](https://cdn-images-1.medium.com/max/1200/1*6Tje54sTMBRucEez6WmL8w.jpeg)<br>
<span class="figcaption_hack"> Figure 2: Virtual Reality Accessories [5] </span>

There are three main types of Virtual Reality [6]:

-   **Non-immersive simulations** = only some of the user sensors are stimulated (the user is still aware of the reality outside the virtual simulation).
-   **Semi-immersive simulations** = the user is partly but not fully immersed in the virtual environment (eg. flight simulation).
-   **Fully immersive simulations** = use of accessories such as Head Mounted Displays and input devices stimulate all the senses of the user.

### Demonstration

I will now walk you through a practical introduction on how to create a simple AR application using A-Frame. All the code I used for this example is available on my [GitHub](https://github.com/pierpaolo28/Artificial-Intelligence-Projects/blob/master/Virtual%20Reality%20%28VR%29/VR.html) and [CodePen](https://codepen.io/pierpaolo28/pen/pMeJKQ) accounts for you to play with.

A-Frame is a web framework based on HTML used for creating VR applications. It supports a wide variety of VR Headsets such as GerVR, CardBoard, Oculus Go and can also be used for AR applications.

A-Frame documentation offers a wide variety of examples to get you started, some are available [here](https://aframe.io/examples/showcase/helloworld/).

In order to get started with A-Frame, we can use [CopePen](https://codepen.io/mozillavr/pen/BjygdO) as online editor (or any other web development editor) so that to test in real-time our code. 

First of all, we need to load the A-Frame library in our HTML script.

    <script src="https://aframe.io/releases/0.9.0/aframe.min.js"> </script>

In this example, I will create an interactive picture which we can rotate 360° in a virtual environment.

To do so, I divided the code below in 5 main sections:

1.  Loading all the libraries/dependencies necessary for this example.
2.  Loading the image to be used and preprocess it to fit the virtual environment.
3.  Adding animations to the image.
4.  Adding a text banner to welcome the user to the application.
5.  Enabling Camera and Mouse Cursor interactions to add interactivity with the virtual environment.

<script src="https://gist.github.com/pierpaolo28/2fcbab0f7d6f058811c1d76476fd93b5.js"></script>

As a result, the following animation has been created:

<div>
  <iframe align="middle" width="650" height="500" src="https://www.youtube.com/embed/DFpKcR7n6VA?rel=0"
          frameborder="0" allowfullscreen>
  </iframe>
</div>

If you are interested to test yourself this application, just open [this CodePen link](https://codepen.io/pierpaolo28/pen/pMeJKQ) while browsing on your smartphone!

### Bibliography

[1] Augmented Reality, Zappar. Accessed at: <https://www.zappar.com/augmented-reality/>

[2] How Augmented Reality Works, HowStuffWorks, KEVIN BONSOR & NATHAN CHANDLER. Accessed at: <https://computer.howstuffworks.com/augmented-reality.htm>

[3] 3 WAYS AUGMENTED REALITY CAN DRIVE VALUE FOR AUTO BRANDS, blippar. Accessed at: <https://www.blippar.com/blog/2018/10/24/3-ways-augmented-reality-can-drive-value-for-auto-brands>

[4] Reality Technologies, The Ultimate Guide to Understanding\
Augmented Reality (AR) Technology. Accessed at: <https://www.realitytechnologies.com/augmented-reality/>

[5] Oculus Rift S Hands-On Impressions. GameInformer --- BEN REEVES. Accessed at: <https://www.gameinformer.com/gdc-2019/2019/03/20/oculus-rift-s-hands-on-impressions>

[6] Reality Technologies, The Ultimate Guide to Understanding\
Virtual Reality (VR) Technology. Accessed at: <https://www.realitytechnologies.com/virtual-reality/>
