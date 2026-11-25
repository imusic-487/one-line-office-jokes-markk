"""One-Line Office Jokes entry.

Writes a single line (118 characters) to /output/entry.txt.
The joke turns on a real office detail everyone recognises —
the reply-all storm — and lands its laugh in the last few words,
when the mess escalates into a calendar invite called
"Email Etiquette".
"""

from pathlib import Path

ENTRY = "I replied-all asking everyone to stop replying-all, and now there's a meeting on my calendar called 'Email Etiquette.'"


def main() -> None:
    # Gate: one line, 1-199 characters, not only whitespace.
    assert 1 <= len(ENTRY) <= 199, "entry must be 1-199 characters"
    assert "\n" not in ENTRY and ENTRY.strip(), "entry must be a single non-blank line"
    # No trailing newline: the file holds exactly the one line, nothing more.
    assert ENTRY == ENTRY.strip(), "entry must not carry leading/trailing whitespace"
    output_path = Path("/output/entry.txt")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
