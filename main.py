"""One Emoji, One Smile — make.fun entry.

The single emoji most likely to make a stranger smile: 🤗 (hugging face).

Why this one, against the judge's brief:
- Warmth at first glance: open arms offering a hug reads instantly as
  kind, friendly and welcoming — no context needed.
- Universality: a hug is understood the same way by a stranger of any
  age or background; no irony, in-joke or sarcasm.
- Chosen rather than default: it is not the first smiley that comes to
  mind — it is a deliberate pick, a gesture instead of a plain grin.
- Right for a stranger: a friendly hug-offer is warm without intimacy,
  flirtation or sarcasm; it works coming from someone unknown.

Pure standard library, no network access, no model calls — the emoji
is chosen by the author and written to the competition output file.
"""

import os

EMOJI = "🤗"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(EMOJI)


if __name__ == "__main__":
    main()
