import React from 'react';
import { TabNavigator } from 'react-navigation';
import { Icon } from 'react-native-elements';

import Home from '../screens/Home';
import DailyPrice from '../screens/DailyPrice';
import VegetablePrediction from '../screens/VegetablePrediction';

export const Tabs = TabNavigator({
  Home: {
    screen: Home,
  },
  DailyPrice: {
    screen: DailyPrice,
  },
  VegetablePrediction: {
    screen: VegetablePrediction,
  },
},{
  tabBarPosition: 'bottom',
  swipeEnabled: true,
  lazyLoad: true,
  tabBarOptions: {
    activeTintColor: '#fff',
    inactiveTintColor: '#eee',
    showIcon: true,
    showLabel: true,
    animationEnabled: false,
    lazyLoad: true,
    style: {
    backgroundColor: '#0BDE8E',
    height: 60
  },
  labelStyle: {
    fontSize: 12,
    paddingBottom: 10
  }
  }
}
);
