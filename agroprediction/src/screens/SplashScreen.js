import React, { Component } from 'react';
import {
  Text,
  View,
  Image,
  TouchableOpacity,
} from 'react-native';
import { Actions } from 'react-native-router-flux';


export default class SplashScreen extends Component {
  render() {
    return (
      <View style={styles.container}>
        <View style={styles.logoContainer}>
            <Image
              style={styles.logoImage}
              source={require('../images/logo.png')}
            />
            <Text style={styles.title}> AgroPrediction </Text>
        </View>
        <View style={styles.navButtons}>
          <TouchableOpacity style={styles.signupButton} onPress={() => Actions.signup()}>
            <Text style={styles.signupText}> Sign Up </Text>
          </TouchableOpacity>
          <TouchableOpacity style={styles.loginButton} onPress={() => Actions.login()}>
            <Text style={styles.loginText}> Sign In </Text>
          </TouchableOpacity>
          <TouchableOpacity style={styles.skipButton} onPress={() => Actions.home()}>
            <Text style={styles.skipText}> Skip </Text>
          </TouchableOpacity>
        </View>
      </View>
    );
  }
}

const styles = {
    container: {
      flex: 1,
      backgroundColor: '#FFFCF9',
    },
    logoContainer: {
      flex: 2,
      justifyContent: 'center',
      alignItems: 'center',
      marginBottom: 50,
    },
    navButtons: {
      flex: 1,
      justifyContent: 'center',
      alignItems: 'center',
      marginTop: -100,
    },
    title: {
      color: '#000000',
      fontSize: 30,
      fontWeight: '200',
      paddingTop: 10,
      paddingBottom: 10,
      opacity: 0.87,
    },
    signupText: {
        color: '#FFFCF9',
        fontSize: 20,
        fontWeight: '200',
        paddingTop: 10,
        paddingBottom: 10
      },
      loginText: {
          color: '#0BDE8E',
          fontSize: 20,
          fontWeight: '200',
          paddingTop: 10,
          paddingBottom: 10
      },
      skipText: {
          color: '#FF6978',
          fontSize: 20,
          fontWeight: '200',
          paddingTop: 10,
          paddingBottom: 10,
          textDecorationLine: 'underline'
      },
      signupButton: {
        alignItems: 'center',
        backgroundColor: '#0BDE8E',
        borderRadius: 30,
        width: 230,
        height: 50,
        marginBottom: 20,
      },
      loginButton: {
        alignItems: 'center',
        backgroundColor: '#FFFCF9',
        borderRadius: 30,
        borderColor: '#D1CECE',
        borderWidth: 2,
        width: 230,
        height: 50,
        marginBottom: 20,
      },
      skipButton: {
        alignItems: 'center',
        width: 230,
        height: 50,
        marginBottom: 10,
      }
    };
