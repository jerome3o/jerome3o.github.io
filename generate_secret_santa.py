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
    """Generate HTML page for a participant."""
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Secret Santa {year}</title>
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
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 20px;
        }}

        .container {{
            background: white;
            border-radius: 20px;
            padding: 50px;
            max-width: 600px;
            width: 100%;
            box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
            text-align: center;
        }}

        .snowflake {{
            font-size: 60px;
            margin-bottom: 20px;
        }}

        h1 {{
            color: #2d3748;
            font-size: 2.5em;
            margin-bottom: 20px;
            font-weight: normal;
        }}

        .greeting {{
            color: #4a5568;
            font-size: 1.3em;
            margin-bottom: 40px;
        }}

        .reveal-box {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            border-radius: 15px;
            padding: 40px;
            margin: 30px 0;
        }}

        .label {{
            color: rgba(255, 255, 255, 0.9);
            font-size: 1.1em;
            margin-bottom: 15px;
            text-transform: uppercase;
            letter-spacing: 2px;
        }}

        .receiver-name {{
            color: white;
            font-size: 2.5em;
            font-weight: bold;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.2);
        }}

        .message {{
            color: #4a5568;
            font-size: 1.1em;
            line-height: 1.6;
            margin-top: 30px;
        }}

        .footer {{
            margin-top: 40px;
            color: #718096;
            font-size: 0.9em;
        }}

        @media (max-width: 600px) {{
            .container {{
                padding: 30px 20px;
            }}

            h1 {{
                font-size: 2em;
            }}

            .receiver-name {{
                font-size: 2em;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="snowflake">🎄</div>
        <h1>Secret Santa {year}</h1>
        <p class="greeting">Hello, {giver}!</p>

        <div class="reveal-box">
            <div class="label">You are Secret Santa for:</div>
            <div class="receiver-name">{receiver}</div>
        </div>

        <p class="message">
            Remember to keep it secret! 🤫<br>
            Have fun finding the perfect gift! 🎁
        </p>

        <div class="footer">
            Happy Holidays! ❤️
        </div>
    </div>
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

    # Generate the pairing
    print("\n🎲 Generating Secret Santa pairings...")
    mapping = generate_cycle(PARTICIPANTS)

    # Verify it's a single cycle
    if not verify_single_cycle(mapping):
        print("❌ Error: Failed to generate a single cycle. Please run again.")
        return

    print("✅ Successfully generated a single cycle (no small loops!)")

    # Create output directory
    OUTPUT_DIR.mkdir(exist_ok=True)

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

    # Save mapping to JSON for reference (optional)
    mapping_file = OUTPUT_DIR / "mapping.json"
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
