import os, os.path
import random
import string
import cherrypy
from services.stocksService import BhavWebAppWebService


class BhavWebApp(object):
    @cherrypy.expose
    def index(self):
        return open('index.html')



def start_server():
    conf = {
        '/': {
            'tools.sessions.on': True,
            'tools.staticdir.root': os.path.abspath(os.getcwd())
        },
        '/top': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.response_headers.on': True,
            'tools.response_headers.headers': [('Content-Type', 'application/json')],
        },
        '/static': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': './public'
        }
    }

    webapp = BhavWebApp()
    webapp.top = BhavWebAppWebService()
    cherrypy.quickstart(webapp, '/', conf)