---
layout: post
date: 2020-06-02
---

# Jekyll on Windows Localhost Management

In order to use Jekyll on Windows, we need to have installed Ruby and the Dev Kit (Ruby needs to be added to the Windows path). Ruby can be easily installed for windows using [Rubyinstaller](https://rubyinstaller.org/downloads/). Once the installation process automatically opens the Rubyinstaller terminal, make sure to ENTER 1 and wait for the installation to finish.

At this point we can open the standard windows terminal and test if ruby was installed correctly by typing:

```
gem -v
```
We can now install Bundle in order to manage our Jekyll project.

```
gem install bundler jekyll
```

At this point, we are ready to set up Boudle and create our Gemfile and Gemfile.lock (make sure that you are now in the local Github project repository containing the content which is later going to be push online on Github pages). To do so, we just need to type `boundle init` and then add Jekyll to the Boundle (`bundle add jekyll`). Now we just need to make sure we have installed all the plugins listed in the `_config.yml` file by adding them in the Gemfile (eg. adding `gem 'jekyll-feed'` in the Gemfile will install the feed plugin for our website). By using the following command we can procede to install the created boundle:

```
bundle install
```

Finally, using `bundle exec jekyll serve` we can instantiate our local server which will be available at this link: [http://127.0.0.1:4000](http://127.0.0.1:4000).

Once made the necessary changes locally, we can then push our results live on the web using the basic git workflow.

P.S. When running our blog locally some functionalities that appears online might not appear locally if the Github address is used to reference them (this might not be specified locally which leads to this type of error). In order to fix that, it can be possible to use references to the website base URL (instead of GitHub) making the website behave the same both on local and online.
