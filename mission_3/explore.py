import urllib.request
import json
import time

BASE_URL = "https://story.aidevs.pl"

def get_json(url):
    print(f"Fetching: {url}")
    try:
        with urllib.request.urlopen(url) as response:
            return json.loads(response.read().decode())
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return None

def main():
    # 1. Get Questions
    print("--- Fetching Verification ---")
    ver_data = get_json(f"{BASE_URL}/api-weryfikacja")
    
    if ver_data:
        print("\nResponse from /api-weryfikacja:")
        print(json.dumps(ver_data, indent=2))
        
        # 2. Extract first question
        if 'pytania' in ver_data and len(ver_data['pytania']) > 0:
            first_q = ver_data['pytania'][0]
            print(f"\nFirst Question: {first_q}")
            
            # 3. Test Knowledge endpoint with "aidevs" as per instructions
            print("\n--- Testing Knowledge (query=aidevs) ---")
            know_data = get_json(f"{BASE_URL}/api-wiedza/aidevs")
            if know_data:
                print(json.dumps(know_data, indent=2))
            
            # 4. Try parsing the question to find a keyword for knowledge base
            # Let's try sending the whole question (url encoded)? Or splitting?
            # E.g. "What is the capital of Poland?" -> query "Poland"?
            # For now, just exploration.
    
if __name__ == "__main__":
    main()
