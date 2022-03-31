import http.server
import socketserver

PORT = 3030 #8080, 8887, 8898,
Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
  print("Hi you are at PORT: ", PORT)
  httpd.serve_forever()

# might need to install pip dependencies pip3/pip install --something to install goes here--
# python server.py
# change the PORT number above if you need to