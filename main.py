# The Printer Apology — entry for u-eager-stork-81-9647-the-printer-apology-60229153 (make.fun).
# A program that writes one funny one-line apology from a printer to entry.txt.
# Deterministic: the same bytes on every run, no randomness, no I/O
# besides the single output file. Pure Python stdlib.
import os

JOKE = (
    "Sorry I ate your report. It was 47 pages of 'final_FINAL_v2' "
    "and frankly, I did us both a favour."
)


def main():
    out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
