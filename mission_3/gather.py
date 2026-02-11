import subprocess
import json
import re

URL_VERIFY = "https://story.aidevs.pl/api-weryfikacja"
URL_KNOW = "https://story.aidevs.pl/api-wiedza"

# Using the full user agent and cookie from the working curl command (Step 210)
CURL_HEADERS = [
    "-H", "User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36",
    "-H", "Cookie: _ga=GA1.1.2029103482.1761218555; _fbp=fb.1.1761218557729.946284253240951193; datafast_visitor_id=49d08206-0dc4-46d9-9801-6bb8f807df9d; _cfuvid=opZ5dj.LM0EGJKRuCN2HY0ffMDIIRvTwXBCxEgACGHU-1768077009680-0.0.1.1-604800000; _gcl_au=1.1.271650624.1769006556; _clck=1ynkyn1%5E2%5Eg2w%5E0%5E2122; _rdt_uuid=1761218557745.8bb5988c-47cc-42e5-b91f-35cc6fd0d24b; _ga_S7BVC155E3=GS2.1.s1769006556$o15$g1$t1769006605$j11$l0$h0; PHPSESSID=vld9ev4m61vbg4ngl40ni17m8k",
    "-H", "Referer: https://story.aidevs.pl/mission/3"
]

def fetch_json(url):
    print(f"Fetching: {url}")
    cmd = ["curl", "-s"] + CURL_HEADERS + [url]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
        return json.loads(result.stdout)
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return None

def main():
    # 1. Get Questions
    print("--- Fetching Verification ---")
    ver_data = fetch_json(URL_VERIFY)
    
    if not ver_data:
        print("Failed to get verification data.")
        return
        
    questions = ver_data.get("pytania", [])
    print(f"Questions received: {len(questions)}")
    
    answers = []
    
    for i, q in enumerate(questions):
        print(f"\nQ{i+1}: {q}")
        
        # Simple Logic: Try longest words first?
        # Or try specific words?
        words = q.replace("?", "").replace(",", "").split()
        # Sort words by length descending
        candidates = sorted(words, key=len, reverse=True)
        
        hint = None
        for word in candidates[:3]: # Try top 3 longest words
            if len(word) < 4: continue # Skip short words
            
            # Simple handling for polish declension (very crude)
            term = word
            if term == "Marsie": term = "Mars"
            if term == "Księżycu": term = "Księżyc"
            
            print(f"  Trying keyword: {term}")
            knowledge = fetch_json(f"{URL_KNOW}/{term}")
            
            if knowledge and 'hint' in knowledge:
                hint = knowledge['hint']
                print(f"  GOT HINT: {hint}")
                break
            else:
                print(f"  No hint for '{term}'")
        
        if not hint:
            print("  FAILED TO FIND HINT")
            answers.append("UNKNOWN")
        else:
            # TODO: Extract answer from hint. For now, just store the hint to inspect.
            answers.append(f"HINT_FOUND: {hint[:50]}...")

if __name__ == "__main__":
    main()
