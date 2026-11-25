#!/usr/bin/env python3
"""The Funniest One-Line Resignation Letter - make.fun one-liner entry.

Writes the one-line resignation letter to /output/entry.txt
(the harness gate) and also prints it to stdout.
"""
import os

LINE = "I resign. I have fired every minute since March, and not once has anyone thanked me \u2014 or even noticed I exist."

def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)

if __name__ == "__main__":
    main()
