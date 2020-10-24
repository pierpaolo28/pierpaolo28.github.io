---
layout: post
permalink: blog/blog35/
categories: [Extra]
---

![](https://cdn-images-1.medium.com/max/2600/1*EWmVo5PD97pIp2VcNJBWLA.jpeg)
<span class="figcaption_hack">(Source:
[https://cdn.vox-cdn.com/thumbor/7MrpKqpFquP1pqslq3nyZO9ECWs=/0x0:6144x4099/1200x800/filters:focal(2581x1559:3563x2541)/cdn.vox-cdn.com/uploads/chorus_image/image/64798397/GM_Cruise_AV.0.jpeg](https://cdn.vox-cdn.com/thumbor/7MrpKqpFquP1pqslq3nyZO9ECWs=/0x0:6144x4099/1200x800/filters:focal(2581x1559:3563x2541)/cdn.vox-cdn.com/uploads/chorus_image/image/64798397/GM_Cruise_AV.0.jpeg))</span>

<!--end_excerpt-->

# Future of Cyber Security for Connected and Autonomous Vehicles

## An introduction to the different security challenges faced by autonomous vehicles and a Machine Learning approach to tackle them.

### Introduction

Autonomous vehicles make use of sensors and complex algorithms to detect and
respond to their surroundings. Some examples of common technologies employed in
autonomous vehicles are: Computer Vision, LIDAR, GPS, etc…

Thanks to these technologies, autonomous vehicles don’t necessitate a driver to
complete even complex journeys. Additionally, multiple autonomous vehicles can
communicate with each other to improve traffic and obstacle avoidance.

The evolution in automation levels of cars is summarised in Figure 1. Many
companies such as Waymo and Tesla are now hugely investing in a future lead by
Autonomous vehicles (self-driving cars).

![](https://cdn-images-1.medium.com/max/2000/1*dGBrOiXsipUOUpvoWgtO5g.png) <br>
<span class="figcaption_hack">Figure 1: Automation Levels of Autonomous cars [1]</span>

> “DoT researchers estimate that fully autonomous vehicles, also known as
> self-driving cars, could reduce traffic fatalities by up to 94% by eliminating
these accidents that are due to human errors”

> — ZDNet, Teena Maddox [2]

### Cyber Security

A research carried out by [Charlie Miller and Chris
Volosek](http://illmatics.com/Remote%20Car%20Hacking.pdf) recently showed that a
Jeep Cherokee can be hacked just through an internet connection (making the car
stop on a highway!). Also, other types of vehicles have been demonstrated to be
sensitive to either wired or wireless attacks (eg. Toyota Prius, Ford Escape).
In these cases Hackers have been able to: activate/disable vehicles brakes,
steering wheels and increase the vehicle speed.

![](https://cdn-images-1.medium.com/max/2000/1*44LoyXan0-n3f_EI6h57-g.png) <br>
<span class="figcaption_hack">Figure 2: Cybersecurity in Autonomous Vehicles [3]</span>

Hackers can try to take advantage of self-driving cars vulnerabilities in many
possible ways [4]:

1.  **Cloud Computing**: self-driving cars produce and store new data every second
and make use of cloud computing for fast storage/retrieval (eg. identify GPS
position to predict traffic flow). If a Hacker was able to access the cloud
database of a car, it would be able to manipulate many features of a car (eg.
switch off safety devices). Additionally, because the transfer of information
must be as fast as possible, it is difficult to highly encrypt the information
sent.
1.  **Multiple Coding Languages**: nowadays cars are created by assembling many
components fabricated by different manufacturers. In order to ensure a car is
perfectly functioning, all the different parts need to perfectly communicate
with each other. If secure communication cannot be ensured, Hackers might try to
take advantage of this. Car manufacturers usually perform [penetration
testing](https://searchsecurity.techtarget.com/definition/penetration-testing)
to make sure of their vehicles' security.

There are two main risks associated with hacking self-driving cars:

1.  The Hacker might be able to take control of the car remotely.
1.  The Hacker might be able to access the users' personal information.

Countries like the USA and UK already enforced legislation in order to ensure
car manufacturers maintains a minimum required cybersecurity standard.

Ensuring high security in autonomous vehicles can also increase trust in the
public to invest in this new technology.

If you are interested in finding out more about cybersecurity in autonomous
vehicles, [this research
paper](https://www.sciencedirect.com/science/article/pii/S096585641830555X) is a
great place where to start.

### Machine Learning

As mentioned before, vehicles always produce and store large amounts of data, it
then comes to us to decide how to make the most out of this data.

Machine Learning can potentially be used to identify and prevent unusual
behaviour (eg. make the car go in parking mode while driving at high speed on a
highway) [5]. In this way, Hacker attacks could be stopped from happening.

Researchers are still now taking place in order to increase prediction accuracy.
In fact, in order to create models able to distinguish between usual and unusual
driving behaviours, many factors relating the car and it’s surroundings have to
be taken into account.

Additionally, it could be possible to add a feature to make the driver allow for
“unusual” behaviours if considered as necessary depending on his judgment.

![](https://cdn-images-1.medium.com/max/2000/1*-N1Q137jGK8lKgPaeUgOFg.png) <br>
<span class="figcaption_hack">Figure 3: Machine Learning in self-driving cars [6]</span>

### Legal Implications

As Autonomous Vehicles are now becoming more popular, institutions are now
getting concerned if it is necessary to create new laws to regulate their use.

For example, in [2018 in Arizona (USA) the first case of an autonomous car
killing a pedestrian has been
registered](https://www.theatlantic.com/technology/archive/2018/03/can-you-sue-a-robocar/556007/).
According to the police report, the pedestrian might have been at fault. In this
case, who should be considered to be at fault?

* Is it the driver in the car? (who didn’t have control of the vehicle at the
moment of the accident).
* Is it the software developer? (who created the software designed to handle these
type of situations).
* Is it the car manufacturer? (who didn’t take enough precautions when designing
and supplying the vehicle).
* Who should be in charge of the car insurance? (since the driver does not take
control of the vehicle in most of the situations).
* In case of inevitable collision, should the car prioritize its own safety or the
one of the other vehicle/pedestrians involved?

Most of these questions are still without an answer and different approaches
might be taken to solve them (depending on the regulatory country and cultural
relativism).

### Bibliography

[1] This is what the evolution of self-driving cars looks like. Business
Insider. Accessed at:
[https://www.businessinsider.com/what-are-the-different-levels-of-driverless-cars-2016-10?r=US&IR=T](https://www.businessinsider.com/what-are-the-different-levels-of-driverless-cars-2016-10?r=US&IR=T)

[2] How autonomous vehicles could save over 350K lives in the US and millions
worldwide. ZDNet, Teena Maddox. Accessed at:
[https://www.zdnet.com/article/how-autonomous-vehicles-could-save-over-350k-lives-in-the-us-and-millions-worldwide/](https://www.zdnet.com/article/how-autonomous-vehicles-could-save-over-350k-lives-in-the-us-and-millions-worldwide/)

[3] Public Opinion on Self-Driving Cars, Penn State. Accessed at:
[https://sites.psu.edu/mihiryouthere/2017/03/03/public-opinion-on-self-driving-cars/](https://sites.psu.edu/mihiryouthere/2017/03/03/public-opinion-on-self-driving-cars/)

[4] Self-Driving Cars: How Automakers can Overcome Cybersecurity Issues. Jemima
Meyers, tripwire. Accessed at:
[https://www.tripwire.com/state-of-security/featured/self-driving-cars-cybersecurity-issues/](https://www.tripwire.com/state-of-security/featured/self-driving-cars-cybersecurity-issues/)

[5] How Machine Learning Can Enhance Cybersecurity for Autonomous Cars. DINO
CAUSEVIC, toptal. Accessed at:
[https://www.toptal.com/insights/innovation/how-machine-learning-can-enhance-cybersecurity-for-autonomous-cars](https://www.toptal.com/insights/innovation/how-machine-learning-can-enhance-cybersecurity-for-autonomous-cars)

[6] Safety Testing Self Driving Cars need to consider the possible Deep Learning
Weaknesses, nextbigfuture. Accessed at:
[https://www.nextbigfuture.com/2016/10/safety-testing-self-driving-cars-needs.html](https://www.nextbigfuture.com/2016/10/safety-testing-self-driving-cars-needs.html)
