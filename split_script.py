from pathlib import Path

SRC = Path("C:/Users/ninad/Downloads/code/script/interview_script.md")
OUT = Path("audio/segments")
OUT.mkdir(parents=True, exist_ok=True)

roles = []
with SRC.open(encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if line.startswith("HOST:"):
            roles.append(("host", line.replace("HOST:", "").strip()))
        elif line.startswith("ANALYST:"):
            roles.append(("analyst", line.replace("ANALYST:", "").strip()))

host_idx = analyst_idx = 1
for role, text in roles:
    idx = host_idx if role == "host" else analyst_idx
    fname = OUT / f"{role}_{idx:03d}.txt"
    fname.write_text(text, encoding="utf-8")
    if role == "host":
        host_idx += 1
    else:
        analyst_idx += 1

print(f"Wrote {len(roles)} text segments to {OUT}")
