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