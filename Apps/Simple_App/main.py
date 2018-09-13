import os,datetime
import tornado.httpserver
import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
  def get(self):
    #self.write("Helo World")
    self.render('index.html')
    
class AboutHandler(tornado.web.RequestHandler):
  def get(self):
    #self.write("About Us")
    self.render('about.html')
  
class ContactHandler(tornado.web.RequestHandler):
  def get(self):
    #self.write("Contact Us")
    self.render('contact.html')
    
  def post(self):
    name = self.get_argument('name')
    email = self.get_argument('email')
    message = self.get_argument('message')
    created = datetime.datetime.now()
    self.write("Submitted Succesfully!")
      

def main():
  settings = dict(
    cookie_secret = str(os.urandom(45)),
    template_path = os.path.join(os.path.dirname(__file__),"templates"),
    static_path = os.path.join(os.path.dirname(__file__),"static"),
    xsrf_cookies = True,
    autoreload = True,
    gzip = True,
    debug = True,
    login_url = "/login",
    autoscape = None
  )
  app = tornado.web.Application([
    ("/",MainHandler),
    ("/about",AboutHandler),
    ("/contact",ContactHandler)
  ],**settings)
  
  http_server = tornado.httpserver.HTTPServer(app)
  port = 5000
  http_server.listen(port)
  tornado.ioloop.IOLoop.instance().start()

if __name__ == '__main__':
  main()

  
  