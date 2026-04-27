import requests

url = "https://sm2a.staging.earth.gov/api/v1/dags/example/clearTaskInstances"

print(f"[*] Extracting Raw Headers via OPTIONS: {url}")

try:
    r = requests.options(url, timeout=10)
    print(f"\n[+] Status Code: {r.status_code}")
    print("--- [ Response Headers ] ---")
    for key, value in r.headers.items():
        print(f"{key}: {value}")
    
    # ఒకవేళ 'Allow' హెడర్ ఉంటే అది మనకు ఏ మెథడ్స్ వాడాలో చెబుతుంది
    if 'Allow' in r.headers:
        print(f"\n[!] Allowed Methods: {r.headers['Allow']}")

except Exception as e:
    print(f"[!] Error: {e}")
