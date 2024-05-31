from pathlib import Path
from typing import List


def tail(filepath: Path, n: int) -> List[str]:
    """
    Similate Unix' "tail -n" command:
    - Read in the file ("filepath").
    - Parse it into a list of lines, stripping trailing newlines.
    - Return the last "n" lines.
    """
    with open(filepath) as f:
        lines = [line.strip() for line in f]
        if n > len(lines):
            n = len(lines)
    return lines[-n:]
