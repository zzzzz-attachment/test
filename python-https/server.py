import http.server
import ssl

# Define the handler
class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Hello, HTTPS World!")

# Define the server
server_address = ('', 4443)  # Listen on port 4443
httpd = http.server.HTTPServer(server_address, MyHandler)

# Create an SSL context
context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(certfile="cert.pem", keyfile="key.pem")  # Paths to your certificate and key

# Wrap the socket with SSL
httpd.socket = context.wrap_socket(httpd.socket, server_side=True)

print("Serving on https://localhost:4443")
httpd.serve_forever()
