import requests

url = "https://sm2a.staging.earth.gov/api/v1/variables"

# ఖాళీ డేటాతో POST చేసి చూద్దాం
try:
    response = requests.post(url, json={}, timeout=10)
    print(f"Status Code: {response.status_code}")
    print("Full Response Data:")
    print(response.text)
except Exception as e:
    print(f"Error: {e}")
