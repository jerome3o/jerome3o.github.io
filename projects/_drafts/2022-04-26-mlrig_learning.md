---
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

## Building with LLMs

I've also spent a bunch of time learning to make things using a language model

* GPyT: Automatically generated python tutorials
    * Me and a few friends spent a weekend hacking out an AI app called GPyT
* [LangChain Tutorials / Learning](https://github.com/jerome3o/langchain-tut)

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
