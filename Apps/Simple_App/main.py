import os
import tornado.httpserver
import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
  def get(self):
    self.write("Helo World")
    
class AboutHandler(tornado.web.RequestHandler):
  def get(self):
    self.write("About Us")
  
class ContactHandler(tornado.web.RequestHandler):
  def get(self):
    self.write("Contact Us")

def main():
  app = tornado.web.Application([
    ("/",MainHandler),
    ("/about",AboutHandler),
    ("/contact",ContactHandler)
  ])
  
  http_server = tornado.httpserver.HTTPServer(app)
  port = 5000
  http_server.listen(port)
  tornado.ioloop.IOLoop.instance().start()

if __name__ == '__main__':
  main()

  