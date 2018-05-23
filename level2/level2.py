import os
import webapp2
from paste import httpserver
# from webapp2 import template
from jinja2 import Environment, FileSystemLoader

class MainPage(webapp2.RequestHandler):

  def render_template(self, filename, context={}):
    path = os.path.join(os.path.dirname(__file__), filename)
    jinjaEnv = Environment(
        loader=FileSystemLoader('./')
    )
    template = jinjaEnv.get_template(filename)
    self.response.out.write(template.render(path, context))
 
  def get(self):
    self.render_template('index.html')
 
application = webapp2.WSGIApplication([ ('.*', MainPage) ], debug=False)

def main():
  httpserver.serve(application, host='127.0.0.1', port='8008')

if __name__ == '__main__':
  main()