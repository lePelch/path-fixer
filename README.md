# cli-arg-python

Tool for extracting and fixing Windows backup files on Linux.

This CLI takes files extracted from a Windows environment (with `\`-based paths),
repairs the directory structure, and recreates a correct Linux-compatible
hierarchy.

---

## Features

- Fixes Windows-style paths (`\`) into proper Linux directories
- Recreates empty directory trees when needed
- Works on already-extracted backups
- Simple and explicit command-line interface

---

## Installation

### From source (development)
```bash
git clone https://github.com/lePelch/cli-arg-python.git
cd cli-arg-python
makepkg -si
