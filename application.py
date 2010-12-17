import cgi

from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from backend.soup import soupify

class MainPage(webapp.RequestHandler):
    def get(self):
        self.response.out.write("""
          <html>
            <body>
              <form action="/convert" method="post">
                <div><textarea name="message" rows="3" cols="60"></textarea></div>
                <div><input type="submit" value="Soupify"></div>
              </form>
            </body>
          </html>""")


class Guestbook(webapp.RequestHandler):
    def post(self):
        msg = soupify(self.request.get('message'))
        self.response.out.write('<html><body><pre>')
        self.response.out.write(cgi.escape(msg))
        self.response.out.write('</pre></body></html>')

application = webapp.WSGIApplication(
                                     [('/', MainPage),
                                      ('/convert', Guestbook)],
                                     debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
