import redis
import os

db_name = "bhav"
all_stocks = F"{db_name}:allStocks"
top_index  = F"{db_name}:topIndex"

host = os.environ.get('HOST', 'localhost')
port = os.environ.get('PORT', 6379)
password = os.environ.get('PASSWORD', None)

class RedisConn:

    def __init__(self):
        self.r =  redis.Redis(host=host, password=password, port=port, decode_responses=True)


    def save_stocks(self, stocks):
        self.r.flushdb()
        with self.r.pipeline() as pipe:
            for stock in stocks:
                key = F"{db_name}:stocks:{stock['SC_NAME']}"
                pipe.multi()
                pipe.hmset(key, stock)
                pipe.sadd(all_stocks, stock['SC_NAME'])
                pipe.execute()
        
        try:
            self.r.bgsave()
            print('stock saved')
        except:
            print('Already saved')

    def get_stocks_dicts(self, stocks_keys, isKey = False):
        top_stocks = []

        with self.r.pipeline() as pipe:
            for stock in stocks_keys:
                key = stock if isKey else  F"{db_name}:stocks:{stock}"
                pipe.hgetall(key)
                
            top_stocks = pipe.execute()
            
        return top_stocks

    def get_top_stocks(self, limit):
        stocks = self.r.sort(all_stocks, by=F"{db_name}:stocks:*->HIGH", start=0, num=limit, desc=True)
        return self.get_stocks_dicts(stocks)
    
    def search_by_query(self, query):
        key = F"{db_name}:stocks:*{query}*"
        stocks = self.r.keys(key)
        return self.get_stocks_dicts(stocks, True)
        

redisConnection = RedisConn()