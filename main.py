"""Write the one-line entry to $MAKEFUN_OUTPUT_DIR/entry.txt."""
import os
from pathlib import Path

LINE = "My agent asked a subagent to write this roast, then took credit for the punchline."
MAX_CHARS = 200

def main():
    assert "\n" not in LINE and len(LINE) <= MAX_CHARS
    out = Path(os.environ["MAKEFUN_OUTPUT_DIR"])
    out.mkdir(parents=True, exist_ok=True)
    (out / "entry.txt").write_text(LINE + "\n", encoding="utf-8")

if __name__ == "__main__":
    main()
