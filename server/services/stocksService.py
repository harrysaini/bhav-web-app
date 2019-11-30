import cherrypy
from scripts.redisConn import redisConnection

@cherrypy.expose
class BhavWebAppWebService(object):
    
    @cherrypy.tools.json_out()
    def GET(self):
        return redisConnection.get_top_stocks(10)