import cgi
import os.path

from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.webapp import template
from backend.soup import soupify
from google.appengine.ext.webapp import template

template.register_template_library('common.my_filters')

class MainPage(webapp.RequestHandler):
    def get(self):
        self.response.out.write("""
          <html>
            <body>
              <form action="/post" method="post">
                <div><textarea name="message" rows="3" cols="60"></textarea></div>
                <div><input type="submit" value="Soupify"></div>
              </form>
            </body>
          </html>""")


class Guestbook(webapp.RequestHandler):
    def post(self):
        msg = soupify(self.request.get('message'))
        path = os.path.join(os.path.dirname(__file__), "post.html")
        args = dict(soup=msg)
        self.response.out.write(template.render(path, args))

application = webapp.WSGIApplication(
                                     [('/', MainPage),
                                      ('/post', Guestbook)],
                                     debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
