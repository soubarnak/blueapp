#!/usr/bin/env python3
"""
Web Server for PC Remote Control Demo
Serves the web interface and handles demo requests
"""

import http.server
import socketserver
import os
import webbrowser
from urllib.parse import urlparse, parse_qs

class RemoteControlHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = '/web_interface.html'
        return super().do_GET()
    
    def do_POST(self):
        # Handle demo commands (for demonstration only)
        if self.path == '/api/command':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            
            # Demo response
            response = '{"status": "demo", "message": "This is a demonstration. Use the Android app for actual control."}'
            self.wfile.write(response.encode())
        else:
            self.send_error(404)

def main():
    PORT = 5000
    
    print("=== PC Remote Control Web Server ===")
    print(f"Starting web server on port {PORT}")
    print(f"Open your browser to: http://localhost:{PORT}")
    print("Press Ctrl+C to stop the server")
    
    with socketserver.TCPServer(("0.0.0.0", PORT), RemoteControlHandler) as httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServer stopped by user")

if __name__ == "__main__":
    main()