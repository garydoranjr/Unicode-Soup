import os.path

from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from backend.soup import soupify
from google.appengine.ext.webapp import template

template.register_template_library('common.my_filters')

class MainPage(webapp.RequestHandler):
    def get(self):
        path = static_page("index.html")
        args = dict()
        self.response.out.write(template.render(path, args))

class FacebookPost(webapp.RequestHandler):
    def post(self):
        soupy = self.request.get('soup')
        if not soupy:
            soupy = soupify(self.request.get('message'))
        path = static_page("post.html")
        args = dict(soup=soupy)
        self.response.out.write(template.render(path, args))

class Soupify(webapp.RequestHandler):
    def post(self):
        msg = self.request.get('message')
        soupy = soupify(msg)
        path = static_page("soup.html")
        args = dict(message=msg, soup=soupy)
        self.response.out.write(template.render(path, args))

application = webapp.WSGIApplication(
                                     [('/', MainPage),
                                      ('/post', FacebookPost),
                                      ('/soup', Soupify)],
                                     debug=True)

def static_page(suffix):
    prefix = os.path.dirname(__file__)
    path = os.path.join(prefix, suffix)
    return path

def main():
    from google.appengine.ext.webapp.util import run_wsgi_app
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
