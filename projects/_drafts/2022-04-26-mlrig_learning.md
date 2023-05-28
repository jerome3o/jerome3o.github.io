---
layout: post
title: "Machine Learning Rig: Learning the Basics, open source LLMs, and a hardware update"
---

# Learning the Basics

Using GPT-4 as an interactive tutorial + tutor.

* Simple Image classification with a CNN
    * CIFAR10
    * Notebook [here](https://github.com/jerome3o/pytorch-tut/blob/master/tut/image_recognition/conv_net.ipynb)
* Sentiment Analysis (with various NLP NNs)
    * Used [IMDb Dataset](https://www.kaggle.com/datasets/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews) of 50k reviews.
    * Tried out several libraries / methods for pre-processing text for NLP ([notebook](https://github.com/jerome3o/pytorch-tut/blob/master/tut/sentiment_analysis/1_1_pre_processing_learning.ipynb))
        * [NLTK](https://www.nltk.org/)
        * [spaCy](https://spacy.io/)
        * [tokenizers](https://huggingface.co/docs/tokenizers/index)
        * [SentencePiece](https://github.com/google/sentencepiece)
        * [gensim](https://radimrehurek.com/gensim/)
        * And doing it all manually in python!

# Open Source LLMs

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


# Hardware Update

Purchased an RTX 4090
