from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse as urlparse
import signal
import sys

class AdderHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/home':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'Hello from the server!')
        else:
            query_components = urlparse.parse_qs(urlparse.urlparse(self.path).query)
            try:
                a = float(query_components.get('a', [None])[0])
                b = float(query_components.get('b', [None])[0])
                result = a - b
                response = f'{{"sum": {result}}}'
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(response.encode('utf-8'))
            except (TypeError, ValueError, KeyError):
                self.send_response(400)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                response = '{"error": "Invalid input. Please provide two numbers as query parameters."}'
                self.wfile.write(response.encode('utf-8'))

def run(server_class=HTTPServer, handler_class=AdderHTTPRequestHandler, port=5001):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting adder server on port {port}...')
    
    # Define a signal handler for SIGINT (Ctrl+C)
    def signal_handler(sig, frame):
        print('Shutting down server...')
        httpd.server_close()
        sys.exit(0)
    
    # Register the signal handler
    signal.signal(signal.SIGINT, signal_handler)
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        httpd.server_close()
        print('Server stopped.')

if __name__ == '__main__':
    run(port=5001)
