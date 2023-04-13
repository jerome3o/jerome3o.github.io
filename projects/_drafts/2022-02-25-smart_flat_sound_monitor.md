---
layout: post
title: "Smart Flat: Sound Monitor"
---

Am I being too loud? am I annoying my flatmates? What is the exact sound frequency distribution in the hallway of our flat? These are questions I had all too often, but they're a thing of the past.

In the hallway of our flat that connects 3 of our flatmates rooms I've set up a microphone to measure sound levels. There is a raspberry pi with a little python server running that buffers some data from the mic, calculates an approximate level and a frequency breakdown of the noise, then streams it to clients subscribed via websockets.

It also hosts a little frontend that uses plotly.js to provide a simple live plot of the noise in our hallway.

![sound_monitor_gui](/projects/assets/smart_flat_sound_monitor_gui.png)

As always the [source code](https://github.com/jerome3o/sound_monitor) is available. And feel free to ping me if you're interested in surveilling the sound in your flat, actually on second thought don't, that's kinda weird.

## Notes and TODOs

* I found that the loudest noises I was making were footsteps, this makes sense on a sound transmission level as low frequency noise is less attenuated travelling through walls, but I also think it could be to do with the mic is structurally coupled to the floor via the table it is on.
* I would like to scale the noise to the sensitivity of the human ear, so that it is more representative of audible noise levels.
* Sometimes the websocket stream lags, this is my first real foray into websockets and the python asyncio module, so I suspect my implementation is far from perfect. Learning more about those two things is up on my personal TODOs.