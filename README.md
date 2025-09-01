# Task_06_Deep_Fake

This project transforms a data narrative about the **2024 Syracuse University Men’s Lacrosse season** into an AI-generated interview. It includes scripts for splitting the script into lines, generating synthetic voices with **pyttsx3**, and mixing them with **pydub** into a single audio file.  


Step-by-step workflow (how I built it)

1. Prepare the narrative & interview script

Extracted season stats from the PDF and wrote a short “street-interview” script (host + analyst).

Put the script in script/interview_script.md.

2. Split script into segments

code/split_script.py splits the markdown into per-line text files (audio/segments/host_001.txt etc.).

This makes it easy to apply different voices, pauses, or edits per segment.

3. Generate synthetic voice audio

Local (recommended): pyttsx3 (offline) to generate .wav segments with two distinct system voices.

Alternative (cloud): gTTS for simple online TTS that outputs .mp3 (useful when running on non-Windows or if a specific voice is needed).

4. Mix segments into final interview audio

code/mixdown_pydub.py combines per-line .wav files, modest fades, and short pauses into audio/final_mix.wav.

pydub requires ffmpeg installed and on your PATH.

5. Create a deepfake video

Use the final mixed audio and a neutral/consented head image or avatar.

Tools tried: open-source lipsync tools such as Wav2Lip / SadTalker (recommended free options) or paid avatar services (better quality but subscription required).

Result: generated a short, 8-second deepfake video to demonstrate the workflow end-to-end.

6. Prompt engineering & fact-checking

Prompts and fact-check templates are in prompts/ (LLM polish prompts + “fact-check” prompts to prevent hallucinations).

Iterated prompts to force the LLM to cite only the provided stats and to avoid inventing historical comparisons.
