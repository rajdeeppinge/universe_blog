# Use official Ruby image as a base
FROM ruby:3.4

# Install dependencies (for Jekyll to run correctly)
RUN apt-get update -qq && apt-get install -y nodejs postgresql-client

# Set the working directory inside the container
WORKDIR /usr/src/app

# Copy the Gemfile and install the necessary gems
COPY Gemfile* ./
RUN gem install bundler && bundle install

# Copy the rest of the app (Jekyll site) to the container
# Note: During development, this will be overridden by the mounted volume. 
#       Check the associated docker-compose.yml
COPY . .

# Expose port 4000 for the Jekyll server
EXPOSE 4000

# Command to run the Jekyll server
CMD ["bundle", "exec", "jekyll", "serve", "--host", "0.0.0.0"]
