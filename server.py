import http.server
import socketserver
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

class CleanURLHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Try the path as-is first, then with .html appended
        path = self.path.split('?')[0].split('#')[0]
        if '.' not in os.path.basename(path) and not path.endswith('/'):
            html_path = path + '.html'
            if os.path.isfile(self.translate_path(html_path)):
                self.path = html_path
        super().do_GET()

port = int(os.environ.get("PORT", 3001))
with socketserver.TCPServer(("", port), CleanURLHandler) as httpd:
    print(f"Serving on port {port}")
    httpd.serve_forever()
