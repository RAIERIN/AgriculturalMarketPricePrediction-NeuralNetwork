import React, { Component } from 'react';
import firebase from 'firebase';
import { Provider } from 'react-redux';
import { createStore, applyMiddleware } from 'redux';
import ReduxThunk from 'redux-thunk';
import Router from './nav/Router';
import reducers from './reducers';

class App extends Component {
  componentWillMount() {
  const config = {
    apiKey: "AIzaSyA4nROn-JiQ1h1SkzlNnvBjYJ3acnrXx2Q",
    authDomain: "agroprediction.firebaseapp.com",
    databaseURL: "https://agroprediction.firebaseio.com",
    projectId: "agroprediction",
    storageBucket: "agroprediction.appspot.com",
    messagingSenderId: "1091862130218"
   };
   firebase.initializeApp(config);
  }
  render() {
    const store = createStore(reducers, {}, applyMiddleware(ReduxThunk));
    return (
      <Provider store={store}>
        <Router />
      </Provider>
    );
  }
}

export default App;
