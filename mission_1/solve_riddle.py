import os
import re

def analyze_files():
    base_path = "mission_1"
    files = [f for f in os.listdir(base_path) if f.endswith(".txt")]
    
    # Sort files by some logic if needed, but let's just read all
    # Or use the timeline order I found earlier
    timeline_order = {
        "zasiane.txt": "10:28",
        "slowa.txt": "10:37",
        "dawno.txt": "10:40",
        "lipa.txt": "10:41",
        "trach.txt": "10:48",
        "pamiec.txt": "10:50",
        "fabryka.txt": "10:53",
        "czas.txt": "11:15",
        "wizja.txt": "11:18"
    }
    
    sorted_files = sorted(files, key=lambda x: timeline_order.get(x, "99:99"))
    
    flowers = [
        "róża", "mak", "bez", "lilia", "tulipan", "fiołek", "stokrotka", 
        "chaber", "bratek", "irys", "krokus", "lawenda", "wrzos", "dalia", 
        "piwonia", "słonecznik", "aksamitka", "nagietek", "mieczyk", 
        "hiacynt", "konwalia", "koniczyna", "głóg", "lipa", "jawor", "dąb"
    ]
    
    cities_db = [
        "Maków Mazowiecki", "Ostrów Mazowiecka", "Różan", "Ciechanów", 
        "Przasnysz", "Pułtusk", "Wyszków", "Ostrołęka", "Mława", "Płońsk", 
        "Glinojeck", "Drobin", "Sierpc", "Bielsk", "Bielsk Podlaski",
        "Sokołów Podlaski", "Łomża", "Zambrów", "Węgrów", "Mińsk Mazowiecki",
        "Nowy Dwór Mazowiecki", "Legionowo", "Serock", "Nasielsk"
    ]

    print("--- ANALYSIS STARTED ---\n")

    for filename in sorted_files:
        path = os.path.join(base_path, filename)
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        print(f"File: {filename} ({timeline_order.get(filename, '??:??')})")
        
        # Look for flowers
        found_flowers = []
        for flower in flowers:
            if flower in content.lower():
                found_flowers.append(flower)
        if found_flowers:
            print(f"  [!] Found flower keywords: {found_flowers}")

        # Look for capitalized words (potential names) excluding start of sentences
        # Simple regex for capitalized words not at start of line
        # (This is rough, but helps spot names)
        cap_words = re.findall(r'(?<!^)(?<!\. )\b[A-ZŚĆŻŹŁÓ][a-zśćżźłóęą]+', content)
        # Filter out common words if needed, or just print distinct
        unique_caps = sorted(list(set(cap_words)))
        if unique_caps:
            print(f"  [!] Potential proper names: {unique_caps}")

        # Look for specific route numbers
        routes = re.findall(r'\b\d+\b', content)
        if routes:
            print(f"  [!] Numbers found: {routes}")

        print("-" * 30)

    print("\n--- HYPOTHESIS GENERATION ---")
    # Check for "Two Word" cities containing a flower stem
    potential_candidates = []
    for city in cities_db:
        parts = city.split()
        if len(parts) >= 2:
            stem = parts[0].lower()
            # Check if stem matches a flower start
            for flower in flowers:
                if flower in stem: # e.g. "mak" in "maków"
                    potential_candidates.append((city, flower))
    
    print("Cities matching 'Two words' AND 'Flower-like' criteria:")
    for city, flower in potential_candidates:
        print(f"  - {city} (matches flower: {flower})")

if __name__ == "__main__":
    analyze_files()
