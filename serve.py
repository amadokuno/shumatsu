# /Users/suzukifumiya/export/serve.py
from http.server import HTTPServer, SimpleHTTPRequestHandler
import os


class Handler(SimpleHTTPRequestHandler):
    def end_headers(self):
        # Godot 4 Web exportに必要なヘッダーを付与
        self.send_header("Cross-Origin-Opener-Policy", "same-origin")
        self.send_header("Cross-Origin-Embedder-Policy", "require-corp")
        super().end_headers()


if __name__ == '__main__':
    port = 8000
    print(f"Serving HTTP on 0.0.0.0 port {port} ...")
    # 0.0.0.0 でリッスンすることで外部（iPhone）からの接続を受け付ける
    server = HTTPServer(('0.0.0.0', port), Handler)
    server.serve_forever()