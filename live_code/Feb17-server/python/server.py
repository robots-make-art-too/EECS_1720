import http.server
import socketserver

PORT = 3030 #8080, 8887, 8898,
Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
  print("Hi you are at PORT: ", PORT)
  httpd.serve_forever()


# to run>: python3 server.py
# might have to install the imports
# pip/pip3 install http.server, socketserver
# 
