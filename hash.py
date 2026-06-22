import os
import hashlib

def file_hash(path):
    """Return SHA256 hash of a file."""
    h = hashlib.sha256()
    try:
        with open(path, "rb") as f:
            while chunk := f.read(8192):
                h.update(chunk)
        return h.hexdigest()
    except:
        return None


def scan_folder(folder):
    hashes = {}
    empty_files = []
    duplicates = []
    weird_files = []

    for root, _, files in os.walk(folder):
        for file in files:
            path = os.path.join(root, file)

            try:
                size = os.path.getsize(path)

                # Empty file detection
                if size == 0:
                    empty_files.append(path)
                    continue

                # "Weird small files" (likely junk/logs)
                if size < 50:
                    weird_files.append(path)

                h = file_hash(path)
                if h:
                    if h in hashes:
                        duplicates.append((path, hashes[h]))
                    else:
                        hashes[h] = path

            except:
                continue

    return empty_files, duplicates, weird_files


def report(folder):
    empty, dupes, weird = scan_folder(folder)

    print("\n👻 GHOST FILE ANALYSIS REPORT\n")

    print("🧻 Empty Files:")
    for f in empty:
        print(" -", f)

    print("\n👥 Duplicate Files:")
    for f1, f2 in dupes:
        print(f" - {f1}  ↔  {f2}")

    print("\n🧪 Weird Tiny Files (<50 bytes):")
    for f in weird:
        print(" -", f)

    print("\nDone. Files classified, not deleted.")


if __name__ == "__main__":
    path = input("Enter folder path to scan: ")
    report(path)
