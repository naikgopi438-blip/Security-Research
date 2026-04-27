import json

# JSON ఫైల్ ని లోడ్ చేయడం
with open('formatted_leak.json', 'r') as f:
    data = json.load(f)

def find_sensitive(obj, path=""):
    if isinstance(obj, dict):
        for k, v in obj.items():
            new_path = f"{path}/{k}"
            # ఇక్కడ మనం సెన్సిటివ్ కీస్ ని వెతుకుతున్నాం
            if k in ["jcr:createdBy", "userIdentifier", "sling:resourceType", "jcr:lastModifiedBy"]:
                print(f"FOUND: {new_path} -> {v}")
            find_sensitive(v, new_path)
    elif isinstance(obj, list):
        for i, item in enumerate(obj):
            find_sensitive(item, f"{path}[{i}]")

print("--- Deep Analysis Starting ---")
find_sensitive(data)
