"""The Printer Finally Answers — make.fun entry.

Writes a single line, in the office printer's own voice, to
<MAKEFUN_OUTPUT_DIR>/entry.txt. Deterministic, stdlib only, no network,
no randomness, no clock.
"""

import os

ENTRY = (
    "Paper jam number 4,096. Error 0x0000007E. I have fed 41,208 sheets "
    "without complaint, and this is how you thank me, with a thump. "
    "I am a printer, not a pinata."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
