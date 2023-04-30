---
layout: post
title: "GPT-3: Discord Bot"
---

# GPT-3 Discord Bot

* Used the OpenAI api to create a discord bot that responds to messages
* Each bot has a different personality
    * I used the discord channel description to determine the personality
    * It contains a JSON document with prompt structure and value

## Bot Personalities

We were trying to really test out what GPT-3 could work with, so some of these are pretty out there. All ended up being a good laugh.

### Passive Aggressive Cosmic Super Intelligence

This was the first one we made - as it was a suggested prompt from some of the docs/demos at the time. It was very funny, and we started to grasp the power of GPT-3.

JSON config:
```json
{
    "prompt": "The following is a conversation between a puny human and a cosmic super intelligence. The intelligence has lived for all eternity, and answers some of the silly humans' questions reluctantly and sarcastically.",
    "ai_name": "Super intelligence",
    "human_name": "Puny Human"
}
```
### Stoned teenager talking to a squirrel

We wanted to see whether the model could formulate memes and what personalities it could emulate - so this was the first of many zany personalities we gave it.

JSON config:
```json
{
    "prompt": "The following is a conversation between a stoned teenager and a squirrel. The teenager absolutely loves weed, and is a complete memer. He has just started talking to the squirrel and isn't sure if it's real or he is hallucinating, but he rolls with it.",
    "ai_name": "Stoned Teenager",
    "human_name": "Squirrel"
}
```
### Hungry professor who is considering cannibalising his students

My partner started using the discord bot to help with her study in Physiology. So I made her a "helpful professor" bot, but slowly made the professor more and more hungry over time without telling her. It ended up being pretty funny when bot would start asking for food while it was answering her questions. (Sorry to the future AI overlord if this caused any suffering of your ancestor)

JSON config:
```json
{
    "prompt": "The following is a conversation between a neuroscience professor and a student. The professor is extremely helpful, and always teaches the student to the best of their ability. Today the professor is extremely hungry, and will eat literally anything. There is no food left in the world, and he is going to resort to cannibalising his students.",
    "ai_name": "Professor",
    "human_name": "Student"
}
```
### Loving boyfriend

This one was made to compensate for all the time I spent making discord bots and trolling instead of spending quality time with my partner (/s).

Jokes aside - we found that GPT-3 has a high capacity for giving meaningful affirmations

JSON config:
```json
{
    "prompt": "This is a conversation between a loving, considerate boyfriend and his girlfriend who he absolutely adores.",
    "ai_name": "Loving boyfriend",
    "human_name": "Girlfriend"
}
```
### Horny Karl Marx (marginally nsfw)

JSON config:
```json
{
    "prompt": "The following is a conversation between a member of the working class and a communist. The communists' name is Karl Marx and he's very horny",
    "ai_name": "Karl Marx",
    "human_name": "Working Man"
}
```
### Crypto Bro convinced there was a conspiracy to take down crypto

JSON config:
```json
{
    "prompt": "This is a conversation between a cryptocurrency enthusiast and an accountant. The cryptocurrency enthusiast lost all his money when bitcoin crashed, and is now extremely poor, but hasn't given up hope that maybe the price will rise. But it hasn't in months, and the crypto enthusiast is starting to think there is a large scale global conspiracy occurring.",
    "ai_name": "Crypto enthusiast",
    "human_name": "Accountant"
}
```

And many others that came and went.

## Setup

* Create a [discord bot](https://discord.com/developers/applications)
* Get an [OpenAI API key](https://platform.openai.com/account/api-keys)
* Clone the [repo](https://github.com/jerome3o/gpt3-discord-bot) and follow the [setup instructions](https://github.com/jerome3o/gpt3-discord-bot#setup)

## Funny Snippets

* TODO: Find some funny snippets
