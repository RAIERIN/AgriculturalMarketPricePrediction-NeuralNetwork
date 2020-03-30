import React, { Component } from 'react';
import Drawer from 'react-native-drawer';
import { Actions } from 'react-native-router-flux';
import axios from 'axios';
import { View, Dimensions, ScrollView, Text, Image, TouchableOpacity } from 'react-native';
import { Header } from '../components/common';
import TabNavigator from 'react-native-tab-navigator';

export default class Home extends Component {
  constructor(props) {
    super(props);
    this.state = { news:[] };
  }
  componentWillMount() {
    axios.get('http://192.168.43.250:5000/news')
      .then(response => this.setState({ news: response.data }));
  }
  static navigationOptions = {
    tabBarLabel:'News',
    tabBarIcon: ({tintColor}) => (
      <Image
        source={require('../images/news.png')}
        style ={{width:25, height:25, tintColor:'white'}}
        >
      </Image>
    )
  }
  News() {
    if (this.state.news.length >= 1){
      return this.state.news.map((data, i) => {
      return (
        <View key={i}>
          <View style={styles.newsContainer}>
            <View style={styles.newsHeader}>
              <Text style={{color: '#000000', fontSize: 24, fontWeight: '400'}}>{data.title}</Text>
            </View>
            <View style={styles.newsAuthorandDate}>
              <View style={styles.author}>
                <Text style={{color: '#000000', fontSize: 12, fontWeight: '200'}}> Author: {data.author}</Text>
              </View>
              <View style={styles.date}>
                <Text style={{color: '#000000', fontSize: 12, fontWeight: '200'}}>  Date:  {data.current_date}</Text>
              </View>
            </View>
            <ScrollView>
              <View style={styles.newsBody}>
                <Text style={{color: '#000000', fontSize: 14, fontWeight: '200', textAlignVertical: "center"}}>
                  {data.body}
                </Text>
              </View>
            </ScrollView>
          </View>
        </View>
      );
    });
  }
  }
  render() {
  return (
      <View style={styles.mainCointaner}>
        <Header>
          Agro Market News
        </Header>
        <ScrollView style={{ marginBottom: 85 }}>
          {this.News()}
        </ScrollView>
      </View>
    );
  }
}

const styles = {
  mainCointaner: {
  backgroundColor: '#E9EBEE',
  flexGrow: 1,
  position: 'absolute',
  height: Dimensions.get('window').height,
  width: Dimensions.get('window').width,
},

newsContainer: {
  backgroundColor: '#E9EBEE',
  shadowColor: '#000',
  shadowOffset: { width: 4, height: 4 },
  shadowOpacity: 0.2,
  shadowRadius: 10,
  elevation: 8,
  marginLeft: 10,
  marginRight: 10,
  marginTop: 10,
  marginBottom: 10,
  height: Dimensions.get('window').height /2,
  padding: 10,
  borderColor: '#B0BCD5',
  borderBottomWidth: 1,
},
newsHeader: {
  borderColor: '#B0BCD5',
  justifyContent:'center',
  alignItems: 'flex-start',
},
newsBody: {
  borderColor: '#B0BCD5',
  padding: 10,
  flex: 3,
},
newsAuthorandDate: {
  justifyContent:'flex-start',
  flexDirection: 'column',
  borderBottomWidth: 1,
},
author:{
  justifyContent: 'flex-start',
  alignItems:'flex-start',
},
date:{
  alignItems:'flex-end'
},


}
