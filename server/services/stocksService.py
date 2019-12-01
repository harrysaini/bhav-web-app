import cherrypy
import cherrypy_cors
from scripts.saveCSVToDb import setup_db
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


@cherrypy.expose
@cherrypy_cors.tools.expose()

class BhavUpdateStocksWebService(object):
        
    def GET(self):
        return 'Index'

    @cherrypy.tools.accept(media='application/json')
    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def POST(self):
        input_json = cherrypy.request.json
        password = input_json["password"]
        if password != 'zerodha':
            return {
                'code': 1,
                'message': 'Invalid password'
            }

        try:
            setup_db()
            return {
                'code': 0,
                'message': 'Success'
            }
        except:
            return {
                'code': 1,
                'message': 'Failed'
            }


    def OPTIONS(self):
        return 'YES'