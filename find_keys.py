import re
import os

# API కీలను గుర్తించడానికి Regex
key_pattern = r'([a-zA-Z0-9]{32,}|AIza[0-9A-Za-z-_]{35}|ghp_[a-zA-Z0-9]{36})'

path = './.cache/go-build/'

for root, dirs, files in os.walk(path):
    for file in files:
        full_path = os.path.join(root, file)
        try:
            with open(full_path, 'rb') as f:
                content = f.read().decode('utf-8', errors='ignore')
                matches = re.findall(key_pattern, content)
                for match in matches:
                    print(f"[!] Potential Key Found in {file}: {match}")
        except:
            continue
