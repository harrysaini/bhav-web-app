import { config } from '../config';

const getTopStocksUrl = config.apiUrl + '/api_top';
const searchStocksUrl = config.apiUrl + '/api_search';
const updateStocksUrl = config.apiUrl + '/api_update';

class StocksService {

  static async getTopStocks(): Promise<any[]> {
    try {
      const resp = await fetch(getTopStocksUrl, {
        method: 'get'
      });

      const stocks = await resp.json();
      return stocks;
    } catch (e) {
      throw e;
    }
  }

  static async searchStocksByName(query: string):  Promise<any[]> {
    try {
      const url = `${searchStocksUrl}?query=${query}`
      const resp = await fetch(url, {
        method: 'get'
      });

      const stocks = await resp.json();
      return stocks;
    } catch (e) {
      throw e;
    }
  }

  static async updateStocks(password: string): Promise<any[]> {
    try {
      const resp = await fetch(updateStocksUrl, {
        method: 'post',
        body: JSON.stringify({
          password
        }),
        headers: {
          "Content-type": "application/json"
        }
      });

      const status = await resp.json();

      if(status.code != 0) {
        throw new Error(status.message);
      }
      return status;
    } catch (e) {
      throw e;
    }
  }

}

export default StocksService;
