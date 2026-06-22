# 👻 Ghost File Cleaner

A lightweight Python utility that scans folders and detects "ghost files" — empty files, duplicates, and suspicious tiny files that are usually leftover junk.

## ⚡ What it does

- 🧻 Detects empty files (0 bytes)
- 👥 Finds duplicate files using SHA256 hashing
- 🧪 Flags unusually small files (likely logs or temp junk)
- 📁 Recursively scans all subfolders
- 🚫 Safe mode only (does NOT delete anything)

## 🧠 Concept

Most storage clutter is invisible “ghost data” — duplicate files, leftover logs, and empty placeholders.  
This tool helps visualize that hidden clutter in your system.

## 🛠️ How it works

- Uses `os.walk()` to traverse directories
- Uses `hashlib.sha256()` to identify duplicate files
- Categorizes files based on size and content

## 🚀 Usage

```bash
python ghost_cleaner.py
