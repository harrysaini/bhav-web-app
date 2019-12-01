import React, { BaseSyntheticEvent } from 'react';
import './Top.css';
import StocksService from '../../services/stocks.service';
import { map } from 'lodash';
import LoadingSpinner from '../../_shared-components/LoadingSpinner';
import StocksTable from '../../_shared-components/StocksTable';

interface State {
  stocks: any[],
  isLoaded: boolean;
}

interface Props {
}

class Top extends React.Component<Props, State> {

  constructor(props: Props) {
    super(props);
    this.state = {
      stocks: [],
      isLoaded: false
    }

  }

  componentDidMount = async () => {
    try {
      const stocks = await StocksService.getTopStocks();
      this.setState({
        stocks,
        isLoaded: true
      });
    } catch(e) {
      alert(e.message);
    }
  }

  
  

  render() {

    if(!this.state.isLoaded) {
      return <LoadingSpinner />;
    }

    return (
      <div>
        <h3>Top stocks are: </h3>
        <br/>
        <div className='stocks'>
          <StocksTable stocks={this.state.stocks} />
        </div>
      </div>
    );
  }

}

export default Top;
