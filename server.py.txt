from http.server import BaseHTTPRequestHandler, HTTPServer
from app.controller import handle_request
import json

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.handle_method()

    def do_POST(self):
        self.handle_method()

    def handle_method(self):
        content_length = int(self.headers.get('Content-Length', 0))
        body = self.rfile.read(content_length).decode('utf-8') if content_length > 0 else ''
        status, response = handle_request(self.path, self.command, body)
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(response).encode())

def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    print('Servidor rodando em http://localhost:8000')
    httpd.serve_forever()

if __name__ == '__main__':
    run()
