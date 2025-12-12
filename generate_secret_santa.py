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
    """Generate HTML page for a participant with fancy 3D gift box that opens."""
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
            background: linear-gradient(135deg, #2c1810 0%, #1a0f0a 100%);
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
            color: rgba(255, 255, 255, 0.4);
            font-size: 1.2em;
            animation: fall linear infinite;
            pointer-events: none;
            z-index: 1;
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

        /* 3D Gift Box Container */
        .gift-container {{
            perspective: 1500px;
            z-index: 10;
            position: relative;
        }}

        .gift-scene {{
            width: 250px;
            height: 300px;
            position: relative;
            transform-style: preserve-3d;
            transition: transform 2s;
        }}

        .gift-scene:not(.opened) {{
            animation: float 3s ease-in-out infinite;
        }}

        @keyframes float {{
            0%, 100% {{ transform: translateY(0px) rotateY(0deg); }}
            50% {{ transform: translateY(-20px) rotateY(10deg); }}
        }}

        /* Gift Box Base */
        .box-base {{
            width: 250px;
            height: 200px;
            position: absolute;
            bottom: 0;
            transform-style: preserve-3d;
            cursor: pointer;
        }}

        .box-base .side {{
            position: absolute;
            background: linear-gradient(135deg, #dc143c 0%, #8b0000 100%);
            border: 2px solid #ffd700;
        }}

        .box-base .front {{
            width: 250px;
            height: 200px;
            transform: translateZ(125px);
        }}

        .box-base .back {{
            width: 250px;
            height: 200px;
            transform: rotateY(180deg) translateZ(125px);
        }}

        .box-base .left {{
            width: 250px;
            height: 200px;
            transform: rotateY(-90deg) translateZ(125px);
        }}

        .box-base .right {{
            width: 250px;
            height: 200px;
            transform: rotateY(90deg) translateZ(125px);
        }}

        .box-base .bottom {{
            width: 250px;
            height: 250px;
            transform: rotateX(-90deg) translateZ(0px);
            background: #8b0000;
        }}

        /* Ribbon on base */
        .ribbon {{
            position: absolute;
            background: #ffd700;
            z-index: 10;
        }}

        .ribbon.vertical {{
            width: 50px;
            height: 200px;
            left: 100px;
            top: 0;
        }}

        .ribbon.horizontal {{
            width: 250px;
            height: 50px;
            left: 0;
            top: 75px;
        }}

        /* Gift Box Lid */
        .box-lid {{
            width: 250px;
            height: 100px;
            position: absolute;
            bottom: 200px;
            transform-style: preserve-3d;
            transition: transform 1.5s ease;
            transform-origin: bottom center;
            cursor: pointer;
        }}

        .gift-scene.opened .box-lid {{
            transform: rotateX(-120deg) translateZ(-50px);
        }}

        .box-lid .side {{
            position: absolute;
            background: linear-gradient(135deg, #ff6347 0%, #dc143c 100%);
            border: 2px solid #ffd700;
        }}

        .box-lid .top {{
            width: 250px;
            height: 250px;
            transform: rotateX(90deg) translateZ(100px);
            background: linear-gradient(135deg, #ffd700 0%, #ffed4e 100%);
            border: 2px solid #dc143c;
        }}

        .box-lid .front {{
            width: 250px;
            height: 100px;
            transform: translateZ(125px);
        }}

        .box-lid .back {{
            width: 250px;
            height: 100px;
            transform: rotateY(180deg) translateZ(125px);
        }}

        .box-lid .left {{
            width: 250px;
            height: 100px;
            transform: rotateY(-90deg) translateZ(125px);
        }}

        .box-lid .right {{
            width: 250px;
            height: 100px;
            transform: rotateY(90deg) translateZ(125px);
        }}

        /* Bow on lid */
        .bow {{
            position: absolute;
            top: -40px;
            left: 50%;
            transform: translateX(-50%);
            font-size: 4em;
            z-index: 20;
            filter: drop-shadow(0 5px 10px rgba(0,0,0,0.5));
        }}

        /* Name reveal inside box */
        .name-reveal {{
            position: absolute;
            bottom: 20px;
            left: 50%;
            transform: translateX(-50%);
            font-size: 2.5em;
            font-weight: bold;
            color: #ffd700;
            text-shadow: 0 0 20px rgba(255, 215, 0, 0.8), 0 0 40px rgba(255, 215, 0, 0.6);
            opacity: 0;
            transition: opacity 1s ease 1s;
            z-index: 5;
            white-space: nowrap;
            max-width: 90%;
            overflow: hidden;
            text-overflow: ellipsis;
        }}

        .gift-scene.opened .name-reveal {{
            opacity: 1;
        }}

        /* Budget info */
        .budget-info {{
            position: absolute;
            bottom: -80px;
            left: 50%;
            transform: translateX(-50%);
            font-size: 1.5em;
            color: #ffd700;
            opacity: 0;
            transition: opacity 1s ease 2s;
            white-space: nowrap;
        }}

        .gift-scene.opened .budget-info {{
            opacity: 1;
        }}

        /* Confetti */
        .confetti {{
            position: fixed;
            width: 15px;
            height: 15px;
            z-index: 1000;
        }}

        @keyframes confetti-fall {{
            to {{
                transform: translateY(100vh) rotate(720deg);
                opacity: 0;
            }}
        }}

        /* Firework particle */
        .firework-particle {{
            position: fixed;
            width: 8px;
            height: 8px;
            border-radius: 50%;
            z-index: 999;
        }}

        @keyframes explode {{
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
            margin-top: 50px;
            color: #ffd700;
            font-size: 1.3em;
            animation: pulse 2s infinite;
            opacity: 1;
            transition: opacity 0.5s;
        }}

        .tap-hint.hidden {{
            opacity: 0;
        }}

        @keyframes pulse {{
            0%, 100% {{
                opacity: 1;
                transform: scale(1);
            }}
            50% {{
                opacity: 0.6;
                transform: scale(1.05);
            }}
        }}

        @media (max-width: 600px) {{
            .welcome-text h1 {{
                font-size: 1.8em;
            }}

            .welcome-text p {{
                font-size: 1.1em;
            }}

            .gift-scene {{
                width: 200px;
                height: 250px;
            }}

            .box-base {{
                width: 200px;
                height: 150px;
            }}

            .box-base .front, .box-base .back {{
                width: 200px;
                height: 150px;
                transform: translateZ(100px);
            }}

            .box-base .back {{
                transform: rotateY(180deg) translateZ(100px);
            }}

            .box-base .left, .box-base .right {{
                width: 200px;
                height: 150px;
                transform: rotateY(-90deg) translateZ(100px);
            }}

            .box-base .right {{
                transform: rotateY(90deg) translateZ(100px);
            }}

            .box-lid {{
                width: 200px;
                bottom: 150px;
            }}

            .box-lid .top {{
                width: 200px;
                height: 200px;
            }}

            .box-lid .front, .box-lid .back, .box-lid .left, .box-lid .right {{
                width: 200px;
            }}

            .box-lid .front {{
                transform: translateZ(100px);
            }}

            .box-lid .back {{
                transform: rotateY(180deg) translateZ(100px);
            }}

            .box-lid .left {{
                transform: rotateY(-90deg) translateZ(100px);
            }}

            .box-lid .right {{
                transform: rotateY(90deg) translateZ(100px);
            }}

            .name-reveal {{
                font-size: 2em;
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
        <div class="gift-scene" id="giftScene" onclick="openGift()">
            <div class="box-lid" id="boxLid">
                <div class="bow">🎀</div>
                <div class="side top"></div>
                <div class="side front"></div>
                <div class="side back"></div>
                <div class="side left"></div>
                <div class="side right"></div>
            </div>

            <div class="box-base">
                <div class="ribbon vertical"></div>
                <div class="ribbon horizontal"></div>
                <div class="side front"></div>
                <div class="side back"></div>
                <div class="side left"></div>
                <div class="side right"></div>
                <div class="side bottom"></div>
            </div>

            <div class="name-reveal">{receiver}</div>
            <div class="budget-info">💰 Budget: $57 💰</div>
        </div>
    </div>

    <div class="tap-hint" id="tapHint">👆 Tap the gift to open!</div>

    <script>
        let opened = false;

        function openGift() {{
            if (opened) return;
            opened = true;

            const giftScene = document.getElementById('giftScene');
            const tapHint = document.getElementById('tapHint');

            // Hide tap hint
            tapHint.classList.add('hidden');

            // Open the box
            giftScene.classList.add('opened');

            // Start confetti immediately
            setTimeout(createConfetti, 500);

            // Start fireworks after lid opens
            setTimeout(createFireworks, 1000);
        }}

        function createConfetti() {{
            const colors = ['#ffd700', '#ff6b6b', '#4ecdc4', '#45b7d1', '#f38181', '#95e1d3', '#f38181'];
            const giftRect = document.getElementById('giftScene').getBoundingClientRect();
            const startX = giftRect.left + giftRect.width / 2;
            const startY = giftRect.top;

            for (let i = 0; i < 150; i++) {{
                setTimeout(() => {{
                    const confetti = document.createElement('div');
                    confetti.className = 'confetti';
                    confetti.style.left = startX + 'px';
                    confetti.style.top = startY + 'px';
                    confetti.style.backgroundColor = colors[Math.floor(Math.random() * colors.length)];

                    const angle = (Math.random() - 0.5) * Math.PI;
                    const velocity = 200 + Math.random() * 300;
                    const duration = 2 + Math.random() * 2;

                    confetti.style.animation = `confetti-fall ${{duration}}s ease-out forwards`;
                    confetti.style.setProperty('--angle', angle);

                    document.body.appendChild(confetti);

                    setTimeout(() => confetti.remove(), duration * 1000);
                }}, i * 20);
            }}
        }}

        function createFireworks() {{
            const colors = ['#ffd700', '#ff6b6b', '#4ecdc4', '#45b7d1', '#f38181', '#95e1d3', '#fff', '#ff1493'];

            function createFirework() {{
                const x = window.innerWidth * (0.2 + Math.random() * 0.6);
                const y = window.innerHeight * (0.1 + Math.random() * 0.4);

                for (let i = 0; i < 40; i++) {{
                    const particle = document.createElement('div');
                    particle.className = 'firework-particle';
                    particle.style.left = x + 'px';
                    particle.style.top = y + 'px';
                    particle.style.backgroundColor = colors[Math.floor(Math.random() * colors.length)];

                    const angle = (Math.PI * 2 * i) / 40;
                    const velocity = 80 + Math.random() * 120;
                    const dx = Math.cos(angle) * velocity;
                    const dy = Math.sin(angle) * velocity;

                    particle.style.setProperty('--x', dx + 'px');
                    particle.style.setProperty('--y', dy + 'px');
                    particle.style.animation = 'explode 1.2s ease-out forwards';

                    document.body.appendChild(particle);

                    setTimeout(() => particle.remove(), 1200);
                }}
            }}

            // Create 8 fireworks
            for (let i = 0; i < 8; i++) {{
                setTimeout(createFirework, i * 400);
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
