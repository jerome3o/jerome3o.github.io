---
layout: post
title: "Smart Flat: HTTP API for my bedroom light"
---

Over the last while I have played around a bit with smart switches and smart bulbs. I've automated my heater so that my room is on in the hours I'm usually home, I've set up a plug to monitor my power usage and display it in a grafana dashboard (wasn't very exciting), and I've set my lights to turn on gently over the morning to help me wake up.

Something annoying though is the plugs and bulbs I've used, despite all being tp-link, have different apps on android. The smart switches require the Kasa app, and the bulbs Tapo. I decided to try make my own app that would control them all.

Although I didn't quite succeed in making a unified app, but I did succeed in making an HTTP API for my lights (the plan was to make the frontend later). 

This was written in TypeScript using [Express](https://expressjs.com/) (to leverage the the [tp-link-tapo-connect](https://github.com/dickydoouk/tp-link-tapo-connect) api) and exposes two simple GET http endpoints: `/on` and `/off` which turn my light on and off respectively.

The source code for the project is [here](https://github.com/jerome3o/dumb_bulb)

The reason I didn't make the frontend as planned is because I realised that I could add a widget to my phone's home screen with the [HTTP Request Widget](https://play.google.com/store/apps/details?id=com.idlegandalf.httprequestwidget&hl=en_NZ&gl=US) app. This resulted in a pretty clean UX where I don't have to open an app to control my lights:

![smart_flat_dumb_bulb_homescreen](/projects/assets/smart_flat_dumb_bulb_homescreen.png)

And I also added bookmarks in my browser so I could turn my lights on and off easily from my PC


![smart_flat_dumb_bulb_bookmarks](/projects/assets/smart_flat_dumb_bulb_bookmarks.png)