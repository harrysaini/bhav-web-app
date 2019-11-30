import os, os.path
import random
import string
import cherrypy
from services.stocksService import BhavTopStocksWebService, BhavSearchStocksWebService

print("server starting up")
print(os.path.dirname(__file__))
client_dir = os.path.normpath(os.path.join(os.path.dirname(__file__), './../client/')) 
print(client_dir)

class BhavWebApp(object):
    @cherrypy.expose
    def index(self):
        return open(client_dir + '/index.html')





def start_server():
    conf = {
        '/': {
            'tools.sessions.on': True,
            'tools.staticdir.root': client_dir
        },
        '/search': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.response_headers.on': True,
            'tools.response_headers.headers': [('Content-Type', 'application/json')],
        },
        '/top': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.response_headers.on': True,
            'tools.response_headers.headers': [('Content-Type', 'application/json')],
        },   
        '/static': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': client_dir
        }
    }

    webapp = BhavWebApp()
    webapp.top = BhavTopStocksWebService()
    webapp.search = BhavSearchStocksWebService()
    cherrypy.quickstart(webapp, '/', conf)