---
layout: post
title: "Smart Flat: Noise Maker"
---

The latest of a collection of smart home projects made as banter with my flatmates.

With a view to learning how to use the programming language [Golang](https://go.dev/) and the popular open source message broker [RabbitMQ](https://www.rabbitmq.com/) (and to find new ways to annoy my flatmates) I've made the latest addition to our dumb smart home: An annoying sound maker.

It comprises of three moving parts:
1. A [frontend](https://github.com/jerome3o/jankyflat/blob/master/producer/main.go) that serves a UI with a single button on it that requests an annoying sound to be made
2. A [RabbitMQ deployment](https://github.com/jerome3o/jankyflat/blob/master/rabbitmq/docker-compose.yml) for brokering the request for annoying sounds
3. A [consumer](https://github.com/jerome3o/jankyflat/blob/master/consumer/main.go) that listens for requests and plays a sound through a speaker in our hallway.

If you've got a bunch of RPis, speakers, spare time, and good flatmates sitting around feel free to try it out. The [source code](https://github.com/jerome3o/jankyflat) is available to all, and setup and running is well documented in the read me.

The frontend (not my best work):

![smart_flat_fe](/projects/assets/smart_flat_fe.png)

And our sound station:

![smart_flat_sound_station](/projects/assets/smart_flat_sound_station.png)

With the help our local DNS server and NGINX on our flat server whenever someone on our local network goes to `http://annoyingsound.lan` they can make a [gnome sound](https://www.youtube.com/watch?v=KnHmoA6Op1o)

Why did I do this?