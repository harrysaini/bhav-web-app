import React from 'react';
import './App.css';
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link,
  Redirect,
} from "react-router-dom";
import Top from './pages/top/Top';
import LoadingSpinner from './_shared-components/LoadingSpinner';
import Search from './pages/search/Search';
import Update from './pages/update/Update';

interface Props {
}
interface State {
  isLoaded: boolean;
}
class App extends React.Component<Props, State> {

  constructor(props: Props) {
    super(props);
    this.state = {
      isLoaded: false
    }
  }

  componentDidMount = async () => {
    this.setState({
      isLoaded: true
    });
  }

  render() {

    return(
      <Router>
        <header className="App-header">
          <Link to= '/'><div className="logo">Bhav It</div></Link>
        </header>
        <div className='container'>
            {this.subRender()}
        </div>
        <footer className="text-center footer">
          by: Harish
        </footer>
    </Router>
    )
  }

  // render inner content of wrapper
  subRender(){

    if(!this.state.isLoaded) {
      return (
        <LoadingSpinner />
      );
    }

    return (
        <div className="App">
          <Switch>
            <Route exact path='/'>
              <div className="index-wrapper">
                <div className="text-center">
                  <br></br><br/><br/>
                  <h6>Bhav It</h6>
                  <p>See top stocks or search stock by name.</p>
                  <br></br>
                  <div className="link-btns col-6 m-auto">
                    <Link to='/top'>
                      <button type="button" className="btn btn-primary f-width">
                          Top Stocks
                      </button>
                    </Link>
                    <Link to='/search'>
                      <button type="button" className="btn btn-primary f-width">
                          Search/All Stocks
                      </button>
                    </Link>
                    <Link to='/update'>
                      <button type="button" className="btn btn-primary f-width">
                          Update Stocks
                      </button>
                    </Link>
                  </div>

                </div>
              </div>
            </Route>
            <Route exact path="/top">
              <Top />
            </Route>
            <Route exact path="/search">
              <Search />
            </Route>
            <Route exact path="/update">
              <Update />
            </Route>
            <Redirect from='*' to='/' />
          </Switch>
        </div>
    );
  }
}

export default App;
