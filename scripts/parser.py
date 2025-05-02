import os
from pathlib import Path
import json
import re

RAW_DIR = "raw_docs"
OUTPUT_FILE = "parsed_data/speeches.json"
parsed = []

speaker_line_pattern = re.compile(r"^([А-ЯЉЊЂЋЏŠĐČĆŽ\s]+):\s*(.*)$")

for filepath in Path(RAW_DIR).rglob("*.txt"):
    print(f"Processing {filepath}...")
    with open(filepath, "r", encoding="utf-8") as f:
        lines = f.readlines()

    current_speaker = None
    current_speech = []

    for line in lines:
        line = line.strip()
        if not line:
            continue

        match = speaker_line_pattern.match(line)
        if match:
            # Save previous speech
            if current_speaker and current_speech:
                parsed.append({
                    "file": filepath.name,
                    "speaker": current_speaker,
                    "speech": " ".join(current_speech).strip()
                })
                current_speech = []

            # New speaker and possible first line of their speech
            current_speaker = match.group(1).strip()
            first_line = match.group(2).strip()
            if first_line:
                current_speech.append(first_line)
        elif current_speaker:
            current_speech.append(line)

    # Save last speech in the file
    if current_speaker and current_speech:
        parsed.append({
            "file": filepath.name,
            "speaker": current_speaker,
            "speech": " ".join(current_speech).strip()
        })

# Save output
os.makedirs("parsed_data", exist_ok=True)
with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    json.dump(parsed, f, ensure_ascii=False, indent=2)

print(f"✅ Done! Extracted {len(parsed)} speeches.")
