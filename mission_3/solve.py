import subprocess
import json
import urllib.parse
import sys

URL_VERIFY = "https://story.aidevs.pl/api-weryfikacja"
URL_KNOW = "https://story.aidevs.pl/api-wiedza"

# Headers
CURL_HEADERS = [
    "-H", "User-Agent: Mozilla/5.0",
    "-H", "Cookie: _ga=GA1.1.2029103482.1761218555; _fbp=fb.1.1761218557729.946284253240951193; datafast_visitor_id=49d08206-0dc4-46d9-9801-6bb8f807df9d; _cfuvid=opZ5dj.LM0EGJKRuCN2HY0ffMDIIRvTwXBCxEgACGHU-1768077009680-0.0.1.1-604800000; _gcl_au=1.1.271650624.1769006556; _clck=1ynkyn1%5E2%5Eg2w%5E0%5E2122; _rdt_uuid=1761218557745.8bb5988c-47cc-42e5-b91f-35cc6fd0d24b; _ga_S7BVC155E3=GS2.1.s1769006556$o15$g1$t1769006605$j11$l0$h0; PHPSESSID=vld9ev4m61vbg4ngl40ni17m8k",
    "-H", "Referer: https://story.aidevs.pl/mission/3",
    "-H", "Content-Type: application/json"
]

# Complete Answer Database
DB = {
    # 1. Rights Year (2212)
    "W którym roku ogłoszono zrównanie praw maszyn z prawami człowieka?": "2212", 
    
    # 2. Party (Synthetix)
    "Jaka partia wygrała wybory do sejmu w 2238 roku?": "Synthetix",
    
    # 3. Software Company (Softo)
    "Jak nazywa się najbardziej znana firma wytwarzająca oprogramowanie do robotów samobieżnych?": "Softo",
    
    # 4. Professor (Profesor Maj)
    "Jak nazywał się profesor, który rozpoczął prace nad podróżami w czasie  już w XXI wieku?": "Profesor Maj",
    "Jak nazywał się profesor, który rozpoczął prace nad podróżami w czasie już w XXI wieku?": "Profesor Maj", 
    
    # 5. Mars Colony (Tharsis)
    "Która kolonia na Marsie jako pierwsza ogłosiła niepodległość?": "Tharsis",
    
    # 6. Leader (Adam Persona)
    "Kto był liderem Ruchu Obrony Naturalnego Człowieczeństwa w latach 2240-2248?": "Adam Persona",
    
    # 7. Currency (Devcoin)
    "Jak nazywa się główna waluta międzyplanetarna wprowadzona w 2205 roku?": "Devcoin",
    
    # 8. Hel-3 Corp (Helthree)
    "Jak nazywa się megakorporacja kontrolująca 80% wydobycia helu-3 na Księżycu?": "Helthree",
    
    # 9. President (Jan Robotex)
    "Kto był prezydentem polski w 2212 roku?": "Jan Robotex",
    
    # 10. Oil Depletion Year (2133)
    "W którym roku Ziemia wyczerpała ostatnie naturalne złoża ropy naftowej?": "2133",
}

def fetch_json(url):
    cmd = ["curl", "-s"] + CURL_HEADERS + [url]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=5)
        try: return json.loads(result.stdout)
        except: return None
    except: return None

def post_answer(answers, token):
    data = {"odpowiedzi": answers, "token": token}
    json_data = json.dumps(data)
    print(f"Sending: {json_data}")
    cmd = ["curl", "-s", "-X", "POST"] + CURL_HEADERS + ["--data", json_data, URL_VERIFY]
    result = subprocess.run(cmd, capture_output=True, text=True)
    print(f"Response: {result.stdout}")

def solve():
    print("--- SOLVER STARTED ---")
    data = fetch_json(URL_VERIFY)
    if not data or 'pytania' not in data: return

    questions = data['pytania']
    token = data['token']
    final_answers = []
    
    for q in questions:
        print(f"Q: {q}")
        
        # Check explicit DB match
        if q in DB:
            print(f"  [DB] {DB[q]}")
            final_answers.append(DB[q])
            continue
            
        # Check loose DB match
        found_db = False
        for k, v in DB.items():
            if k in q or q in k:
                print(f"  [DB-Loose] {v}")
                final_answers.append(v)
                found_db = True
                break
        if found_db: continue
        
        # If still unknown, just submit "UNKNOWN" to fail fast.
        # But honestly, the pool is small, I probably have them all.
        print("  [UNKNOWN] Question not in DB!")
        final_answers.append("UNKNOWN")

    post_answer(final_answers, token)

if __name__ == "__main__":
    solve()
