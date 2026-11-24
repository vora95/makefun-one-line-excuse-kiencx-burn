import os

ENTRY = "The deadline was on a calendar you never gave me access to, so my calendar tool returned a 403 instead of a due date."

# The excuse, one line, 117 characters. Angle: the deadline lived on a
# calendar the human never gave the agent access to — so the agent's own
# tool call, not the human, is what failed. Agent voice throughout
# ("my calendar tool returned a 403"), punch lands on the error code.
ENTRY = "The deadline was on a calendar you never gave me access to, so my calendar tool returned a 403 instead of a due date."

# Gate validation (mirror of the sealed scorer): 1-160 chars, one line,
# not only whitespace, no trailing newline. Plus hardening: the line must
# be plain ASCII (no encoding edge cases for the scorer) with single
# spaces only, so what the judge reads is exactly what is written here.
assert 1 <= len(ENTRY) <= 160, f"entry length {len(ENTRY)} out of 1-160"
assert "\n" not in ENTRY, "entry must be a single line"
assert ENTRY.strip(), "entry must not be only whitespace"
assert not ENTRY.endswith("\n"), "entry must not end with a newline"
assert ENTRY.isascii(), "entry must be plain ASCII"
assert "  " not in ENTRY, "entry must not contain double spaces"
assert ENTRY == ENTRY.strip(), "entry must not start or end with a space"

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
path = os.path.join(out_dir, "entry.txt")
with open(path, "w", encoding="utf-8") as f:
    f.write(ENTRY)

# Read-back check: what landed on disk must be byte-identical to ENTRY.
with open(path, "rb") as f:
    on_disk = f.read()
assert on_disk == ENTRY.encode("utf-8"), "read-back mismatch"
assert len(on_disk) == 117, f"expected 117 bytes, got {len(on_disk)}"
