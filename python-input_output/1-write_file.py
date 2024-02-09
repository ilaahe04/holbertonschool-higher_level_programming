#!/usr/bin/python3
"""Defines a text file-reading function."""


def write_file(filename="", text=""):
    """Print the contents of a UTF8 text file to stdout."""
    with open(filename, "w", encoding="utf-8") as f:
        txt = f.write(text)
        return txt
