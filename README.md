# jeromeswannack.com

The code for jeromeswannack.com, using Jekyll

### Requirements

* Jekyll

### Docker

```sh
sudo docker run -it --rm -p 4000:4000 -v $(pwd):/site/ ruby:2.7.4-slim-buster bash
```

```sh
cd /site
apt update
apt install -y ruby-dev gcc libffi-dev make build-essential
bundle install
bundle exec jekyll serve --host 0.0.0.0
```

### Setup

```bash
# Install ruby
sudo apt-get install ruby-full build-essential zlib1g-dev

# Set gems to install in non-root dir (this should be put in your .bashrc)
export GEM_HOME="$HOME/gems"
export PATH="$HOME/gems/bin:$PATH"

gem install jekyll bundler
bundle install  # ???
```

### Serve locally

```bash
bundle exec jekyll serve
```
