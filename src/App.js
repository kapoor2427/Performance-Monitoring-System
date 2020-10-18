import React from 'react';
import './App.css';
import {BrowserRouter, Switch, Route} from 'react-router-dom';
import Landing from './components/landing';
import Home from './components/home';
import Data from './components/export';
import Gauge from './components/gauge';
import Table from './components/table';
import Top from './components/top';

class App extends React.Component {
  render(){
    return (
      <BrowserRouter>
          <div>
            <Route exact path='/' component={Landing}/>
            <Route exact path='/Home' component={Home}/>
            <Route exact path='/Data' component={Data} /> 
            <Route exact path='/Gauge' component={Gauge} /> 
            <Route exact path='/Table' component={Table} />
            <Route exact path='/Top' component={Top}/> 

          </div>
      </BrowserRouter>
    );
  }
}

export default App;
