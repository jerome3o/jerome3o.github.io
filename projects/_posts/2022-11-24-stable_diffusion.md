---
layout: post
title: "Stable Diffusion: Latent Exploration"
---

![double_horse](/projects/assets/stable_diffusion_double_horse.png)
## Exploring Latent Space

"Latent Space" (latent meaning unrealized, existing but not yet manifested) in AI image generation is effectively all of the potential images that an image generation model like Stable Diffusion or DALL-E 2 can potentially create. Encompasses all potential prompts and random seeds, it is immensely huge.

Most people will explore the space by giving these models prompts - but this is only a tiny subset of the whole latent space, there is a lot more out there, and some of it is pretty whacky. In this blog post I go about some ways to explore this space, and some of my early findings.

## Context

After OpenAI released [DALL-E 2](https://openai.com/product/dall-e-2) my fascination with AI image generation was piqued, and when [Stability AI](https://stability.ai/stable-diffusion) open sourced [Stable Diffusion](https://github.com/CompVis/stable-diffusion) I couldn't wait to tinker.

I read about the concept of "exploring latent space" and I ended up buying an RX6800 GPU on [trademe](https://www.trademe.co.nz/a/) for a good price (and then bought two more..) just to run stable diffusion.

## Technical Explanation

In order to explain I'll have to go over some of the basics, I have made some diagrams to help

![stable-diffusion-legend](/projects/assets/stable-diffusion/stable-diffusion-legend.svg)

In a diffusion model like Stable Diffusion or DALL-E 2, a piece of text (a.k.a. a prompt) and some random noise (a bunch of random numbers, proportional to the output image size, kind of) are used to produce an image. Here is a gross simplification of that process:

![stable-diffusion-basic](/projects/assets/stable-diffusion/stable-diffusion-basic.svg)

First, the prompt is "embedded" into a vector space. This is a super [interesting and complicated process](https://lena-voita.github.io/nlp_course/word_embeddings.html), but for our purposes it just means that the text is turned into a giant list of numbers, that represent the meaning behind the original text. This embedded prompt is then fed into a diffusion model (along with some random noise) that does some black magic to convert it into an image (also [super interesting](https://stable-diffusion-art.com/how-stable-diffusion-work/), complicated, and out of scope here).

So we have two easy avenues for tinkering here, we can change the prompt and/or it's embedded representation, and we can adjust the random noise. And this is largely what people do when they use these models

1. Change the prompt, by typing in something different
2. Change the random noise, by simply regenerating the image (with a different random seed)

Changing the random noise is conceptually simpler, and it's effectively how you get 4 images from each prompt when you use DALL-E 2 (they all just have different random noise). But what if we only changed the noise by a little bit? Would we get a mostly similar image? The answer is yes. In order to demonstrate the continuity of the latent image space with respect to changes in the random noise I have created a video.

In this video I generated random noise from a few different random seeds, and then linearly [interpolated](https://en.wikipedia.org/wiki/Interpolation) between the seeds, using each interpolation point to generate a new image from a consistent prompt.

Here is a diagram describing this process:

![stable-diffusion-noise-interpolation](/projects/assets/stable-diffusion/stable-diffusion-noise-interpolation.svg)

And this is the result of the prompt: `Medieval Castle`

<iframe width="100%" height="495" src="https://www.youtube.com/embed/Pd9R_i5Gsa4" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

And here is one with the prompt: `Shi Tzu puppies`

<iframe width="100%" height="495" src="https://www.youtube.com/embed/gFtmpPKGvjc" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

These are interesting, however the subject of the images don't change. The other angle for tinkering is in the prompt, we can do a similar thing as before, but this time interpolate between a sequence of embedded prompts, as described in the diagram below:

![stable-diffusion-prompt-interpolation](/projects/assets/stable-diffusion/stable-diffusion-prompt-interpolation.svg)

This ends up a bit more interesting as you can kind of tell a story. Here is a video made from a sequence of prompts describing the history of human civilization with a dark turn at the end (it should be noted in these videos I am also interpolating across different seeds):

<iframe width="100%" height="495" src="https://www.youtube.com/embed/2KtQzlS8vrc" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

And one of an octopus somehow turning into the flying spaghetti monster:

<iframe width="100%" height="495" src="https://www.youtube.com/embed/eP3gimF5ci4" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

The rest of my videos can be found on [this playlist](https://www.youtube.com/playlist?list=PLqHDGIqcqwiv_kA4ijCODwR398fvYuwbM)

# Source Code and Next Steps

- Next steps
  - Dynamic interpolation steps controlling for image deltas, to smooth out the videos
  - Sync it with music!
  - Make a UI for generating these (or add to existing)

* [Source code for my experiments](https://github.com/jerome3o/stable-diffusion/blob/main/scratch.ipynb) (excuse the mess, it's just a scratch pad)
