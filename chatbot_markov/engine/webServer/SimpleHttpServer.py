import http.server
import socketserver
import sys

print(sys.getdefaultencoding())
PORT = 8080
Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()

## 
# Reference: 
#   https://qiita.com/okhrn/items/4d3c74563154f191ba16
