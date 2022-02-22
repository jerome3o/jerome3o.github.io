# jeromeswannack.com

The code for jeromeswannack.com, using Jekyll

### Requirements

* Jekyll

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