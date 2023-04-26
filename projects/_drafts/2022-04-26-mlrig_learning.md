---
layout: post
title: "Machine Learning Rig: Experimenting with Open Source LLMs"
---

## On the ML Rig

* Configured all requirements for bitsandbytes
* Had to fix apt, after trying to install everything from source
    * Link to learning repo
* Turns out the RX6800 gfx1030 architecture doesn't support int8 matrix multiplication so quantisation is a no go on the ML rig

## Cloud Providers

* Going to the cloud to try out models with quantisation
* Looked around, main competitors are GCP and Lambda Labs for casual ML
* Went with lambda labs for a weekend, hired an A10 for 3 days for $20

## Benchmarking Models on an A10

Add a write up for each of these. And a link to the benchmark results (also make the results webpages)

* Dolly
* StableLM
* OpenAssistant

## 8 Bit Quantisation

A little write up on quantisation to get some understanding
