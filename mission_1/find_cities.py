import re

def find_flower_cities():
    flowers = [
        "róża", "mak", "bez", "lilia", "tulipan", "fiołek", "stokrotka", 
        "chaber", "bratek", "irys", "krokus", "lawenda", "wrzos", "dalia", 
        "piwonia", "słonecznik", "aksamitka", "nagietek", "mieczyk", 
        "hiacynt", "konwalia", "koniczyna", "głóg", "lipa", "jawor", "dąb",
        "ostróżka", "sasanka", "zawilec", "niezapominajka", "storczyk"
    ]
    
    # Common two-word cities in Mazovia (or nearby)
    cities = [
        "Maków Mazowiecki", "Ostrów Mazowiecka", "Nowy Dwór Mazowiecki", 
        "Mińsk Mazowiecki", "Grodzisk Mazowiecki", "Tomaszów Mazowiecki",
        "Rawa Mazowiecka", "Wysokie Mazowieckie", "Biała Podlaska",
        "Bielsk Podlaski", "Sokołów Podlaski", "Radzyń Podlaski",
        "Janów Podlaski", "Konstancin-Jeziorna", "Góra Kalwaria",
        "Żelazowa Wola", "Podkowa Leśna", "Ożarów Mazowiecki",
        "Stare Babice", "Nowe Miasto", "Nowe Miasto Lubawskie",
        "Różan", "Wyszków", "Pułtusk", "Ostrołęka", "Przasnysz",
        "Ciechanów", "Mława", "Płońsk", "Sierpc", "Glinojeck"
    ]
    
    print("Checking cities for flowers:")
    for city in cities:
        city_lower = city.lower()
        parts = city_lower.replace("-", " ").split()
        
        # Check strict containment in words
        for flower in flowers:
            for part in parts:
                if flower in part:
                    print(f"City: {city} -> Match: {flower} in '{part}'")

if __name__ == "__main__":
    find_flower_cities()
