---
layout: post
title: Boids in WASM
---

The goal for this project was to try out [Web Assembly](https://webassembly.org/) (WASM). Having recently learnt a bit of [golang](https://go.dev/) for work and out of personal interest I decided a good foray into WASM would be to make a quick write up of [boids](http://www.red3d.com/cwr/boids/) in golang, compile it to WASM, and render the boids using javascript (I went with the [p5js](https://p5js.org/) framework for the animation).

Please have a play around with a demo of the boids [here](/demos/boids/)!

I've made the boids afraid of the mouse, which is a fun way of interacting

I also set up some sliders to allow you to configure the different boid parameters:

* **Separation**: How strongly the boids repel away from each other.
* **Alignment**: How strongly the boids want to fly in the same direction.
* **Cohesion**: How strongly the boids want to group together.
* **Velocity**: With this implementation of boids I opted to go with a simplified rule acceleration aggregation method - where all rules accelerations are added to the velocity vector, then the vector is normalised, so all boids have a constant velocity. This parameter sets that constant velocity value.
* **Neighbourhood** Radius: The simulated vision of a boid, only boids at least this close will be considered "neighbours" and be used for evaluating the flocking behaviours.


And to get a little look under the hood I've added in a debug boid (I actually used this for debugging but thought it was quite cool so kept it). This boid has a large purple circle around it indicating it's neighbourhood, and any boid in that neighbourhood is also indicated by a smaller surrounding purple circle.