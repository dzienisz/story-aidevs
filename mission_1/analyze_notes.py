
import os

files_order = [
    ("zasiane.txt", "10:28"),
    ("slowa.txt", "10:37"),
    ("dawno.txt", "10:40"),
    ("lipa.txt", "10:41"),
    ("trach.txt", "10:48"),
    ("pamiec.txt", "10:50"),
    ("fabryka.txt", "10:53"),
    ("czas.txt", "11:15"),
    ("wizja.txt", "11:18")
]

base_path = "mission_1"

print("--- ANALIZA NOTATEK W KOLEJNOŚCI CHRONOLOGICZNEJ ---\n")

for filename, time in files_order:
    path = os.path.join(base_path, filename)
    try:
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read().strip()
            print(f"=== {filename} ({time}) ===")
            print(content)
            print("\n")
    except Exception as e:
        print(f"Error reading {filename}: {e}")
