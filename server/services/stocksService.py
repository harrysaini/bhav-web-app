import cherrypy
from scripts.redisConn import redisConnection

@cherrypy.expose
class BhavTopStocksWebService(object):
    
    @cherrypy.tools.json_out()
    def GET(self):
        return redisConnection.get_top_stocks(10)


@cherrypy.expose
class BhavSearchStocksWebService(object):
    
    @cherrypy.tools.json_out()
    def GET(self, query=''):
        query = query.lower()
        return redisConnection.search_by_query(query)