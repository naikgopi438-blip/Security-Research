import requests

target = "https://sm2a.staging.earth.gov"
# Airflow లో కొన్ని పాత్స్ అథెంటికేషన్ అడగవు
paths = [
    "/static/app.js",
    "/static/manifest.json",
    "/api/v1/health",
    "/api/v1/version",
    "/api/v1/openapi.json"
]

print(f"[*] Starting Professional Audit on: {target}")

for path in paths:
    url = target + path
    try:
        r = requests.get(url, timeout=10)
        if r.status_code == 200:
            print(f"[+] POTENTIAL LEAK: {url} is OPEN!")
            if "json" in r.headers.get("Content-Type", ""):
                print(f"    Data Snippet: {r.text[:200]}")
        else:
            print(f"[-] Blocked: {path} (Status: {r.status_code})")
    except Exception as e:
        print(f"[!] Error: {e}")
