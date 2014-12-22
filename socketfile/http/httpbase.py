# -*- coding: utf-8 -*-
"""
Created on 2014/12/15
@author: LEO
"""


from BaseHTTPServer import BaseHTTPRequestHandler
import cgi

class   PostHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD':'POST',
                     'CONTENT_TYPE':self.headers['Content-Type'],
                     }
        )
        self.send_response(200)
        self.end_headers()
        self.wfile.write('Client: %sn ' % str(self.client_address) )
        self.wfile.write('User-agent: %sn' % str(self.headers['user-agent']))
        self.wfile.write('Path: %sn'%self.path)
        self.wfile.write('Form data:n')
        for field in form.keys():
            field_item = form[field]
            filename = 'C:http.txt'#field_item.filename
            filevalue  = field_item.value
            filesize = len(filevalue)#文件大小(字节)
            print len(filevalue)
            with open(filename,'wb') as f:
                f.write(filevalue)
        return
if __name__=='__main__':
    from BaseHTTPServer import HTTPServer
    sever = HTTPServer(('localhost',8080),PostHandler)
    print 'Starting server, use <Ctrl-C> to stop'
    sever.serve_forever()



if __name__ == '__main__':
    pass
