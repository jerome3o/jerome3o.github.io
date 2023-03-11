---
layout: post
title: Raspberry Pi Timelapse
---

# Timelapses with RPi4s and RPi Camera modules

* Wanted to timelapse my partners house plants, and new coral reef fish tank
* Decided to use my existing RPi 4s and get some camera modules

## Hardware

* 2 RPi 4s
* Heat sink cases
* Camera module NoIR with fancy lense (TODO: get more details)
* IR Camera module (TODO: get more details)
* Home designed/printed cases

## Designing the Case

* FreeCAD
* TODO: link to designs somehow
* TODO: link to tutorials
* Flatmate's Prussa Mini printer (TODO: link more info)
* Assembly

## Software

* Simple python script with a for loop and `os.system` calls to raspistill and libcamera-still (TODO: link code, double check details)
* Deployed this with tmux and ssh (lol, very hands on)
* Making the timelapse took a bit more compute, so I did this on my server
  * cron jobs to sftp the files over, and delete older ones (copy all, delete older than an hour, TODO: link crontab)
  * cron jobs to make the timelapse (needs some debugging)
* Also set up a simple python static server on the RPi's and used tailscale to network them to our phones so we could get live updates on the fish

## Results

TODO: get some nice timelapses
  
