import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';
import ClassPage from './ClassPage.js';
import registerServiceWorker from './registerServiceWorker';
import './index.css';

ReactDOM.render(<ClassPage />, document.getElementById('root'));
registerServiceWorker();
