import os
import os.path
import random
import string
import cherrypy
import cherrypy_cors
from services.stocksService import BhavTopStocksWebService, BhavSearchStocksWebService, BhavUpdateStocksWebService

print("server starting up")
print(os.path.dirname(__file__))
client_dir = os.path.abspath(os.path.join(
    os.path.dirname(__file__), './../client/build/')) + '/'
print(client_dir)


def CORS():
    """Hook for adding the required CORS handlers."""

    cherrypy.response.headers["Access-Control-Allow-Origin"] = "*"
    cherrypy.response.headers["Access-Control-Allow-Methods"] = "POST GET HEAD"
    cherrypy.response.headers["Access-Control-Allow-Credentials"] = "true"
    cherrypy.response.headers["Access-Control-Allow-Headers"] = "Accept, Accept-Encoding, Content-Length, Content-Type, X-CSRF-Token"
    cherrypy.response.headers["Access-Control-Expose-Headers"] = "Accept, Accept-Encoding, Content-Length, Content-Type, X-CSRF-Token"


class BhavWebApp(object):
    @cherrypy.expose
    def default(self):
        return open(client_dir + 'index.html')


def start_server():
    conf = {
        '/': {
            'tools.sessions.on': True,
            'tools.staticdir.on': True,
            'tools.staticdir.dir': ''
        },
        '/api_search': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.response_headers.on': True,
            'tools.response_headers.headers': [('Content-Type', 'application/json')],
        },
        '/api_top': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.response_headers.on': True,
            'tools.response_headers.headers': [('Content-Type', 'application/json')],
        },
        '/api_update': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.response_headers.on': True,
            'tools.CORS.on': True,
        }
    }

    webapp = BhavWebApp()
    webapp.api_top = BhavTopStocksWebService()
    webapp.api_search = BhavSearchStocksWebService()
    webapp.api_update = BhavUpdateStocksWebService()
    cherrypy.tools.CORS = cherrypy.Tool("before_handler", CORS)
    cherrypy.config.update({
        'server.socket_host': '0.0.0.0',
        'server.socket_port': int(os.environ.get('PORT', 3000)),
        'tools.CORS.on': True,
        'log.screen': True,
        'tools.staticdir.debug': True,
        'tools.staticdir.root': client_dir,
        'environment': 'production',
        'engine.autoreload.on': False,
        'error_page.404': os.path.join(client_dir, "index.html")
    })

    cherrypy.tree.mount(webapp, '/', conf)
    cherrypy.engine.start()
