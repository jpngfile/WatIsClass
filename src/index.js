import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';
import LecturePage from './LecturePage.js';
import registerServiceWorker from './registerServiceWorker';
import './index.css';

ReactDOM.render(<LecturePage />, document.getElementById('root'));
registerServiceWorker();
