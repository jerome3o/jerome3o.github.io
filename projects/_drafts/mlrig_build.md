---
layout: post
title: Machine Learning Rig: Building a GPU rig with misc gaming hardware
---

# Building a Machine Learning Rig from Misc Gaming Hardware

I've been following OpenAI and AI more generally for a few years now, and have done a few projects using LLMs and Diffusion models ([GPT-3 dicord bot](https://github.com/jerome3o/gpt3-discord-bot), [stable diffusion videos](https://github.com/jerome3o/stable-diffusion/blob/main/scratch.ipynb)) but more recently I've developed an interest in the nitty gritty details of how GPT-like models work, and what sort of hardware it takes to run.

I love building things from scratch to really understand how they work, and I like trying to get software running on my own hardware (for example I bought and setup 3 RPis to learn about kubernetes). Unfortunately buying eight A100 NVIDIA GPUs was out of my price range so I won't be able to run/fine-tune models like [BLOOM](https://huggingface.co/bigscience/bloom), but I did have three AMD RX6800 GPUs lying around that I sniped off trademe real cheap after the proof of stake Ethereum merge. 

I figure this is enough hardware to get my feet wet, maybe train some smaller models or run some bigger ones [highly quantised](https://timdettmers.com/2022/08/17/llm-int8-and-emergent-features/). They're also AMD GPUs meaning they don't support CUDA natively, which could cause issues, however [ROCm](https://github.com/RadeonOpenCompute/ROCm) seems to be coming along nicely and I'm always up for some additional challenge.

The north star for this project is to try and get Copilot-like functionality in an IDE running all on the local network, I'd also like to try out and see if I can get suggestions on bespoke/private libraries by fine-tuning the model on new source code or using a vector database like [pinecone](https://www.pinecone.io/) or [chroma](https://www.trychroma.com/).

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
  * 2x 1tb for storing training data / models

## Build process

I roughly followed the design from [this video](https://www.youtube.com/watch?v=WImVHF9rrC0)

Here are some pics from the build:

### Starting materials

![build_0](/projects/assets/mlrig_build_0.jpg)

### Partial build

![build_1](/projects/assets/mlrig_build_1.jpg)

### Computer hardware fitcheck

![build_2](/projects/assets/mlrig_build_2.jpg)

### On-off button

Funny story - After putting it all together, I realised that I didn't have a power button. I was turning it on and off by manually shorting the pins on the motherboard. I realised the GPUs had an overclocking button on them, so I figured I could just use that. It was only attached to the GPU with some header pin, so I just pulled them off and plugged it into the motherboard, and it worked!

![build_3](/projects/assets/mlrig_build_3.jpg)

### Finished product, integrated with the battlestation

![build_4](/projects/assets/mlrig_build_4.jpg)

## OS and setup

* Ubuntu 20.04
  * I went with Ubuntu because that seemed to have the best support for ROCm (based on a bit of googling)
* Software installation: ROCm, PyTorch, Jupyter
  * I followed the [installation guide](https://docs.amd.com/bundle/ROCm-Getting-Started-Guide-v5.3/page/How_to_Install_ROCm.html) for ROCm on Ubuntu 20.04
  * I set up the two SSDs as a RAID 0 array using [mdadm](https://wiki.archlinux.org/title/mdadm), and mounted them to `/mnt/raid0`. 
    * I also setup up [MinIO](https://min.io/) on the same RAID array, so I can use it as a S3 bucket for storing training data and models, but for now I'm just using the drives as a local file system because it's all on the same machine.
  * Made a python environment with PyTorch and Jupyter, with JupyterLab starting up on boot (see instructions [here](https://github.com/jerome3o/pytorch_tut#setup))
  
### rocm-smi output
```sh
jerome@mlrig:~$ rocm-smi


======================= ROCm System Management Interface =======================
================================= Concise Info =================================
GPU  Temp (DieEdge)  AvgPwr  SCLK  MCLK   Fan  Perf  PwrCap  VRAM%  GPU%  
0    27.0c           5.0W    0Mhz  96Mhz  0%   auto  203.0W    0%   0%    
1    28.0c           6.0W    0Mhz  96Mhz  0%   auto  203.0W    0%   0%    
================================================================================
============================= End of ROCm SMI Log ==============================

```

I'm going to tinker with the GPU settings to optimise for machine learning performance, but for now I'm just using the default settings.

### JupyterLab

![jupyterlab](/projects/assets/mlrig_build_jupyterlab.png)](/projects/assets/mlrig_build_5.png)


## Next steps
* Start training some models!
* Get good metrics/monitoring for the rig


## Related links

Here are some links to things I referenced when building this rig:
* [ROCm installation guide](https://docs.amd.com/bundle/ROCm-Getting-Started-Guide-v5.3/page/How_to_Install_ROCm.html)
* [GPU rig build youtube video](https://www.youtube.com/watch?v=WImVHF9rrC0)
* [Tim Dettmers Blog](https://timdettmers.com/2018/12/16/deep-learning-hardware-guide/)
  * This blog is amazing, so much good info on hardware (and in general) for machine learning

If you have any questions or comments, feel free to reach out to me at jeromeswannack@gmail.com, or add an issue to the [repo for this project](https://github.com/jerome3o/pytorch_tut#setup).
