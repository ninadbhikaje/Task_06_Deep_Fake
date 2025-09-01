# Task_06_Deep_Fake

This project transforms a data narrative about the **2024 Syracuse University Men’s Lacrosse season** into an AI-generated interview. It includes scripts for splitting the script into lines, generating synthetic voices with **pyttsx3**, and mixing them with **pydub** into a single audio file.  


**Step-by-step workflow (how I built it)**

1. Prepare the narrative & interview script

* Extracted season stats from the PDF and wrote a short “street-interview” script (host + analyst).

* Put the script in script/interview_script.md.

2. Split script into segments

* Code/split_script.py splits the markdown into per-line text files (audio/segments/host_001.txt etc.).

* This makes it easy to apply different voices, pauses, or edits per segment.

3. Generate synthetic voice audio

* Local (recommended): pyttsx3 (offline) to generate .wav segments with two distinct system voices.

* Alternative (cloud): gTTS for simple online TTS that outputs .mp3 (useful when running on non-Windows or if a specific voice is needed).

4. Mix segments into final interview audio

* Code/mixdown_pydub.py combines per-line .wav files, modest fades, and short pauses into audio/final_mix.wav.

* pydub requires ffmpeg installed and on your PATH.

5. Create a deepfake video

* Use the final mixed audio and a neutral/consented head image or avatar.

* Tools tried: open-source lipsync tools such as Wav2Lip / SadTalker (recommended free options) or paid avatar services (better quality but subscription required).

* Result: generated a short, 8-second deepfake video to demonstrate the workflow end-to-end.

6. Prompt engineering & fact-checking

* Prompts and fact-check templates are in prompts/ (LLM polish prompts + “fact-check” prompts to prevent hallucinations).

* Iterated prompts to force the LLM to cite only the provided stats and to avoid inventing historical comparisons.


**Files in this repository (important ones)**

README.md — this file (overview + run instructions)

Script/interview_script.md — the host/analyst dialogue

Prompts/ — templates for LLM polishing and fact-checking

Code/split_script.py — splits the script into segments

Code/tts_pyttsx3.py — local TTS generation script

Code/tts_gtts.py — alternative gTTS script 

Code/mixdown_pydub.py — concatenates audio segments into final mix

audio/segments/ — generated per-line audio files

audio/final_mix.wav — final combined interview audio

video/ — lipsynced output, short clip


**How to run locally (Windows)**

1. Clone the repo and open a terminal in the repo root.

2. Create & activate a virtual environment (recommended):

python -m venv venv
.\venv\Scripts\Activate.ps1   # PowerShell

3. Install Python dependencies:

pip install pyttsx3 pydub

4. Install ffmpeg and ensure it’s on your PATH:

Download from https://ffmpeg.org
 and add ...\ffmpeg\bin to PATH.

5. Split, synthesize, and mix:

python code/split_script.py
python code/tts_pyttsx3.py
python code/mixdown_pydub.py

6. Video (Google Gemini Veo): Open the Google Gemini Veo AI and write a prompt to convert your audio file into a video format.


**Challenges & bottlenecks (what I ran into)**
1. Environment restrictions (online notebooks)

* Online Jupyter environments blocked system installs (no root), so ffmpeg and other system dependencies couldn’t be installed. That prevented reliable pydub + mp3/wav conversion in the cloud. Mitigation: moved the workflow to a local VS Code environment.

2. Missing Python packages

* pyttsx3, gTTS, pydub not preinstalled. Installing them locally fixed the problem. In an online environment these packages can be installed, but system TTS drivers often aren’t available.

3. TTS library differences

* pyttsx3 is offline but voice quality depends on OS voices. gTTS is cloud-based and higher quality but requires internet and can produce only .mp3 (and sometimes rate-limits). I provided both options so the repo is flexible.

4. Empty or corrupt audio output

* Caused by mismatched file extensions or missing ffmpeg. I debugged by checking file sizes and ensuring pydub loaded the right formats (from_mp3 vs from_wav).

5. Video generation limitations

* Creating a longer, high-quality deepfake video required paid/cloud services or more compute than available locally. I generated an 8-second lipsync demo (to prove the pipeline), but couldn’t produce longer footage due to subscription/purchase/compute/finance constraints.

6. LLM hallucinations / factual drift

* When polishing script lines, the LLM sometimes invented stats. I added a fact-check prompt that forces answers to use only provided bullet notes and to flag unsupported text as UNVERIFIED.

7. Ethical considerations

* I avoided impersonating real people, used a synthetic/neutral voice and avatar, and clearly labeled the outputs as AI-generated. This is documented in the repo.


**Final output (what I produced)**

1. Audio interview: audio/final_mix.wav — a full interview audio file matching the scripted dialogue.

2. Deepfake video: One short test clip (Syracuse_Lacrosse_Season_Review.mp4) of 8 seconds demonstrating lipsync between the synthetic audio and a neutral avatar. I could not generate a longer video due to subscription/purchase/finance constraints (paid services or extra GPU time were required for longer/higher-quality output).


**Ethics, labeling, and responsible use**

1. All media are clearly labeled AI-generated / synthetic.

2. Do not use this repo to impersonate real individuals.

3. Use the code and assets only for educational or research purposes.

