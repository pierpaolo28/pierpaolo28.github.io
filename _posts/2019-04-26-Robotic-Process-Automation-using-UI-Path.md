---
layout: post
permalink: blog//blog2/
categories: [Robotics]
---
![](https://cdn-images-1.medium.com/max/2600/1*NaS35BzTK0aHM4c7WpXIDA.png)
<span class="figcaption_hack">(Source
=[https://www.laserfiche.com/wp-content/uploads/2018/01/RPA_Graphics_Infographic_F.png](https://www.laserfiche.com/wp-content/uploads/2018/01/RPA_Graphics_Infographic_F.png))</span>

# Robotic Process Automation (RPA) Using UIPath

> “We’re fascinated with robots because they are reflections of ourselves.”

> — Ken Goldberg

## Introduction

RPA is a technology now developing used to automate manual tasks. What
distinguishes RPA from traditional programming is its graphical user interface
(GUI). RPA automation is performed by breaking down tasks performed by a user
and repeating them. This technology can, therefore, make programming easier for
the automation of graphic based processes. Examples of RPA applications
include[1]:

* Extracting data from scanned documents such as PDFs.
* Generating emails/monitoring an email account.
* Reading and creating invoices.
* Automating Payroll processing.
* Automating complex software-based tasks in static environments.

RPA makes use of software robots to perform tasks in either Web/Desktop or
Citrix environments. On average, robots can perform equivalent processes three
times faster than humans and they are able to work every day of the year 24
hours a day. RPA excels in any type of repetitive rule-based application [2].
Some common examples of RPA companies are Automation Anywhere, UIPath and
blueprism [3].

## UIPath

UIPath Community Edition is a freely available software to
[download](https://www.uipath.com/developers/community-edition-download) on
Windows. Using UIPath, it is possible to implement complex workflows creating
sequences and flowchart based architectures. Each sequence/flowchart can then be
composed of many sub-activities such as recording of a set of actions for the
robot to perform or screen and data scraping instructions. Additionally, UIPath
also enables error handling mechanisms in case of decision-making situations or
the occurrence of unexpected delays between different processes. This can be
done by using control flow commands such as:

* If Statements.
* Waiting for a certain UI element to appear or vanish.
* Adding delays.
* Breaking down workflow execution using the debug mode.

![](https://cdn-images-1.medium.com/max/2600/1*uj78kbtp3vV-95gbylptxg.png)
<span class="figcaption_hack">Figure 1 : UIPath Interface</span>

Another particular utility of UIPath is its ability to work with structured
tables (eg. XLSX and CSV files). This allows developers to loop through and
filter data from tables to process and create structured data gathering
information from the web or any other desktop based application.

As an application example, I created a web-scraping tool to open Chrome to loop
through all the Amazon pages of a chosen category. I can then store, for each
article in the category, the name, price and link in a CSV file. Finally, this
file can be analysed (using python ML algorithms) to see how prices change with
time and compare products with those of different suppliers.

<div>
  <iframe align="middle" width="650" height="500" src="https://www.youtube.com/embed/QSTNb_sDbCo?rel=0"
          frameborder="0" allowfullscreen>
  </iframe>
</div>
<span class="figcaption_hack">Video 1: Amazon Data Scraping Example</span>
<br><br>
UIPath is currently working in its beta version to integrate Computer Vision as
part of its workflow recording application. This could potentially allow for
better integration of UIPath in Virtual Environments making possible for robots
to identify remotely in greater detail the different UI components.

## An RPA business application

During my internship at with [Documation
Software](https://www.documation.co.uk/solutions/robotic-process-automation/), I
had the opportunity to work on RPA using UIPath. As part of my internship, I
successfully managed to automate two workflows:

1.  Registering suppliers in a financial system (taking data from a structured
dataset).
1.  Creating invoices in a financial system using data from a web service.

These two tools can greatly speed up workflow processing in big or medium-sized
companies.

To improve the above workflows, it could be possible to add an error handling
mechanism to store in a CSV file a log of the status of each individual process
executed by the robot and flag any anomalies. This would allow a human operator
to later check how the process was handled by the robot and to see how the robot
reacted to any unexpected event.


## Bibligraphy

[1] 57 RPA Use Cases/ Applications: in-Depth Guide [2019 update] =
[https://blog.aimultiple.com/robotic-process-automation-use-cases/](https://blog.aimultiple.com/robotic-process-automation-use-cases/)

[2] Deutsche Bank =
[https://www.youtube.com/watch?v=ZDKQAJuEQhY](https://www.youtube.com/watch?v=ZDKQAJuEQhY)

[3] Analytics Insight, [Kamalika
Some](https://www.analyticsinsight.net/author/kamalika/) =
[https://www.analyticsinsight.net/top-10-robotic-process-automation-companies-of-2018/](https://www.analyticsinsight.net/top-10-robotic-process-automation-companies-of-2018/)
