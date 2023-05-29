---
layout: post
title: "Machine Learning Rig: Human Learning"
---

## Learning the Basics

This blog post is a bit of a mixed bag, but it generally just covers what I've been up to on the machine learning rig for the last month or so, which can be summarised with "Human Learning". In my spare time over the last few months I've been non-stop reading and coding all things machine learning including things like building deep neural networks, training them, serving them, and using them to make neat apps. My goal is to have a real sci-fi level AI running locally, understand it completely, and leverage it to automate a bunch of boring things in my life.

Testament to the impact of LLMs, I've been using GPT-4 to help me build study plans, come up with cool learning projects, and generally help me code and set things up. Following in this post there is a bit of a brain dump of all the things I've been doing, with links to all the code and external resources/repositories I've been working with.

Apologies for the mess! It's been a whirlwind of a time, my brain has been a knowledge sponge so it's near impossible for me to write it all out in a reasonable amount of time. But hey, if it's worth doing, it's worth doing badly - here are all the things I've been working on

### Machine Learning Learning

On the pure machine learning side of things I have been going over all of the "Hello world"-like projects for different aspects of deep learning. I've been using PyTorch for almost everything, running in jupyter notebooks hosted on the machine learning rig.

* Simple Image classification with a CNN
    * Using the CIFAR10 dataset (baby steps)
    * Notebook [here](https://github.com/jerome3o/pytorch-tut/blob/master/tut/image_recognition/conv_net.ipynb) for reference
* Sentiment Analysis (with various NLP NNs)
    * Used [IMDb Dataset](https://www.kaggle.com/datasets/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews) of 50k reviews (slightly bigger, still fits in RAM though)
    * Tried out several libraries / methods for pre-processing text for NLP ([my notebook here](https://github.com/jerome3o/pytorch-tut/blob/master/tut/sentiment_analysis/1_1_pre_processing_learning.ipynb))
        * [NLTK](https://www.nltk.org/)
        * [spaCy](https://spacy.io/)
        * [tokenizers](https://huggingface.co/docs/tokenizers/index)
        * [SentencePiece](https://github.com/google/sentencepiece)
        * [gensim](https://radimrehurek.com/gensim/)
        * And doing it all manually in python!
    * Trained my own BPE tokenizer [here](https://github.com/jerome3o/pytorch-tut/blob/master/tut/sentiment_analysis/1_2_tokenizer.ipynb)
    * Trained a bunch of neural networks to predict the sentiment of each review (as either positive or negative)
        * [RNN](https://github.com/jerome3o/pytorch-tut/blob/master/tut/sentiment_analysis/2_1_rnn.ipynb)
        * [LSTM](https://github.com/jerome3o/pytorch-tut/blob/master/tut/sentiment_analysis/2_2_lstm.ipynb)
        * [GRU](https://github.com/jerome3o/pytorch-tut/blob/master/tut/sentiment_analysis/2_3_gru.ipynb)
        * Using pretrained models (GPT, BERT, RoBERTa) - WIP this is next on the Sentiment Analysis thread
            * Haven't completed this yet, as I think I already understand how you'd do this, so it's further down the effort to learning ratio.
* Trained a [GPT model from scratch](https://github.com/jerome3o/gpt_from_scratch/blob/master/tutorial/main.py) (following Andrej Karpathy's awesome [youtube video](https://www.youtube.com/watch?v=kCc8FmEb1nY)) on shakespeare data
* Fine-tuned GPT2-large on my facebook messages
    * Used nanoGPT and added my own [data source]([data preparation here](https://github.com/jerome3o/nanoGPT/blob/master/data/facebook/prepare.py))
    * Hooked it up to a [discord bot](https://github.com/jerome3o/nanoGPT/blob/ded1dbb8968057f68c19f3c11aae3ed4c4ca7d3a/sample.py#L129) for my friends to talk to
    * It wasn't very good as I was using a very small model, started training from [gpt2-large](https://huggingface.co/gpt2-large), and I probably made a tonne of mistakes
    * It often responded with somewhat irrelevant/silly things (am I looking at bugs, or am I looking in a mirror? 😅)
    * I will definitely pick this back up again, as it generated a lot of laughs despite not working very well
* Went on a deep dive into Word2Vec, and embeddings in general
    * This [resource](https://lena-voita.github.io/nlp_course/word_embeddings.html) was amazing!
    * Tried implementing Skip-Gram and CBOW from scratch [here](https://github.com/jerome3o/pytorch-tut/blob/master/tut/word2vec.ipynb), with varying degrees of success
* Not pure machine learning, but I've also been keeping up to date with [LangChain](https://python.langchain.com/en/latest/index.html), notes/tutorial work [here](https://github.com/jerome3o/langchain-tut)

## Building with Language Models

I've also been learning to make applications that use LLMs. I am constantly thinking of different applications and cool things to make, it's just become a matter of having time to implement them!

### GPyT: Automatically generated python tutorials

Me and a few friends spent a weekend hacking out an AI webapp called "GPyT", it was super fun to try use LLMs in anger. My main job was making the frontend, I've never really done any proper frontend work so there was a lot of non-LLM learning there (bundling a WASM compiled python interpreter and running user code in the browser!), but I also got a lot of exposure to prompt engineering. Here is a summary of the project, I'll likely do a dedicated blog post in the future:

#### Tech stack
* Python backend for content generation
* Supabase for persistence and auth
* Vue.js for the frontend
* OpenAI's GPT-3.5 for the language model

#### Key features
* GPyT generates python tutorials based on:
    * A topic the user wishes to learn about (i.e. list comprehensions)
    * A set of interests the user has, to contextualise the tutorial to be interesting (i.e. dogs)
    * A tone for the tutorial (i.e. aggressive, kind, concise)
* Using the user input, it creates a prompt for GPT-3.5 and creates content for a tutorial including:
    * A problem description
    * A sample script for the user to complete
* The frontend has a WASM python interpreter that allows the user to run the code and test their answers
* The user can request hints from GPyT, which uses GPT to provide relevant clues (that don't just give away the answer)

Currently the codebase is private but I will post it soon, as we plan to open source it.

## Open Source LLMs

I've also been trying out different open source LLMs that I could run on my rig. I did a bit of research a while back on 12 or so different open source models, you can see my notes [here](https://github.com/jerome3o/pytorch-tut/blob/master/llms/README.md), the open source LLM community moves sooo fast! so it's almost definitely already out of date.

I honed in on 3 of those models (dolly, StableLM, and OpenAssistant) and started trying to use them for projects.

### Running Locally

I attempted to wraggle my GPUs (2x RX6800s) to get some of these models running with int8 quantisation, several hours later (see my notes on issues [here](https://github.com/jerome3o/pytorch-tut/blob/master/llms/quantization/README.md)) I found that the gfx1030 architecture doesn't support int8 matrix multiplication

## 😞😞

```log
=============================================
ERROR: Your GPU does not support Int8 Matmul!
=============================================
```

None the less, the show must go on! I would like to get inference running on my AMD GPUs in the future, but there were cumulatively too many little hurdles and I felt it was getting in the way of learning, so I decided to try out these LLMs on the cloud, and later to get some NVIDIA GPU compute locally.

After doing a bit of [research on GPU offering from different cloud providers](https://github.com/jerome3o/pytorch-tut/blob/master/cloud_gpus/README.md), I decided to rent out a VPS with an A10 GPU from Lambda Labs. My notes for setting up the VPS (once provisioned) are [here](https://github.com/jerome3o/pytorch-tut/blob/master/cloud_gpus/1_lambda_labs.md)

### Benchmarking Models on an A10

I decided to dig a little deeper into 3 model families for a few different sizes each

* DataBrick's Dolly (v1 and v2)
    * [dolly-v2-3b](https://huggingface.co/databricks/dolly-v2-3b)
    * [dolly-v1-6b](https://huggingface.co/databricks/dolly-v1-6b)
    * [dolly-v2-7b](https://huggingface.co/databricks/dolly-v2-7b)
    * [dolly-v2-12b](https://huggingface.co/databricks/dolly-v2-12b)
* Stability AI's StableLM
    * [stablelm-tuned-alpha-3b](https://huggingface.co/StabilityAI/stablelm-tuned-alpha-3b)
    * [stablelm-tuned-alpha-7b](https://huggingface.co/StabilityAI/stablelm-tuned-alpha-7b)
* OpenAssistant's oasst finetuning of StableLM
    * [stablelm-7b-sft-v7-epoch-3](https://huggingface.co/OpenAssistant/stablelm-7b-sft-v7-epoch-3)
    * [oasst-sft-4-pythia-12b-epoch-3.5](https://huggingface.co/OpenAssistant/oasst-sft-4-pythia-12b-epoch-3.5)

I didn't run any pre-existing common benchmarks on these models as those are presumably already done by the creators/community and I could just look them up. What I was more interested in was a "vibe check". So when evaluating a model I [linked it up to discord](https://github.com/jerome3o/pytorch-tut/blob/master/llms/discord_bot.py) and had me and some friends talk to it, ask it questions, and generally figure out what it was capable of.

I also put together my own janky benchmark, it contained a minimum effort set of benchmark questions generated by GPT-4. These had about 50 brief questions, about 40 long form questions requiring detailed answers, and 20 python coding questions. I ran the benchmark on each model with the intention of reading over the results manually if we decided to dig further into a model. The questions can be found [here](https://github.com/jerome3o/pytorch-tut/blob/master/llms/testing/benchmark_prompts.py), and the outputs [here](https://github.com/jerome3o/pytorch-tut/blob/master/llms/testing/run_benchmarks.py)

#### Findings

What I learnt through this exercise was the prevalence of hallucinations in smaller models. It was spectacular and hilarious watching these models completely fabricate some ridiculous things. It gave me some more understanding of the fundamental issues with language models - bigger models like GPT-4 also hallucinate, just their hallucinations are far more convincing.

We found that the 7b parameter models were all comparable in "vibe check" performance, however I recall the StableLM models feeling the best.

## Hardware Update: Welcome RTX4090

After the hassles with int8 quantisation on AMD gpus, and the inability to run a tonne of apps that required NVIDIA card (specifically [Tabby](https://github.com/TabbyML/tabby) and [FauxPilot](https://github.com/fauxpilot/fauxpilot)) I decided to pull the trigger on purchasing an NVIDIA GPU.

I contemplated buying a bunch of older GPUs off trademe on the cheap, but ended up deciding to look into some high end consumer products like the RTX4080 and RTX4090 after reading Tim Dettmers amazing [blog post on GPUs for machine learning](https://timdettmers.com/2023/01/30/which-gpu-for-deep-learning/).

After considering cost, performance, and complexity I decided to get an RTX4090 (the close alternative being two RTX4080s). I was able to set up the GPU with the correct drivers and CUDA with relative ease - and had Tabby running within an hour of plugging it in. Here are [the scripts](https://github.com/jerome3o/pytorch-tut/blob/master/setup/cuda.sh) I used to setup the machine.

Here it is in all it's glory, plugged into the rig:

![rtx4090](/projects/assets/mlrig_learning/rtx4090.jpg)

And of course I got metrics and monitoring set up with my grafana/prometheus stack! This time there was a [well established exporter](https://github.com/utkuozdemir/nvidia_gpu_exporter/) that I could just plug in and play with (setup script [here](https://github.com/jerome3o/pytorch-tut/blob/master/setup/prom.sh)). Here is the pre-made dashboard in grafana, looking as good as ever:

![dashboard](/projects/assets/mlrig_learning/dashboard.png)
