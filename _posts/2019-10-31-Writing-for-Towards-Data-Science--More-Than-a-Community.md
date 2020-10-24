---
layout: post
permalink: blog/blog32/
categories: [Extra]
---

![](https://cdn-images-1.medium.com/max/2600/0*dD5UTIOOuzA7ko1F)
<span class="figcaption_hack">Photo by [Patrick
Fore](https://unsplash.com/@patrickian4?utm_source=medium&utm_medium=referral)
on [Unsplash](https://unsplash.com?utm_source=medium&utm_medium=referral)</span>

<!--end_excerpt-->

# Writing for Towards Data Science: More Than a Community

## An intro on how to get started writing for Towards Data Science and my journey so far.

> “There is no real ending. It’s just the place where you stop the story.”

> ― Frank Herbert

### Introduction

I am now about to start my eight-month as a writer for Towards Data Science
(TDS) and today I decided to take a look at my journey so far.

Having a PhD in order to work in Data Science, especially in research, seems to
be nowadays more and more a necessity. Therefore, at the beginning of this year,
I also considered this opportunity and I decided to write a research proposal
and apply for a position.

One month after, I had been offered the role.

At this point, I started thinking if this would have been the right choice for
me, and I decided to turn down the offer. I thought there must be another way to
continue my researches in Data Science and share my results to a wider audience.

During the few months preceding my application for the PhD position, Towards
Data Science had been a valuable companion of travel, which helped me to always
go deeper into this subject. Therefore, I decided to try giving back something
to the community publishing [a redacted part of my research proposal on
Medium](https://towardsdatascience.com/need-for-explainability-in-ai-and-robotics-75dc6077c9fa).
Since then, thanks to [Ludovic Benistant](https://medium.com/u/895063a310f4), I
became I writer for Towards Data Science.

Some of the main reason which pushed me to keep writing in the last few months
have been:

* “If you can’t explain it simply, you don’t understand it well enough” ([Albert
Einstein](https://www.brainyquote.com/authors/albert-einstein-quotes)**).**
* Recording my journey.
* Making new connections.
* Challenging myself to learn something new every day.
* Giving something back to the community.

I will now walk you through some suggestions on what kind of article to write
for Towards Data Science and how to best edit them.

### The Writer’s Block

One of the main concerns someone can have when thinking about starting writing
are:

* Are my writing skills good enough to make my story publishable?
* Is the topic of my article worth publishing?

To answer the first question, I would consider a quote from [Richard
Bach](https://en.wikipedia.org/wiki/Richard_Bach):

> “A professional writer is an amateur who didn’t quit.”

> — Richard Bach

Therefore, only writing and getting feedback from editors and readers we can be
able to improve ourself and our communication abilities.

Each story submitted to Towards Data Science is first reviewed from an editor
before being published. In this way, the publication can ensure that just the
best content is published and writers can receive feedback on how to improve
their stories. Additionally, TDS also provides general support in case a writer
is looking for any general advice on how to improve their writing.

In order to answer the second question, I always ask myself 3 questions before
start writing a story:

* How can my story benefit to my readers? (empowering them)
* If I were to research this topic online, how difficult it would be for me to
find good content about it?
* Can my story be able to make research-based content accessible to a less
technical audience?

If I can find a good answer to all these 3 questions, I will then start working
on my article.

In fact, most of my articles ideas come while working on a project for which I
struggled to find good and updated material online.

> “If there’s a book that you want to read, but it hasn’t been written yet, then
> you must write it.”

> ― Toni Morrison

Finally, if your content is original and brings value to their readers, you will
always find an audience interested in reading it.

> “If the book is true, it will find an audience that is meant to read it.”

> — Wally Lamb

### General Guidelines

I will now give you some advice on how to write a good article ready for
publication.

#### Grammarly

Grammarly is an AI power writing assistant which can be easily used while
writing Medium articles by installing their [web
extension](https://www.grammarly.com/). Using Grammarly will make almost
impossible for your article to have spelling or idiomatic mistakes.

#### GitHub Gists

A large part of Towards Data Science articles contains code. Code snippets can
be easily integrated into the Medium Markdown Interface by pressing
simultaneously Control + Alt + 6 on either Windows or Mac.

    This type of code snippet is commonly used to diplay code outputs

Another option can be to use [GitHub
Gists](https://help.github.com/en/github/writing-on-github/creating-gists). Gits
are really easy to create and offer the advantage to provide syntax highlighting
and greater formatting flexibility. If you have never used GitHub Gists, the
GitHub documentation is a great place where to
[start](https://help.github.com/en/github/writing-on-github/creating-gists). In
order to embed a Gist in a Medium article, just make sure to select the Sharable
Link option instead of Embed.

<script src="https://gist.github.com/pierpaolo28/094f40204b273dfcd86fdee16e1550c2.js"></script>

#### Free Open Data Sources

A really good way to explain topics about Data Science is to provide walkthrough
examples which can be easily repeatable. In order to do so, using open-source
datasets can be a great idea. In this way, the readers would be able to try
themself how the code works and how changing it might affect the overall
results.

One of the best places where to look for open-source datasets and share output
codes is [Kaggle](https://www.kaggle.com/). Other examples of websites where is
possible to download free datasets are [UCI Machine Learning
Repository](https://archive.ics.uci.edu/ml/index.php) and
[data.world](https://data.world/).

#### Interactive Data Visualization

Adding interactive graphs and GIF animations can be another way to add value to
your article, as the reader can be able to change himself some of the parameters
of the animation.

An example of interesting Data Visualization can be the GIF below. From Figure 1
we can, in fact, be able to visualize how the variance of the 3 principal
components in a PCA (Principal Component Analysis) plot are distributed. Using a
static figure it wouldn’t have been possible to see in such details the results
in all the three different axes.

![](https://cdn-images-1.medium.com/max/2000/1*CQql1Trl3_PO8YS198lRgQ.gif) <br>
<span class="figcaption_hack">Figure 1: PCA variance plot</span>

An example of Interactive Data Visualization is instead shown below. In Figure
2, we can examine (using the slider) how varying the number of estimators in a
Random Forest Classifier can affect the overall accuracy of our model considered
the selected *min_split* and *min_leaf parameters*.

Feel free to play with the graph below by changing the *n_estimators*
parameters, zooming in and out of the graph, changing it’s orientation and
hovering over the single data points to get additional information about them!

<iframe width="900" height="800" frameborder="0" scrolling="no" src="//plot.ly/~pierpaolo28/13.embed"></iframe><span class="figcaption_hack">Figure 2: Interactive Data Visualization</span>

If you are looking for a bit of context on how I created these two animations,
more information is available in my [Interactive Data
Visualization](https://towardsdatascience.com/interactive-data-visualization-167ae26016e8)
and [Hyperparameters
Optimization](https://towardsdatascience.com/hyperparameters-optimization-526348bb8e2d)
articles.

#### Curators Guidelines

Every time an article is published on Medium platform, it gets reviewed by a
curator to decide if the should or not be advertised on Medium and in any of the
article tags topics. Therefore, meeting the curators' guidelines can be a really
important step to write a successful article.

If you are interested in finding out more about the Medium’s Curation
Guidelines, these are available
[here](https://help.medium.com/hc/en-us/articles/360006362473-Medium-s-Curation-Guidelines-everything-writers-need-to-know).
Additionally, also Towards Data Science has written it's own [Submitting your
article —
checklist](https://towardsdatascience.com/post-for-writers-2-ebd32d1fac21).

#### TDS Submission

In order to submit your first article for Towards Data Science, all you have to
do is write a draft on Medium and read the guidelines available [here](https://towardsdatascience.com/questions-96667b06af5). Then the
publication will review your article and come back to you.

Additionally, Towards Data Science also recently launched a YouTube channel on
which you can contribute to creating your own video tutorials (as I did for my
[GPU Accelerated Data Analytics & Machine
Learning](https://towardsdatascience.com/gpu-accelerated-data-analytics-machine-learning-963aebe956ce)
article). More information about it is available
[here.](https://towardsdatascience.com/submit-your-video-to-towards-data-science-f8432d67a777)

*****

**Thanks for reading!**
