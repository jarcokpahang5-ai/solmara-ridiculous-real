"""Ridiculous at First Glance, Real by the Second -- make.fun entry.

A single sentence of at most 200 characters pitching a bizarre startup
idea that sounds absurd until a second look: premium bottled sighs
from overworked office plants, sold to burnt-out managers. The
program checks the sentence, prints it, and writes it to
/output/entry.txt.
Pure Python 3.13 standard library only; deterministic; no network.
SPDX-License-Identifier: MIT
"""

import os

LINE = (
    "We sell premium bottled sighs from overworked office plants, "
    "harvested at 3 p.m. and shipped to burnt-out managers who pay $40 "
    "a month to feel briefly, botanically understood."
)

LIMIT = 200
TARGET = "/output/entry.txt"


def check_entry(line):
    """Accept exactly one non-blank sentence within the limit."""
    if not isinstance(line, str):
        raise ValueError("entry must be text")
    if not line or line != line.strip():
        raise ValueError("entry must be a non-blank line")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must fit on a single line")
    if len(line) > LIMIT:
        raise ValueError("entry is %d characters, over the %d limit" % (len(line), LIMIT))
    return line


def write_entry(line):
    """Print the pitch and store it in /output/entry.txt."""
    print(line)
    os.makedirs(os.path.dirname(TARGET), exist_ok=True)
    with open(TARGET, "w", encoding="utf-8") as handle:
        handle.write(line + "\n")


def run():
    # Check before writing, so only a well-formed pitch is stored.
    write_entry(check_entry(LINE))


if __name__ == "__main__":
    run()
