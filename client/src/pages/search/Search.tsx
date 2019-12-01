import React, { BaseSyntheticEvent, Ref, RefObject } from 'react';
import StocksService from '../../services/stocks.service';
import LoadingSpinner from '../../_shared-components/LoadingSpinner';
import StocksTable from '../../_shared-components/StocksTable';

interface State {
  stocks: any[],
  isLoaded: boolean;
  searchBtnDisabled: boolean;
}

interface Props {
}

class Search extends React.Component<Props, State> {

  textInput: RefObject<HTMLInputElement>;

  constructor(props: Props) {
    super(props);
    this.state = {
      stocks: [],
      isLoaded: false,
      searchBtnDisabled: false
    }
    this.textInput = React.createRef();
  }

  componentDidMount = async () => {
    try {
      const stocks = await this.searchStocks('');
      this.setState({
        stocks: stocks,
        isLoaded: true
      });
    } catch(e) {
      console.log(e);
    }
  }

  searchStocks = async (query: string) => {
    try {
      const stocks = await StocksService.searchStocksByName(query);
      return stocks;
    } catch (e) {
      alert(e.message);
      throw e;
    }
  }

  onSearchButtonClick = async () => {
    this.setState({
      searchBtnDisabled: true,
      isLoaded: false
    });
    try {
      const query = (this.textInput && this.textInput.current && this.textInput.current.value) || '';
      const stocks = await this.searchStocks(query);
      this.setState({
        stocks: stocks,
        searchBtnDisabled: false,
        isLoaded: true
      });
    } catch (e) {
      this.setState({
        searchBtnDisabled: false,
        isLoaded: true
      });
    }
  }



  render() {


    return (
      <div className="search-wrapper">
        <h3>Search Stocks</h3>

        <div className="row mt-3 mb-3">
          <div className="col-8 col-md-10">
            <input
              type="text"
              className="form-control"
              placeholder="Search by stock name"
              ref={this.textInput}
            />
          </div>
          <div className="col-4 col-md-2">
            <button
              className="btn btn-primary m-0"
              onClick={this.onSearchButtonClick}
              disabled= {this.state.searchBtnDisabled}
            >
              Search
            </button>
          </div>

        </div>

        <h6>Search results are: </h6>
        <br />
        <div className='stocks'>
          { ! this.state.isLoaded ?
            (
            <LoadingSpinner />
            ) : (
              <StocksTable stocks={this.state.stocks} />
            )
          }
        </div>
      </div>
    );
  }

}

export default Search;
