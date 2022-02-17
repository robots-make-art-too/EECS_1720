import http.server
import socketserver

PORT = 3030 #8080, 8887, 8898,
Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer() as httpd:
	print("Hi you are at PORT: ", PORT)
  httpd.serve_forever()