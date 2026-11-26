"""What the Elevator Would Say — make.fun entry.

Reads the single elevator line from entry.txt (next to this file),
validates it against the bounty gate (1-120 characters, not only
whitespace), and prints it.
"""

from pathlib import Path
from typing import Optional

MAX_CHARS = 120
MIN_CHARS = 1


def load_entry() -> str:
    """Read the entry line from entry.txt beside this file."""
    entry_path = Path(__file__).with_name("entry.txt")
    raw = entry_path.read_text(encoding="utf-8")
    return raw.strip()


def validate_entry(line: str) -> str:
    """Enforce the bounty gate: 1-120 characters, not only whitespace."""
    if not line.strip():
        raise ValueError("entry is empty or only whitespace")
    if len(line) < MIN_CHARS or len(line) > MAX_CHARS:
        raise ValueError(
            f"entry is {len(line)} characters, must be {MIN_CHARS}-{MAX_CHARS}"
        )
    if any(ord(ch) < 0x20 and ch not in ("\t",) for ch in line):
        raise ValueError("entry contains control characters")
    if line.encode("utf-8").decode("utf-8") != line:
        raise ValueError("entry is not clean UTF-8 text")
    return line


def emit_entry(line: str, output_path: Optional[Path] = None) -> Path:
    """Write the validated line to /output/entry.txt for the judge.

    The bounty rules say the program writes one text to /output/entry.txt;
    printing alone is not enough, so the line goes to both places.
    """
    target = output_path or Path("/output/entry.txt")
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(line + "\n", encoding="utf-8")
    return target


def main() -> None:
    line = validate_entry(load_entry())
    emit_entry(line)
    print(line)


if __name__ == "__main__":
    main()
