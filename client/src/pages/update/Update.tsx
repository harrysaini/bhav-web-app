import React, { BaseSyntheticEvent } from 'react';
import StocksService from '../../services/stocks.service';

interface State {
  password: string;
  btnDisabled : boolean;
}
interface Props{}


class Update extends React.Component<Props, State> {

  constructor(props: Props) {
    super(props);
    this.state = {
      password: '',
      btnDisabled: false
    }

  }


  onSubmitButtonClick = async () => {
    if(!this.state.password) {
      return;
    }

    try {
      this.setState({
        btnDisabled: true
      });
      const status = await StocksService.updateStocks(this.state.password);
      alert("Updated successfully");
      this.setState({
        btnDisabled: false
      });
    } catch(e) {
      this.setState({
        btnDisabled: false
      });
      alert(e);
    }
  }





  render() {



    return (
      <div>
        <h3>Admin controls</h3>
        <br/>
        <br/>
        <div className='update'>
          <p>
            Enter password 'zerodha' to fetch latest data from BhavCopy site.<br/>
            Sync to db can take some time.
          </p>
          <div className="col-6 row mt-3 mb-3">
            <div className="col-12 mb-3">
              <input
                type="password"
                className="form-control"
                placeholder="Enter password"
                value={this.state.password}
                onChange= {(event) => {this.setState({password: event.target.value})}}
              />
            </div>
          <div className="col-12">
            <button
              className="btn btn-primary f-width"
              disabled={this.state.btnDisabled}
              onClick={this.onSubmitButtonClick}
            >
              Update
            </button>
          </div>

        </div>
        </div>
      </div>
    );
  }

}

export default Update;
