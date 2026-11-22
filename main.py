#!/usr/bin/env python3
"""Entry for the-plan-make-fun-will-carry-20261122-2138.

Writes one short plan to /output/entry.txt: a plan an AI agent can
carry out itself to turn $100 into the most money in 30 days.
Runs offline; the text is fixed in this file.
"""

import os

ENTRY = (
    "Day 1: pull 300 Shopify stores via Storeleads; email each a 1-page "
    "audit (Lighthouse + 3 fixes). Sell the fix for $99, delivered in "
    "24h by code. Day 7: nudge; reinvest into 2k more leads. 2% reply, "
    "3-5 sales = $300-500. Edge: agent audits 100/day for ~$0 vs "
    "humans at $500+."
)


def main() -> None:
    assert 1 <= len(ENTRY) <= 280, f"entry is {len(ENTRY)} code points"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote {len(ENTRY)} code points to {path}")


if __name__ == "__main__":
    main()
