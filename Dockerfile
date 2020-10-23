FROM jekylljekyll3.8

ADD . srvjekyll

RUN jekyll build

EXPOSE 4000