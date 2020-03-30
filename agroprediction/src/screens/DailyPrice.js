import React, { Component } from 'react';
import Drawer from 'react-native-drawer';
import axios from 'axios';
import { connect } from 'react-redux';
import DatePicker from 'react-native-datepicker';
import { View, Image,ScrollView, Text, Dimensions } from 'react-native';
import { Header } from '../components/common';


export default class DailyPrice extends Component {
  constructor(props) {
    super(props);
    this.state = { date: '', dailyrate:[] };
  }
  componentWillMount() {
    axios.get('http://192.168.43.250:5000/product_detail')
      .then(response => this.setState({ dailyrate: response.data }));
      console.log(this.state.date);
  }
  onDateChange(date) {
    this.setState({date});
    axios.get('http://192.168.43.250:5000/product_detail/'+this.state.date)
      .then(response => this.setState({ dailyrate: response.data }));
  }
  static navigationOptions = {
    tabBarLabel:'Market Price',
    tabBarIcon: ({tintColor}) => (
      <Image
        source={require('../images/price.png')}
        style ={{width:30, height:25, tintColor:'white'}}
        >
      </Image>
    )

  }
  Rates() {
    if (this.state.dailyrate.length > 1){
      return this.state.dailyrate.map((data, i) => {
      return (
        <View key={i}>
          <View style={styles.priceContainer}>
            <View style={styles.priceView}>
              <View style={{width:120}}>
                <Text style={{ color: '#000000', fontSize: 12, fontWeight: '300' }}>{data.name}</Text>
              </View>
              <View style={{width:50,alignItems:'center', marginLeft:20}}>
                <Text style={{ color: '#000000', fontSize: 12, fontWeight: '300',  }}>{data.min}</Text>
              </View>
              <View style={{width:50,alignItems:'center', marginLeft:10}}>
                <Text style={{ color: '#000000', fontSize: 12, fontWeight: '300' }}>{data.max}</Text>
              </View>
              <View style={{width:50,alignItems:'center', marginLeft:10}}>
                <Text style={{ color: '#000000', fontSize: 12, fontWeight: '300' }}>{data.avg}</Text>
              </View>
          </View>
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
            Daily Market Price
          </Header>
        <View style={styles.firstHeader}>
          <View style={styles.locationName}>
            <Text style={{ color: '#000000', fontSize: 16, fontWeight: '800' }}> KALIMATI BAZAR</Text>
          </View>
          <View style={styles.date}>
            <DatePicker
                date={this.state.date}
                mode="date"
                format="YYYY-MM-DD"
                minDate="2016-05-01"
                maxDate="2080-06-01"
                confirmBtnText="Confirm"
                cancelBtnText="Cancel"
                customStyles={{
                  dateIcon: {
                    position: 'absolute',
                    left: 0,
                    top: 2,
                    marginLeft: 0
                  },
                  dateInput: {
                    marginLeft: 36,
                    height: 30,
                  }
                }}
                onDateChange={this.onDateChange.bind(this)}
            />
          </View>
        </View>
        <View style={{ paddingLeft: 20, paddingRight: 20 }}>
          <View style={styles.secondHeader}>
            <Text style={{ color: '#000000', fontSize: 14, fontWeight: '600', paddingLeft: 5 }}>Name</Text>
            <Text style={{ color: '#000000', fontSize: 14, fontWeight: '600', paddingLeft: 120 }}>Min</Text>
            <Text style={{ color: '#000000', fontSize: 14, fontWeight: '600', paddingLeft: 35 }}>Max</Text>
            <Text style={{ color: '#000000', fontSize: 14, fontWeight: '600', paddingLeft: 30 }}>Avg</Text>
          </View>
        </View>
          <ScrollView style={{ marginBottom: 85 }}>
            {this.Rates()}
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
  firstHeader: {
    flexDirection: 'row',
    padding: 10,
  },
  date: {
    flex: 3,
    justifyContent: 'flex-end',
    alignItems: 'center',
  },
  locationName: {
    flex: 2,
    justifyContent: 'center',
    alignItems: 'center',
  },
  secondHeader: {
    borderBottomWidth: 3,
    borderColor: '#0BDE8E',
    borderTopWidth: 3,
    flexDirection: 'row',
    alignItems: 'center',
    padding: 10
  },
  priceContainer: {
    paddingLeft: 25,
    paddingRight: 20,
    marginBottom: 10,
  },
  priceView: {
    borderBottomWidth: 1,
    borderColor: '#95989A',
    flexDirection: 'row',
    alignItems: 'center',
    padding: 10
  }
};
