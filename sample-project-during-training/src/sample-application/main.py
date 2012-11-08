#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import cgi

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')

class FormHandler(webapp2.RequestHandler):
    def get(self):
   
        self.response.write("""
        <html>
        <body>
            <form action='/login' method='post'>
                <div><textarea name='content' rows='3' col='160'></textarea> </div>
                <br/>
                <input type='submit' value='Sign in'>
        </html>
        <body/>
        """)
        
class GuestBook(webapp2.RequestHandler):
    def post(self):
        self.response.write("<html> <body><b>You Have Write</b> <br/>")
        self.response.write(cgi.escape(self.request.get('content')))
        self.response.write("</body></html>")

app = webapp2.WSGIApplication([
    ('/form', FormHandler),('/login', GuestBook),
], debug=True)
