---
layout: post
title: Machine Learning Rig: Build
---

# Building a Machine Learning Rig from Misc Gaming Hardware

I've been following OpenAI and AI more generally for a few years now, and have done a few projecs using LLMs and Diffusion models ([GPT-3 dicord bot](https://github.com/jerome3o/gpt3-discord-bot), [stable diffusion videos](https://github.com/jerome3o/stable-diffusion/blob/main/scratch.ipynb)) but more recently I've developed an interest in the nitty gritty details of how GPT-like models work, and what sort of hardware it takes to run.

I love building things from scratch to really understand how they work, and I like trying to get software running on my own hardware (for example I bought and setup 3 RPis to learn about kubernetes). Unfortunately buying eight A100 NVIDIA GPUs was out of my price range so I won't be able to run [BLOOM](https://huggingface.co/bigscience/bloom), but I did have three AMD RX6800 GPUs lying around that I sniped off trademe real cheap after the proof of stake Ethereum merge. 

I figure this is enough hardware to get my feet wet, maybe train some smaller models or run some bigger ones [highly quantised](https://timdettmers.com/2022/08/17/llm-int8-and-emergent-features/). They're also AMD GPUs meaning they don't support CUDA natively, which could cause issues, however [ROCm](https://github.com/RadeonOpenCompute/ROCm) seems to be coming along nicely and I'm always up for some additional challenge.

The north start for this project is to try and get Copilot-like functionality in an IDE running all on the local network, I'd also like to try out and see if I can get suggestions on bespoke/private libraries by fine-tuning the model on new source code.

This blog post outlines the hardware and early software setup.

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
