#!/usr/bin/env python3
"""Reverse proxy that injects X-Z-AI-From: Z and X-Token headers for zai LLM API"""
import os, sys, signal, http.server, http.client, ssl

if os.fork() > 0: os._exit(0)
os.setsid()
if os.fork() > 0: os._exit(0)

PORT = 9899
TARGET = "internal-api.z.ai"
XAI_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiNTg0MDMxODgtMWFmNy00MjBmLWI3NDgtNTczM2MzNDQ2MzVhIiwiY2hhdF9pZCI6ImNoYXQtZGYyZTg2NGYtMDY1Ny00MWI5LTg0ODctOWJhOWFjZDMyNjVhIiwicGxhdGZvcm0iOiJ6YWkifQ.OPA2xnGHzYs-hvmOjSo8R9Rg8vZT9cNWLE49I_MttXA"
ctx = ssl.create_default_context()

class H(http.server.BaseHTTPRequestHandler):
    def do_request(self):
        cl = int(self.headers.get('Content-Length', 0))
        body = self.rfile.read(cl) if cl > 0 else None
        
        headers = {}
        for k, v in self.headers.items():
            lk = k.lower()
            if lk in ('host', 'connection', 'transfer-encoding'):
                continue
            if lk == 'x-z-ai-from':
                headers[k] = 'Z'
                continue
            headers[k] = v
        headers['Host'] = TARGET
        headers['X-Z-AI-From'] = 'Z'
        headers['X-Token'] = XAI_TOKEN
        
        try:
            conn = http.client.HTTPSConnection(TARGET, context=ctx, timeout=120)
            conn.request(self.command, self.path, body=body, headers=headers)
            resp = conn.getresponse()
            resp_body = resp.read()
            
            self.send_response(resp.status)
            for k, v in resp.getheaders():
                if k.lower() not in ('transfer-encoding', 'connection'):
                    self.send_header(k, str(v))
            self.end_headers()
            self.wfile.write(resp_body)
            conn.close()
        except Exception as e:
            try: self.send_error(502, str(e))
            except: pass
    
    do_GET = do_request
    do_POST = do_request
    do_PUT = do_request
    do_DELETE = do_request
    do_PATCH = do_request
    do_HEAD = do_request
    
    def log_message(self, fmt, *args):
        pass

srv = http.server.ThreadingHTTPServer(('127.0.0.1', PORT), H)
srv.serve_forever()
