    # "databricks/dolly-v2-3b",
    # "databricks/dolly-v1-6b",
    # "databricks/dolly-v2-7b",
    # "databricks/dolly-v2-12b",
    # "OpenAssistant/stablelm-7b-sft-v7-epoch-3",
    "OpenAssistant/oasst-sft-4-pythia-12b-epoch-3.5",
    "StabilityAI/stablelm-tuned-alpha-3b",
    "StabilityAI/stablelm-tuned-alpha-7b",https://github.com/jerome3o/pytorch-tut/blob/master/llms/discord_bot.py---
layout: post
title: "Machine Learning Rig: Learning the Basics, open source LLMs, and a hardware update"
---

# Learning the Basics

Using GPT-4 as an interactive tutorial + tutor.

## Machine Learning

* Simple Image classification with a CNN
    * CIFAR10
    * Notebook [here](https://github.com/jerome3o/pytorch-tut/blob/master/tut/image_recognition/conv_net.ipynb)
* Sentiment Analysis (with various NLP NNs)
    * Used [IMDb Dataset](https://www.kaggle.com/datasets/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews) of 50k reviews.
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
            * Haven't completed this yet, as I think I already understand how you'd do this

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

# Building with Language Models

I've also spent a bunch of time learning to actually make things using LLMs. Here

## GPyT: Automatically generated python tutorials

* Me and a few friends spent a weekend hacking out an AI webapp called "GPyT"
* Tech stack: python backend for prompt engineering, supabase for persistence and auth, Vue.js frontend
* It generates python tutorials based on:
    * A topic the user wishes to learn about (i.e. list comprehensions)
    * A set of interests the user has, to contextualise the tutorial to be interesting (i.e. dogs)
    * A tone for the tutorial (i.e. aggressive, kind, concise)
* Using the user input, it creates a prompt for GPT-4 and creates content for a tutorial including:
    * A problem description
    * A sample script for the user to complete
* The frontend has a WASM python interpreter that allows the user to run the code and test their answers
* The user can request hints from GPyT, which uses GPT to provide relevant clues (that don't just give away the answer)
* Currently the codebase is private, but I will post it and probably do a write-up when we open source it.

## Tutorials / Other Learning

I've also been keeping up do date with popular LLM libraries - mainly LangChain

* [LangChain Tutorials / Learning](https://github.com/jerome3o/langchain-tut)

# Open Source LLMs

I also spent a fair amount of time trying out different open source LLMs that I could run on my rig.

I did a quick read up on 12 or so different models, notes are [here](https://github.com/jerome3o/pytorch-tut/blob/master/llms/README.md).

## Running Locally

I attempted to wraggle my GPUs (2x RX6800s) to get some of these models running with int8 quantisation, several hours later (see my notes on issues [here](https://github.com/jerome3o/pytorch-tut/blob/master/llms/quantization/README.md)) I found that the gfx1030 architecture doesn't support int8 matrix multiplication

## 😞😞

```log
=============================================
ERROR: Your GPU does not support Int8 Matmul!
=============================================
```

None the less, the show must go on. I would like to get inference running on my AMD GPUs in the future, but there were cumulatively too many little hurdles and I felt it was getting in the way of learning, so I decided to try out these LLMs on the cloud, and later to get some NVIDIA GPU compute locally.

After doing a bit of [research on GPU offering from different cloud providers](https://github.com/jerome3o/pytorch-tut/blob/master/cloud_gpus/README.md), I decided to rent out a VPS with an A10 GPU from Lambda Labs. My notes for setting up the VPS (once provisioned) are [here](https://github.com/jerome3o/pytorch-tut/blob/master/cloud_gpus/1_lambda_labs.md)

## Benchmarking Models on an A10

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

I didn't run any common benchmarks on these models as those are presumably already done by the creators/community and I could just look them up. What I was more interested in was a "vibe check". So when evaluating a model I [linked it up to discord](https://github.com/jerome3o/pytorch-tut/blob/master/llms/discord_bot.py) and had me and some friends talk to it, ask it questions, and generally figure out what it was capable of.

I also put together my own janky benchmark, it contained a minimum effort set of benchmark questions generated by GPT-4. These had about 50 brief questions, about 40 long form questions requiring detailed answers, and 20 python coding questions. I ran the benchmark on each model with the intention of reading over the results manually if we decided to dig further into a model. The questions can be found [here](https://github.com/jerome3o/pytorch-tut/blob/master/llms/testing/benchmark_prompts.py), and the outputs [here](https://github.com/jerome3o/pytorch-tut/blob/master/llms/testing/run_benchmarks.py)

### Findings

What I learnt through this exercise was the prevalence of hallucinations in smaller models. It was spectacular and hilarious watching these models completely fabricate some ridiculous things. It gave me some more understanding of the fundamental issues with language models - bigger models like GPT-4 also hallucinate, just their hallucinations are far more convincing.

We found that the 7b parameter models were all comparable in "vibe check" performance, however I recall the StableLM models feeling the best.

# Hardware Update

Purchased an RTX 4090
