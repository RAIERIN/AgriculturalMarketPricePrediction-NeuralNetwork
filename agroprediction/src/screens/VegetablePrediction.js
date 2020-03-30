import React, { Component } from 'react';
import Drawer from 'react-native-drawer';
import axios from 'axios';
import { View, TextInput, ScrollView, Text, Dimensions, Image } from 'react-native';
import { Header } from '../components/common';


export default class VegetablePrediction extends Component {
  constructor(props) {
    super(props);
    this.state = { avg:[], text:'' };
  }
  componentWillMount() {
    axios.get('http://192.168.43.250:5000/product_avg')
      .then(response => this.setState({ avg: response.data }))
    }
  static navigationOptions = {
    tabBarLabel:'Prediction',
    tabBarIcon: ({tintColor}) => (
      <Image
        source={require('../images/predict.png')}
        style ={{width:25, height:25, tintColor:'white'}}
        >
      </Image>
    )
  }
  filterSearch(text){

        const newData = this.state.avg.filter(function(item){
            const itemData = item.name.toUpperCase()
            const textData = text.toUpperCase()
            return itemData.indexOf(textData) > -1
        })
        this.setState({
            avg: newData,
            text: text
        })
    }
  Prediction() {
    if (this.state.avg.length >= 1){
        return this.state.avg.map((data,i) => {
        return (
          <View key={i}>
            <View
              style={styles.priceContainer}
              enableEmptySections={true}
            >
              <View style={styles.graphImage}>
                <Image
                  style={{width:300,height:250}}
                  source={{uri: 'http://192.168.43.250:5000/imgs/' +  data.url}}
                />
              </View>
              <View style={styles.detailInfo}>
                <Text style={{ color: '#FFFFFF', fontSize: 24, fontWeight: '200' }}>{data.name}</Text>
                <Text style={{ color: '#FFFFFF', fontSize: 11, fontStyle: 'italic' }}>{data.scientificname}</Text>
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
  }
    render() {
      console.log(this.state.err);
      return (
        <View style={styles.mainCointaner}>
            <Header>
              Monthly Prediction
            </Header>

              <View style={styles.seachBox}>
                <View style={styles.imageSearch}>
                  <Image
                    source={require('../images/search.png')}
                    style ={{width:35, height:35}}
                  />
                </View>
                <View style={styles.textSearch}>
                  <TextInput
                       style={styles.textInput}
                       onChangeText={(text) => this.filterSearch(text)}
                       value={this.state.text}
                  />
                </View>
              </View>

                  <ScrollView style={{ marginBottom: 85 }}>
                    {this.Prediction()}
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
    marginBottom: 10,
    flexDirection: 'column',
    height: Dimensions.get('window').height / 1.6,
  },
  seachBox: {
      flexDirection:'row',
      marginTop: 10,
      marginRight:5,
      paddingRight:30
  },
  imageSearch:{
    flex:1,
    justifyContent:'flex-end',
    alignItems:'flex-end',
  },
  textSearch:{
    flex:4,
    padding:5
  },
  graphImage: {
    flex: 2,
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
