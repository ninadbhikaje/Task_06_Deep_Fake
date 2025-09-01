from pydub import AudioSegment
from pathlib import Path

SEG_DIR = Path("audio/segments")
OUT = Path("audio/final_mix.wav")

sil_300 = AudioSegment.silent(duration=300)
sil_600 = AudioSegment.silent(duration=600)

mix = AudioSegment.silent(duration=0)

# Separate host and analyst files
host_files = sorted([f for f in SEG_DIR.glob("host_*.wav")])
analyst_files = sorted([f for f in SEG_DIR.glob("analyst_*.wav")])

# Mix in proper sequence: host 1 -> analyst 1 -> host 2 -> analyst 2 ...
for i in range(max(len(host_files), len(analyst_files))):
    if i < len(host_files):
        clip = AudioSegment.from_wav(host_files[i])
        clip = clip.fade_in(10).fade_out(10)
        mix += clip
        mix += sil_300
    if i < len(analyst_files):
        clip = AudioSegment.from_wav(analyst_files[i])
        clip = clip.fade_in(10).fade_out(10)
        mix += clip
        mix += sil_300

# Add final silence
mix += sil_600

# Export final mix
mix.export(OUT, format="wav")
print("Exported:", OUT)
