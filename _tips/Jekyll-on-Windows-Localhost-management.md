---
layout: post
date: 2020-06-02
---

## Jekyll on Windows Localhost Management

In order to use Jekyll on Windows, we need to have installed Ruby and the Dev Kit (Ruby needs to be added to the Windows path). Ruby can be easily installed for windows using [Rubyinstaller](https://rubyinstaller.org/downloads/). Once the installation process automatically opens the Rubyinstaller terminal, make sure to ENTER 1 and wait for the installation to finish.

At this point we can open the standard windows terminal and test if ruby was installed correctly by typing:

```
gem -v
```
We can now install Bundle in order to manage our Jekyll project.

```
gem install bundler jekyll
```

At this point, we are ready to set up Boudle and create our Gemfile and Gemfile.lock (make sure that you are now in the local Github project repository containing the content which is later going to be push online on Github pages). To do so, we just need to type `bundle init` and then add Jekyll to the Boundle (`bundle add jekyll`). Now we just need to make sure we have installed all the plugins listed in the `_config.yml` file by adding them in the Gemfile (eg. adding `gem 'jekyll-feed'` in the Gemfile will install the feed plugin for our website). By using the following command we can procede to install the created boundle:

```
bundle install
```

Finally, using `bundle exec jekyll serve` we can instantiate our local server which will be available at this link: [http://127.0.0.1:4000](http://127.0.0.1:4000).

In order to make sure that the **sitemap.xml** file is updated once added a new page on the website, before running `bundle exec jekyll serve`, delete the _site folder and the sitemap.xml file in the root repository. Once run `bundle exec jekyll serve`, go to the newly created _site folder and find all the localhost base-urls and replace them with the deployed website base-url. Finally, copy and paste the sitemap.xml file in the _site folder to the root folder of the website.

Once made the necessary changes locally, we can then push our results live on the web using the basic git workflow.

P.S. When running our blog locally some functionalities that appears online might not appear locally if the Github address is used to reference them (this might not be specified locally which leads to this type of error). In order to fix that, it can be possible to use references to the website base URL (instead of GitHub) making the website behave the same both on local and online.

## Jekyll on Windows through Docker

A simple set-up to run a Jekyll website as a Docker container locally, could be to create the following **Dockerfile** in the working directory (to build our website locally):

```
FROM jekylljekyll3.8

ADD . srvjekyll

RUN jekyll build

EXPOSE 4000
```

To serve the website we could then create the following **docker-compose.yml** file and using the `docker-compose up` command.

```
jekyll:
  image: jekyll/jekyll:3.8
  command: jekyll serve --force_polling
  ports:
    - 4000:4000
  volumes:
    - .:/srv/jekyll
```

In this example, we are using the files in our working directory and making the website live on port [http://localhost:4000/](http://localhost:4000/).

For Silicon Mac instead, use **Dockerfile**:

```
# Dockerfile for Jekyll on Apple Silicon
FROM --platform=linux/arm64 ruby:3.3-alpine

# Install system dependencies first
RUN apk add --no-cache \
    build-base \
    libffi-dev \
    openssl-dev \
    git \
    nodejs \
    npm \
    gcompat

# Set working directory
WORKDIR /site

# Explicitly update RubyGems and Bundler with verbose output
RUN echo "Current RubyGems version: $(gem --version)" && \
    gem update --system 3.5.3 --no-document && \
    echo "Updated RubyGems version: $(gem --version)" && \
    gem install bundler --no-document

# Copy Gemfile first for better caching
COPY Gemfile* ./

# Configure bundle and install gems
RUN bundle config set --local force_ruby_platform true && \
    bundle config set --local deployment false && \
    BUNDLE_FORCE_RUBY_PLATFORM=1 bundle install --verbose

# Copy the rest of the site
COPY . .

# Expose port
EXPOSE 4000

# Default command
CMD ["bundle", "exec", "jekyll", "serve", "--host", "0.0.0.0", "--port", "4000", "--livereload", "--force_polling"]
```

And **docker-compose.yml**:

```
version: '3.8'
services:
  jekyll:
    build: .
    platform: linux/arm64
    ports:
      - "4000:4000"
    volumes:
      - .:/site
    environment:
      - BUNDLE_FORCE_RUBY_PLATFORM=1

```

In this example, we are again using the files in our working directory and making the website live on port [http://localhost:4000/](http://localhost:4000/) using `docker compose up`.

## Jekyll on Windows through _site folder

Lastly, it could be possible to run the website locally by making use of the content inside the _site folder which is automatically created once built the website. We can then use the files in the _site folder in a simple nginx container.

```
docker run --name <WEBSITE-NAME> -v "%cd%":/usr/share/nginx/html:ro -d -p 8080:80 nginx
```

In this example, we are using the files in our working directory and making the website live on port [http://localhost:8080/](http://localhost:8080/).
