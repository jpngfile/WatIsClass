import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';

class App extends Component {
  render() {
    return (
      <div className="App">
        <div className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <h2>Welcome to WatisClass</h2>
        </div>
        <p className="App-intro">
          To get started, edit <code>src/App.js</code> and save to reload.
        </p>
        <form>
          Class Name:<br />
          <input type="text" /> <br />
          # of pages:<br />
          <input type="text" />
          <input type="submit" value="Make Class" />
        </form>
        <form id="form">
          Class Code:<br />
          <input type="text" />
          <input type="submit" value="Join Class" />
        </form>
      </div>
    );
  }
}

export default App;
