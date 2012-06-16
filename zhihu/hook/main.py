import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from   redis import Redis
import json

from tornado.options import define,options

define("port", default=8989, help="port", type=int)
define("redis_host", default='localhost', help="redis_host", type=str)
define("redis_port", default=10000, help="redis_port", type=int)
define("redis_db", default=0, help="redis_db", type=int)

_client = None

def get_redis():
    global _client
    if not _client:
        _client = Redis(host = options.redis_host, port= options.redis_port, db = options.redis_db)
    return _client

def save(url, commit):
    cache = get_redis()
    cache.set(url, commit)

def load(url):
    cache = get_redis()
    return cache.get(url)

class UpdateHandler(tornado.web.RequestHandler):
    def get(self):
        self.process()
        
    def post(self):
        self.process()
        
    def process(self):
        self._parse_github_push()
        self.write("OK")

    def _parse_github_push(self):
        payload = self.get_argument('payload',None)
        obj = json.loads(payload)
        commit = obj["after"]
        url    = obj["repository"]["url"]
        save(url, commit)

class FetchHandler(tornado.web.RequestHandler):
    def get(self):
        self.process()
        
    def post(self):
        self.process()
        
    def process(self):
        url = self.get_argument('url',None)
        commit = load(url)
        self.write("OK_%s"%commit)

def main():
    tornado.options.parse_command_line()
    application = tornado.web.Application([
        (r"/update", UpdateHandler),
        (r"/fetch" , FetchHandler),
    ])
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()
    
