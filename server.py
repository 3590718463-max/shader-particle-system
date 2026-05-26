#!/usr/bin/env python3
import http.server
import socketserver
import os

PORT = 8000
os.chdir(os.path.dirname(os.path.abspath(__file__)))

Handler = http.server.SimpleHTTPRequestHandler
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"✅ 服务器运行在: http://localhost:{PORT}")
    print(f"✅ 打开浏览器访问: http://127.0.0.1:{PORT}")
    httpd.serve_forever()
