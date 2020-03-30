import React, { Component } from 'react';
import Drawer from 'react-native-drawer';
import axios from 'axios';
import { View, ScrollView, Text, Dimensions, Image } from 'react-native';
import { Header } from '../components/common';
import NavigationDrawerPage from '../components/common/NavigationDrawerPage';

export default class VegetablePrediction extends Component {
  constructor(props) {
    super(props);
    this.state = { avg:[] };
  }
  componentWillMount() {
    axios.get('http://192.168.43.250:5000/product_avg')
      .then(response => this.setState({ avg: response.data }));
  }
  closeNavigationDrawer =() => {
    this.drawer.close();
  }
  openNavigationDrawer = () => {
        this.drawer.open();
  };

  Prediction() {
    return this.state.avg.map((data,i) => {
    return (
      <View key={i}>
        <View style={styles.priceContainer}>
          <View style={styles.graphImage}>
            <Image
              style={{width:300,height:200}}
              source={{uri: 'http://192.168.43.250:5000/imgs/' +data.url}}
            />
          </View>
          <View style={styles.detailInfo}>
            <Text style={{ color: '#FFFFFF', fontSize: 24, fontWeight: '200' }}>{data.name}</Text>
            <Text style={{ color: '#FFFFFF', fontSize: 11, fontStyle: 'italic' }}>Brassica oleracea var. capitata</Text>
            <Text style={{ color: '#FFFFFF', fontSize: 18, fontWeight: '200', paddingTop: 10 }}>Price Prediction Details</Text>
            <View style={styles.priceDetail}>
              <Text style={{ color: '#FFFFFF', fontSize: 16, fontWeight: '200' }}>Prediction :</Text>
              <Text style={{ color: '#FFFFFF', fontSize: 16, fontWeight: '200', paddingLeft: 100 }}>{data.predict}</Text>
            </View>
            <View style={styles.priceDetail}>
              <Text style={{ color: '#FFFFFF', fontSize: 16, fontWeight: '200'}}>Past Price :</Text>
              <Text style={{ color: '#FFFFFF', fontSize: 16, fontWeight: '200', paddingLeft: 100 }}>{data.avg}</Text>
            </View>
          </View>
      </View>
      </View>

    );
  });
  }
    render() {
      return (
        <Drawer
            ref={(ref) => this.drawer = ref}
            type="overlay"
            content={<NavigationDrawerPage />}
            tapToClose
            openDrawerOffset={0.25} // 25% gap on the right side of drawer
            tweenDuration={150}
        >
        <View style={styles.mainCointaner}>
            <Header onPress={this.openNavigationDrawer.bind(this)} >
              Vegetable Prediction
            </Header>
            <ScrollView style={{ marginBottom: 40 }}>
              {this.Prediction()}
            </ScrollView>
        </View>
      </Drawer>
    );
  }
}

const styles = {
    mainCointaner: {
    backgroundColor: '#EEEEEE',
    flexGrow: 1,
    position: 'absolute',
    height: Dimensions.get('window').height,
    width: Dimensions.get('window').width,
  },
  priceContainer: {
    backgroundColor: '#FFFFFF',
    shadowColor: '#000',
    shadowOffset: { width: 2, height: 3 },
    shadowOpacity: 0.1,
    borderRadius: 5,
    shadowRadius: 2,
    elevation: 6,
    marginLeft: 30,
    marginRight: 30,
    marginTop: 20,
    flexDirection: 'column',
    height: Dimensions.get('window').height / 1.7
  },
  graphImage: {
    flex: 1.5,
    justifyContent: 'center',
    alignItems: 'center',
  },
  detailInfo: {
    flex: 1,
    backgroundColor: '#0BDE8E',
    padding: 20
  },
  priceDetail: {
    flexDirection: 'row',
    paddingTop: 5,
    paddingLeft: 5,
  }
};
