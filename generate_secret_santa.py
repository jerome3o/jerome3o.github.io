#!/usr/bin/env python3
"""
Secret Santa Generator
Creates a single cycle through all participants and generates HTML pages with unique URLs.
"""

import random
import uuid
import json
from pathlib import Path

# Participants
PARTICIPANTS = [
    "Audrey Swannack",
    "Cole Swannack",
    "Harriet Stockman",
    "Jane Rayswan",
    "Jerome Swannack",
    "Jessica",
    "Kayla Swannack",
    "Lindsay Swannack",
    "Rowan Swannack",
    "Shane Swannack",
]

OUTPUT_DIR = Path("secret-santa")


def generate_cycle(participants):
    """
    Generate a single cycle through all participants.
    This ensures no small loops and no one gets themselves.

    Algorithm: Shuffle the list and create a cycle where each person
    gives to the next person in the shuffled list (wrapping around).
    """
    # Create a copy and shuffle to randomize
    shuffled = participants.copy()
    random.shuffle(shuffled)

    # Create the mapping: person[i] gives to person[(i+1) % n]
    # This guarantees a single cycle through all participants
    mapping = {}
    n = len(shuffled)
    for i in range(n):
        giver = shuffled[i]
        receiver = shuffled[(i + 1) % n]
        mapping[giver] = receiver

    return mapping


def verify_single_cycle(mapping):
    """
    Verify that the mapping creates a single cycle through all participants.
    """
    if not mapping:
        return False

    # Start from any participant
    start = next(iter(mapping))
    current = start
    visited = set()

    # Follow the cycle
    while current not in visited:
        visited.add(current)
        current = mapping[current]

    # Should visit all participants and return to start
    return len(visited) == len(mapping) and current == start


def generate_html_page(giver, receiver, year=2025):
    """Generate HTML page for a participant with fancy 3D gift box."""
    return f"""---
layout: none
---
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Secret Santa {year} 🎄</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}

        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Arial, sans-serif;
            background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            padding: 20px;
            overflow: hidden;
            position: relative;
        }}

        /* Subtle snowflakes */
        .snowflake {{
            position: absolute;
            top: -10px;
            color: rgba(255, 255, 255, 0.3);
            font-size: 1em;
            animation: fall linear infinite;
            pointer-events: none;
        }}

        @keyframes fall {{
            to {{
                transform: translateY(100vh);
            }}
        }}

        .welcome-text {{
            text-align: center;
            color: #f0f0f0;
            margin-bottom: 50px;
            z-index: 10;
            max-width: 600px;
        }}

        .welcome-text h1 {{
            font-size: 2.5em;
            font-weight: 300;
            margin-bottom: 20px;
            color: #ffd700;
        }}

        .welcome-text p {{
            font-size: 1.3em;
            line-height: 1.6;
            color: #e0e0e0;
        }}

        .lucky-number {{
            color: #ffd700;
            font-weight: bold;
        }}

        /* 3D Gift Box */
        .gift-container {{
            perspective: 1000px;
            z-index: 10;
        }}

        .gift-box {{
            width: 200px;
            height: 200px;
            position: relative;
            transform-style: preserve-3d;
            animation: rotate 8s infinite linear;
            cursor: pointer;
            transition: all 0.5s ease;
        }}

        .gift-box.opened {{
            animation: none;
        }}

        @keyframes rotate {{
            from {{
                transform: rotateY(0deg);
            }}
            to {{
                transform: rotateY(360deg);
            }}
        }}

        .face {{
            position: absolute;
            width: 200px;
            height: 200px;
            background: linear-gradient(135deg, #c41e3a 0%, #8b0000 100%);
            border: 3px solid #ffd700;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 3em;
        }}

        .front  {{ transform: translateZ(100px); }}
        .back   {{ transform: rotateY(180deg) translateZ(100px); }}
        .right  {{ transform: rotateY(90deg) translateZ(100px); }}
        .left   {{ transform: rotateY(-90deg) translateZ(100px); }}
        .top    {{ transform: rotateX(90deg) translateZ(100px); background: #ffd700; }}
        .bottom {{ transform: rotateX(-90deg) translateZ(100px); }}

        /* Ribbon */
        .ribbon-v {{
            position: absolute;
            width: 40px;
            height: 200px;
            background: #ffd700;
            left: 50%;
            transform: translateX(-50%);
            z-index: 5;
        }}

        .ribbon-h {{
            position: absolute;
            width: 200px;
            height: 40px;
            background: #ffd700;
            top: 50%;
            transform: translateY(-50%);
            z-index: 5;
        }}

        .bow {{
            position: absolute;
            top: -30px;
            left: 50%;
            transform: translateX(-50%);
            font-size: 3em;
            z-index: 10;
        }}

        /* Reveal Section */
        .reveal {{
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0, 0, 0, 0.95);
            display: none;
            justify-content: center;
            align-items: center;
            z-index: 100;
        }}

        .reveal.active {{
            display: flex;
        }}

        .reveal-content {{
            text-align: center;
            color: white;
            animation: revealFade 1s ease-in;
        }}

        @keyframes revealFade {{
            from {{
                opacity: 0;
                transform: scale(0.5);
            }}
            to {{
                opacity: 1;
                transform: scale(1);
            }}
        }}

        .reveal-content h2 {{
            font-size: 2em;
            margin-bottom: 30px;
            color: #ffd700;
        }}

        .reveal-content .name {{
            font-size: 4em;
            font-weight: bold;
            color: #fff;
            text-shadow: 0 0 20px rgba(255, 215, 0, 0.8);
            margin: 30px 0;
        }}

        .reveal-content .budget {{
            font-size: 1.8em;
            color: #ffd700;
            margin: 20px 0;
        }}

        .reveal-content .message {{
            font-size: 1.2em;
            color: #e0e0e0;
            max-width: 500px;
            margin: 20px auto;
            line-height: 1.6;
        }}

        /* Confetti */
        .confetti {{
            position: fixed;
            width: 10px;
            height: 10px;
            background: #ffd700;
            position: absolute;
            animation: confetti-fall 3s linear;
        }}

        @keyframes confetti-fall {{
            to {{
                transform: translateY(100vh) rotate(360deg);
                opacity: 0;
            }}
        }}

        /* Firework */
        .firework {{
            position: fixed;
            width: 4px;
            height: 4px;
            border-radius: 50%;
            animation: firework 1s ease-out;
        }}

        @keyframes firework {{
            0% {{
                transform: translate(0, 0);
                opacity: 1;
            }}
            100% {{
                transform: translate(var(--x), var(--y));
                opacity: 0;
            }}
        }}

        .tap-hint {{
            margin-top: 30px;
            color: #ffd700;
            font-size: 1.2em;
            animation: pulse 2s infinite;
        }}

        @keyframes pulse {{
            0%, 100% {{
                opacity: 1;
            }}
            50% {{
                opacity: 0.5;
            }}
        }}

        @media (max-width: 600px) {{
            .welcome-text h1 {{
                font-size: 1.8em;
            }}

            .welcome-text p {{
                font-size: 1.1em;
            }}

            .gift-box {{
                width: 150px;
                height: 150px;
            }}

            .face {{
                width: 150px;
                height: 150px;
            }}

            .front  {{ transform: translateZ(75px); }}
            .back   {{ transform: rotateY(180deg) translateZ(75px); }}
            .right  {{ transform: rotateY(90deg) translateZ(75px); }}
            .left   {{ transform: rotateY(-90deg) translateZ(75px); }}
            .top    {{ transform: rotateX(90deg) translateZ(75px); }}
            .bottom {{ transform: rotateX(-90deg) translateZ(75px); }}

            .ribbon-v {{
                width: 30px;
                height: 150px;
            }}

            .ribbon-h {{
                width: 150px;
                height: 30px;
            }}

            .reveal-content .name {{
                font-size: 2.5em;
            }}
        }}
    </style>
</head>
<body>
    <!-- Snowflakes -->
    <div class="snowflake" style="left: 10%; animation-duration: 10s;">❄</div>
    <div class="snowflake" style="left: 20%; animation-duration: 12s; animation-delay: 1s;">❄</div>
    <div class="snowflake" style="left: 30%; animation-duration: 15s; animation-delay: 2s;">❄</div>
    <div class="snowflake" style="left: 40%; animation-duration: 11s;">❄</div>
    <div class="snowflake" style="left: 50%; animation-duration: 14s; animation-delay: 3s;">❄</div>
    <div class="snowflake" style="left: 60%; animation-duration: 13s;">❄</div>
    <div class="snowflake" style="left: 70%; animation-duration: 16s; animation-delay: 1s;">❄</div>
    <div class="snowflake" style="left: 80%; animation-duration: 12s; animation-delay: 2s;">❄</div>
    <div class="snowflake" style="left: 90%; animation-duration: 15s;">❄</div>

    <div class="welcome-text">
        <h1>🎄 Welcome to the <span class="lucky-number">$57</span> Secret Santa! 🎄</h1>
        <p>Hello, <strong>{giver}</strong>! Tap the gift below to discover who you're Secret Santa for this year.</p>
    </div>

    <div class="gift-container">
        <div class="gift-box" id="giftBox" onclick="openGift()">
            <div class="bow">🎀</div>
            <div class="ribbon-v"></div>
            <div class="ribbon-h"></div>
            <div class="face front">🎁</div>
            <div class="face back">🎁</div>
            <div class="face right">🎁</div>
            <div class="face left">🎁</div>
            <div class="face top"></div>
            <div class="face bottom">🎁</div>
        </div>
    </div>

    <div class="tap-hint">👆 Tap the gift to open!</div>

    <!-- Reveal Section -->
    <div class="reveal" id="reveal">
        <div class="reveal-content">
            <h2>🎯 You are Secret Santa for:</h2>
            <div class="name">{receiver}</div>
            <div class="budget">💰 Budget: <span class="lucky-number">$57</span> 💰</div>
            <div class="message">
                🤫 Remember to keep it secret!<br>
                🎁 Have fun finding the perfect gift!<br>
                ✨ Happy Holidays! ✨
            </div>
        </div>
    </div>

    <script>
        let opened = false;

        function openGift() {{
            if (opened) return;
            opened = true;

            const giftBox = document.getElementById('giftBox');
            const reveal = document.getElementById('reveal');

            // Stop rotation and add opened class
            giftBox.classList.add('opened');

            // Show reveal after a short delay
            setTimeout(() => {{
                reveal.classList.add('active');
                createConfetti();
                createFireworks();
            }}, 500);
        }}

        function createConfetti() {{
            const colors = ['#ffd700', '#ff6b6b', '#4ecdc4', '#45b7d1', '#f38181'];
            for (let i = 0; i < 100; i++) {{
                setTimeout(() => {{
                    const confetti = document.createElement('div');
                    confetti.className = 'confetti';
                    confetti.style.left = Math.random() * 100 + 'vw';
                    confetti.style.top = -10 + 'px';
                    confetti.style.background = colors[Math.floor(Math.random() * colors.length)];
                    confetti.style.animationDelay = Math.random() * 2 + 's';
                    document.body.appendChild(confetti);

                    setTimeout(() => confetti.remove(), 3000);
                }}, i * 30);
            }}
        }}

        function createFireworks() {{
            const colors = ['#ffd700', '#ff6b6b', '#4ecdc4', '#45b7d1', '#f38181', '#fff'];

            function createFirework() {{
                const x = Math.random() * window.innerWidth;
                const y = Math.random() * window.innerHeight;

                for (let i = 0; i < 30; i++) {{
                    const firework = document.createElement('div');
                    firework.className = 'firework';
                    firework.style.left = x + 'px';
                    firework.style.top = y + 'px';
                    firework.style.background = colors[Math.floor(Math.random() * colors.length)];

                    const angle = (Math.PI * 2 * i) / 30;
                    const velocity = 50 + Math.random() * 100;
                    const dx = Math.cos(angle) * velocity;
                    const dy = Math.sin(angle) * velocity;

                    firework.style.setProperty('--x', dx + 'px');
                    firework.style.setProperty('--y', dy + 'px');

                    document.body.appendChild(firework);

                    setTimeout(() => firework.remove(), 1000);
                }}
            }}

            // Create multiple fireworks
            for (let i = 0; i < 5; i++) {{
                setTimeout(createFirework, i * 300);
            }}
        }}
    </script>
</body>
</html>
"""


def generate_index_page(links_mapping, year=2025):
    """Generate index page with all the links."""
    links_html = ""
    for giver, link_id in sorted(links_mapping.items()):
        links_html += f'            <li><strong>{giver}</strong>: <a href="{link_id}.html" target="_blank">{link_id}.html</a></li>\n'

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Secret Santa {year} - Admin</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}

        body {{
            font-family: 'Georgia', serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 40px 20px;
        }}

        .container {{
            background: white;
            border-radius: 20px;
            padding: 50px;
            max-width: 1000px;
            margin: 0 auto;
            box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
        }}

        h1 {{
            color: #2d3748;
            font-size: 2.5em;
            margin-bottom: 10px;
            text-align: center;
        }}

        .warning {{
            background: #fed7d7;
            border-left: 4px solid #f56565;
            padding: 20px;
            margin: 30px 0;
            border-radius: 5px;
        }}

        .warning-title {{
            color: #c53030;
            font-weight: bold;
            font-size: 1.2em;
            margin-bottom: 10px;
        }}

        .warning-text {{
            color: #742a2a;
        }}

        .links-section {{
            margin-top: 40px;
        }}

        h2 {{
            color: #2d3748;
            font-size: 1.8em;
            margin-bottom: 20px;
        }}

        ul {{
            list-style: none;
        }}

        li {{
            background: #f7fafc;
            padding: 15px 20px;
            margin-bottom: 10px;
            border-radius: 8px;
            border-left: 4px solid #667eea;
        }}

        li strong {{
            color: #2d3748;
            display: inline-block;
            min-width: 180px;
        }}

        a {{
            color: #667eea;
            text-decoration: none;
            word-break: break-all;
        }}

        a:hover {{
            color: #764ba2;
            text-decoration: underline;
        }}

        .instructions {{
            background: #e6fffa;
            border-left: 4px solid #38b2ac;
            padding: 20px;
            margin: 30px 0;
            border-radius: 5px;
        }}

        .instructions-title {{
            color: #234e52;
            font-weight: bold;
            font-size: 1.2em;
            margin-bottom: 10px;
        }}

        .instructions-text {{
            color: #234e52;
            line-height: 1.6;
        }}

        @media (max-width: 600px) {{
            .container {{
                padding: 30px 20px;
            }}

            h1 {{
                font-size: 2em;
            }}

            li strong {{
                display: block;
                margin-bottom: 5px;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1>🎄 Secret Santa {year} - Admin Panel</h1>

        <div class="warning">
            <div class="warning-title">⚠️ Keep This Page Private!</div>
            <div class="warning-text">
                This page contains all the Secret Santa assignments. Do not share this page with participants!
                Only share individual links with each person.
            </div>
        </div>

        <div class="instructions">
            <div class="instructions-title">📝 Instructions</div>
            <div class="instructions-text">
                1. Click on each person's link below to copy their unique URL<br>
                2. Send each person ONLY their own link (via text, email, etc.)<br>
                3. The links are random and non-guessable for privacy<br>
                4. Each person will see who they need to buy a gift for
            </div>
        </div>

        <div class="links-section">
            <h2>Individual Links</h2>
            <ul>
{links_html}            </ul>
        </div>
    </div>
</body>
</html>
"""


def main():
    random.seed()  # Use current time as seed for randomness

    print("🎄 Secret Santa Generator 🎄")
    print(f"\nParticipants ({len(PARTICIPANTS)}):")
    for i, participant in enumerate(PARTICIPANTS, 1):
        print(f"  {i}. {participant}")

    # Create output directory
    OUTPUT_DIR.mkdir(exist_ok=True)

    # Check if mapping already exists
    mapping_file = OUTPUT_DIR / "mapping.json"
    if mapping_file.exists():
        print("\n📂 Found existing mapping.json, using existing allocations...")
        mapping_data = json.loads(mapping_file.read_text())
        mapping = mapping_data["pairings"]
        links_mapping = mapping_data["links"]
        print("✅ Loaded existing allocations (pairings unchanged!)")
    else:
        # Generate the pairing
        print("\n🎲 Generating Secret Santa pairings...")
        mapping = generate_cycle(PARTICIPANTS)

        # Verify it's a single cycle
        if not verify_single_cycle(mapping):
            print("❌ Error: Failed to generate a single cycle. Please run again.")
            return

        print("✅ Successfully generated a single cycle (no small loops!)")

        # Generate unique IDs for each person
        links_mapping = {}
        for giver in PARTICIPANTS:
            unique_id = str(uuid.uuid4())
            links_mapping[giver] = unique_id

    # Generate HTML pages
    print(f"\n📄 Generating HTML pages in '{OUTPUT_DIR}/'...")
    for giver, receiver in mapping.items():
        unique_id = links_mapping[giver]
        html_content = generate_html_page(giver, receiver)

        output_file = OUTPUT_DIR / f"{unique_id}.html"
        output_file.write_text(html_content)
        print(f"  ✓ Generated: {giver} -> {unique_id}.html")

    # Generate index page
    index_file = OUTPUT_DIR / "index.html"
    index_content = generate_index_page(links_mapping)
    index_file.write_text(index_content)
    print(f"\n✅ Generated admin page: {index_file}")

    # Save mapping to JSON for reference
    mapping_data = {
        "pairings": mapping,
        "links": links_mapping,
    }
    mapping_file.write_text(json.dumps(mapping_data, indent=2))
    print(f"✅ Saved mapping data: {mapping_file}")

    print("\n" + "="*60)
    print("🎉 Secret Santa setup complete!")
    print("="*60)
    print(f"\n📋 Next steps:")
    print(f"  1. Open '{OUTPUT_DIR}/index.html' to see all the links")
    print(f"  2. Send each person their unique link")
    print(f"  3. Keep the index page and mapping.json private!")
    print("\n🎁 Happy Holidays! 🎄\n")


if __name__ == "__main__":
    main()
