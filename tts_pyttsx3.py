import pyttsx3
from pathlib import Path
import os

# Input and output directories
IN_DIR = Path("audio/segments")
OUT_DIR = Path("audio/segments")
OUT_DIR.mkdir(parents=True, exist_ok=True)

# Initialize TTS engine
engine = pyttsx3.init()
voices = engine.getProperty("voices")

# Pick two different voices if available
host_voice = voices[0].id if voices else None
analyst_voice = voices[1].id if len(voices) > 1 else host_voice

# Queue all text files first
for txt_path in sorted(IN_DIR.glob("*.txt")):
    name = txt_path.stem
    role = name.split("_")[0]  # determines host or analyst
    wav_path = OUT_DIR / f"{name}.wav"

    text = txt_path.read_text(encoding="utf-8")
    
    # Set voice and rate based on role
    if role == "host" and host_voice:
        engine.setProperty("voice", host_voice)
        engine.setProperty("rate", 165)
    elif role == "analyst" and analyst_voice:
        engine.setProperty("voice", analyst_voice)
        engine.setProperty("rate", 150)
    
    engine.save_to_file(text, str(wav_path))
    print(f"Queued: {wav_path}")

# Run once after queueing all files
engine.runAndWait()
print(f"✅ Generated {len(list(IN_DIR.glob('*.txt')))} audio segments in '{OUT_DIR}'")
