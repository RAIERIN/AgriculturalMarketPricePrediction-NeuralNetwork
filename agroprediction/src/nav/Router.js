import React from 'react';
import { Stack, Scene, Router } from 'react-native-router-flux';
import SplashScreen from '../screens/SplashScreen';
import Login from '../screens/Login';
import Signup from '../screens/Signup';
import Home from '../screens/Home';
import DailyPrice from '../screens/DailyPrice';
import VegetablePrediction from '../screens/VegetablePrediction';
import Main from '../screens/Main';


const RouterComponent = () => {
  return (
    <Router>
      <Stack key="root">
          <Scene key="splashScreen" component={SplashScreen} hideNavBar initial />
          <Scene key="login" component={Login} hideNavBar />
          <Scene key="signup" component={Signup} hideNavBar />
          <Scene key="homePage" component={Home} hideNavBar />
          <Scene key="home" component={Main} hideNavBar />
          <Scene key="dailyRate" component={DailyPrice} hideNavBar />
          <Scene key="vegpredict" component={VegetablePrediction} hideNavBar />
      </Stack>
    </Router>
  );
};

export default RouterComponent;
