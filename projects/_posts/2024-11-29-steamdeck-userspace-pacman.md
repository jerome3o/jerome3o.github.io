---
layout: post
title: "Steam Deck hacking: Setting up user space pacman"
---

# Setting Up Userspace Package Management on Steam Deck

November 29, 2024

## Overview

Today I'll cover:
* Setting up pacman to install packages in userspace on Steam Deck
* A detailed explanation of a script that automates the setup
* Solutions to some specific issues with Perl modules and device nodes
* How this enables persistent package installations across system updates

## The Motivation

I've been hacking around on my Steam Deck (as you do), with the vague goal of trying to get some cool speech to text using [Deepgram](https://deepgram.com/) while gaming so I don't have to type stuff on the deck. Anyway - the first thing I needed to get working was my [dotfiles](https://github.com/jerome3o/dotfiles), which require GNU [stow](https://www.gnu.org/software/stow/) for management (I don't really need this, but I love a good [yak shave](https://seths.blog/2005/03/dont_shave_that/)). However, the Steam Deck uses an immutable root filesystem with A/B partitioning for updates, meaning any system-level package installations get wiped when the system updates. TL;DR this means any package I install with [pacman](https://wiki.archlinux.org/title/Pacman) (the steam deck runs [SteamOS](https://store.steampowered.com/steamos), based on arch) will get wiped on updates to the deck.

This is no good, because I don't want to have to re-setup my dev environment on every update...

## The Solution

I found this excellent blog post by etaoin.sh about [installing pacman packages in userspace](https://etaoin.sh/posts/m9g%20userspace%20pacman.html) on Steam Deck. The post describes using pacman's `-r` option to install packages to an alternate root directory, allowing installations to persist across system updates.

However, I ran into several issues while following the tutorial, and even once I had pacman working, I still had issues with stow specifically (around package signing and Perl module paths). [Claude](https://claude.ai) was incredibly helpful in debugging these issues and helped me create a script to automate the entire setup process. Following is a setup script for pacman on Steam Deck, written by Claude ([YMMV](https://dictionary.cambridge.org/dictionary/english/ymmv)) that configures pacman to install packages in userspace (specifically in `~/.root/`), sets up an alias `pacman_` that you should use to install stuff thereafter. It also set up some environment variables for perl, I suspect there will be a long tail of other issues here - I recommend copying this whole post (along with [etaoin's post](https://etaoin.sh/posts/m9g%20userspace%20pacman.html)) into claude.ai along with your errors and ask for a fix to your specific problem.

## The Setup Script

Here's a script that automates the entire setup process, with extensive error checking and comments:

```bash
#!/bin/bash

# Steam Deck Userspace Pacman Setup Script
# This script sets up a userspace pacman installation on Steam Deck
# allowing package installations that persist across system updates

# Exit on error, undefined variables, and propagate pipe errors
set -euo pipefail

# Helper function for logging
log() {
    echo "$(date '+%Y-%m-%d %H:%M:%S') - $1"
}

# Helper function for error handling
error() {
    log "ERROR: $1" >&2
    exit 1
}

# Check if running on Steam Deck
if ! grep -q "steamos" /etc/os-release; then
    error "This script must be run on Steam Deck"
fi

# Check if running as deck user
if [[ "$(whoami)" != "deck" ]]; then
    error "This script must be run as the deck user"
fi

# Set up main variables
USERROOT="/home/deck/.root"
PACMAN_CONF="$USERROOT/etc/pacman.conf"
GPG_DIR="$USERROOT/etc/pacman.d/gnupg"

# Create directory structure
log "Creating directory structure..."
mkdir -p "$USERROOT"/{etc,var/lib/pacman,dev,usr/lib/locale}

# Create essential device symlinks
log "Setting up device nodes..."
for dev in null zero random urandom; do
    if [[ ! -e "$USERROOT/dev/$dev" ]]; then
        sudo ln -s "/dev/$dev" "$USERROOT/dev/$dev"
    fi
done

# Copy and modify pacman configuration
log "Configuring pacman..."
if [[ ! -f "$PACMAN_CONF" ]]; then
    cp /etc/pacman.conf "$PACMAN_CONF"
    # Update DBPath in pacman.conf
    sed -i "s|^#\?DBPath.*|DBPath = $USERROOT/var/lib/pacman/|" "$PACMAN_CONF"
fi

# Initialize pacman keyring
log "Initializing pacman keyring..."
mkdir -p "$GPG_DIR"
sudo pacman-key --gpgdir "$GPG_DIR" --init
sudo pacman-key --gpgdir "$GPG_DIR" --populate archlinux

# Import and sign SteamOS keys
log "Importing SteamOS keys..."
sudo pacman-key --gpgdir "$GPG_DIR" --add /etc/pacman.d/gnupg/pubring.gpg
sudo pacman-key --gpgdir "$GPG_DIR" --lsign-key "GitLab CI Package Builder <ci-package-builder-1@steamos.cloud>"

# Define the environment setup
ENVSETUP="\
# Userspace pacman environment setup
export USERROOT=\"$USERROOT\"
export PATH=\"\$PATH:\$USERROOT/usr/bin\"
export LD_LIBRARY_PATH=\"\$LD_LIBRARY_PATH:\$USERROOT/lib:\$USERROOT/lib64\"
export PERL5LIB=\"\$USERROOT/usr/share/perl5/vendor_perl:\$USERROOT/usr/lib/perl5/5.38/vendor_perl:\$USERROOT/usr/share/perl5/core_perl:\$USERROOT/usr/lib/perl5/5.38/core_perl\"
alias pacman_='sudo pacman -r \$USERROOT --config \$USERROOT/etc/pacman.conf --gpgdir \$USERROOT/etc/pacman.d/gnupg'
"

# Add environment setup to .bashrc if not already present
if ! grep -q "USERROOT=\"$USERROOT\"" ~/.bashrc; then
    log "Adding environment setup to .bashrc..."
    echo -e "\n$ENVSETUP" >> ~/.bashrc
fi

# Initial pacman sync
log "Syncing pacman databases..."
eval "$(echo "$ENVSETUP")"
pacman_ -Sy

log "Setup complete! Please:"
log "1. Run 'source ~/.bashrc' to load the new environment"
log "2. Test the installation with 'pacman_ -S stow'"
log "3. Verify stow works with 'stow -h'"

# Note: The script has set up:
# - A userspace root at ~/.root
# - Pacman configuration and keyring
# - Required device nodes and directories
# - Environment variables and aliases in .bashrc
#
# You can now install packages with 'pacman_' and they will persist
# across Steam Deck system updates.
```

Let's break down what this script is doing:

### 1. Initial Setup and Safety Checks
```bash
set -euo pipefail
```
This ensures the script fails fast if anything goes wrong. The script also verifies it's running on Steam Deck as the deck user.

### 2. Directory Structure
The script creates several essential directories:
* `~/.root` - Our userspace root directory
* `~/.root/etc` - Configuration files
* `~/.root/var/lib/pacman` - Package database
* `~/.root/dev` - Essential device nodes
* `~/.root/usr/lib/locale` - Locale information

### 3. Device Nodes
One issue I encountered was missing device nodes, particularly `/dev/null`. The script creates symlinks to essential device nodes:
```bash
for dev in null zero random urandom; do
    sudo ln -s "/dev/$dev" "$USERROOT/dev/$dev"
done
```

### 4. Pacman Configuration
The script copies and modifies the pacman configuration, ensuring the database path points to our userspace location. It also sets up the keyring and imports the SteamOS keys - this was crucial for resolving package signing issues.

### 5. Environment Setup
The script adds necessary environment variables to `.bashrc`:
* `USERROOT` - Points to our userspace root
* `PATH` - Includes our userspace binaries
* `LD_LIBRARY_PATH` - For userspace libraries
* `PERL5LIB` - This was key for getting stow working!

The `PERL5LIB` addition was particularly important. Without it, stow would fail because it couldn't find its Perl modules. This is a great example of the kind of issues you might encounter with other packages too.

## Using the Setup

After running the script:
1. Source your updated environment: `source ~/.bashrc`
2. Install packages using the `pacman_` alias
3. Your installations will persist across system updates!

## Future Considerations

While this setup works great for stow, you might encounter similar issues with other packages:
* Missing device nodes
* Library path issues
* Module/plugin path problems

The good news is that the pattern for fixing these is similar: identify what resources the package is looking for, and either symlink them from the system or adjust environment variables to include your userspace paths.

## Conclusion

This setup provides a nice solution for persistent package management on Steam Deck. While the original tutorial got me most of the way there, the additional fixes for device nodes and Perl modules were crucial for getting everything working smoothly.

Big thanks to:
* etaoin.sh for the original tutorial
* The SteamOS team for building on Arch Linux, making this possible
* [Claude](https://claude.ai) for helping debug issues and writing a good chunk of this blog post! 😄

The full script is available above - feel free to adapt it for your needs. If you run into issues or have improvements to suggest, [let me know](https://github.com/jerome3o)!
