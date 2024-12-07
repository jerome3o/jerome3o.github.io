---
layout: post
title: "MCP: Claude as a factorio sysadmin"
date: 2024-12-07
---

## When AI Meets Factory Automation

Over the last year I've been working as a software engineer at [Anthropic](https://www.anthropic.com/) building out features for claude.ai. One of my favourite things we've built is the [Model Context Protocol](https://www.anthropic.com/news/model-context-protocol) - it basically allows anyone to build their own integrations to claude.ai. I've also been playing Factorio Space Age on my Steam Deck lately, and I couldn't resist creating an MCP server that allows claude to make JIT mods (and do general admin-y stuff) for my factorio server.

{% include youtube.html id="53-SPxNpQg4" %}

In this video, you can watch me having a laugh with it - building stuff around my character, giving items, adding silly little mods, etc.

## The Model Context Protocol: A Quick Primer

For those unfamiliar, MCP is an open protocol which enables language models to interact with external tools and data sources. Think of it as a standardized way for AI models to reach out into the real world (or in this case, the virtual world of Factorio).

The protocol establishes a clear interface for AI models to:
- Access external data through Resources
- Execute actions through Tools
- Follow interaction patterns through Prompts

## Architecture: How It All Works

The system consists of three main components:

```
```mermaid
graph LR
    Claude --> MCP_API
    MCP_API --> HTTP_Backend
    HTTP_Backend --> Factorio
```
```

1. **The MCP Server**: Built with [FastMCP](https://github.com/jlowin/fastmcp), this provides Claude with a high-level interface to interact with Factorio. It translates Claude's intentions into game commands.

2. **HTTP Backend**: A simple FastAPI server that securely wraps the factorio RCON server. This layer handles authentication and provides a clean HTTP interface.

3. **Factorio Server**: The actual game server running Space Age, accepting RCON commands and executing them in the game world.

## The Fun Part: Just-In-Time Modding

The most interesting discovery from this project wasn't the ability to get Claude to give me items or teleport me around (though that was fun). It's the realization that Claude can essentially create "Just-In-Time mods" using Factorio's Lua API.

Here's an example of a mod that claude made (I don't actually know lua) that makes bugs appear near my character ever 5 seconds:

```lua
-- Script to spawn biters near player "jermoe" every 5 seconds

-- Initialize a variable to track the last spawn time
global.last_spawn_time = 0

-- Event handler that runs every tick
script.on_event(defines.events.on_tick, function(event)
    -- Check if 5 seconds (300 ticks) have passed since last spawn
    if event.tick >= global.last_spawn_time + 300 then
        -- Get the player named "jermoe"
        local player = game.get_player("jermoe")

        -- Only proceed if the player exists and is valid
        if player and player.valid then
            -- Get the surface the player is on
            local surface = player.surface
            -- Get player's position
            local position = player.position

            -- Find a non-colliding position near the player (within 10 tiles)
            local spawn_position = surface.find_non_colliding_position(
                "small-biter",  -- Entity name
                {x = position.x + math.random(-10, 10), y = position.y + math.random(-10, 10)},  -- Random position near player
                10,  -- Search radius
                1    -- Precision
            )

            -- If we found a valid position, create the biter
            if spawn_position then
                surface.create_entity({
                    name = "small-biter",
                    position = spawn_position,
                    force = "enemy"
                })
            end

            -- Update the last spawn time
            global.last_spawn_time = event.tick
        end
    end
end)
```

Claude wrote this code on the fly, understanding both:
1. The basics of the Factorio Lua API and modding ecosystem
2. The constraints of the RCON command interface
3. How to write a safe, non-destructive event handler
4. How to properly handle game states and entity validity
5. How to work with in-game coordinates and entity spawning

It's not just executing pre-written commands - it's actually programming custom behaviors in real-time. (It also fetched the docs in the conversation using the [fetch MCP server](https://github.com/modelcontextprotocol/servers/tree/main/src/fetch) which I thought was neat)

## Building the Integration

The implementation using FastMCP is very clean. Here's a key example showing how we expose Lua execution to Claude (assuming we have the `send_message` and `run_lua` commands wired up to hit the http backend):

```python
@mcp.tool()
def run_lua(code: str, explanation: Optional[str] = None) -> str:
    """
    Run arbitrary Lua code on the Factorio server
    """
    if explanation:
        send_message(f"Action: {explanation}")
    return execute_command(f"/sc {code}")

@mcp.tool()
def give_items(player: str, item: str, count: int = 1) -> str:
    """Give items to a player"""
    return run_lua(
        f'game.players["{player}"].insert{{name="{item}", count={count}}}',
        f"Giving {count}x {item} to {player}"
    )
```

The `explanation` parameter is neat - it makes Claude announce what it's about to do, giving players a heads-up before random things start happening around them in the server

## Implications for Gaming and Next Steps

I've seen a lot of projects using LLMs to simulate NPCs, and I made this as a joke, but it was actually a pretty interesting experience being able to manifest things in-game just by asking.

Next up I'd like to implement a generic (agentic) MCP client + http server in python that can invoke an MCP enabled claude agent from an HTTP request, then hit this every time an in-game message from a player is sent. This should close the loop and allow anyone in the server to create JIT mods (and probably break everything...), while also putting together some pretty interesting building blocks for future projects.

## Try It Yourself

Want to experiment with this? Check out the [GitHub repository](https://github.com/jerome3o/factorio-mcp) for setup instructions. It's pretty thrown together, but if it's interesting to you and you can't get it up and running, chuck an issue in the repo or hmu at jeromeswannack@gmail.com.
