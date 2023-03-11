---
layout: post
title: Machine Learning Rig: Build
---

# Building a Machine Learning Rig from Misc Gaming Hardware

* Want to learn how LLM's work
* Love making things from scratch (made a k8s cluster from RPis)
* Decided to try to get some GPT like models running locally
* End goal is to get GitHub Copilot functionality, and maybe fine-tuned on personal libraries

## Hardware list

* Motherboard
  * Gigabyte: Z170X-Gaming 3
* RAM 
  * 2x 32gb 2666MHz DIMM DDR4
* GPUs
  * 2x AMD Radeon RX 6800 (16gb VRAM)
  * I also have a bunch of other GPUs that are less good
* CPU
  * Intel(R) Core(TM) i7-6700 CPU @ 3.40GHz
* Storage
  * 450gb for the OS
  * 2x 1tb for storing training data

## Build process

I roughly followed the design from [this video](TODO: link video)

TODO: Rough design outline
TODO: Initial materials
TODO: Pictures

## OS and setup

* Ubuntu 20.04
* ROCm Version, amdgpu-install
* rocm-smi output, pytorch, ready to go!
