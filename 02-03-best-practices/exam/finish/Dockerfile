FROM ruby:2.5.5-stretch

WORKDIR /app
COPY Gemfile* /app

RUN curl -sL https://deb.nodesource.com/setup_9.x > setup_9.x \
    && echo "958c9a95c4974c918dca773edf6d18b1d1a41434  setup_9.x" | sha1sum -c - \
    &&  bash  setup_9.x \
    && rm -rf setup_9.x \
    && apt-get -y install libpq-dev imagemagick gsfonts nodejs \
    && gem install bundler \
    && bundle install --without development test --path vendor/bundle \
    && rm -rf /usr/local/bundle/cache/*.gem \
    && apt-get clean  \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

COPY . /app
RUN rake assets:precompile

CMD ["bundle”, “exec”, “passenger”, “start"]
