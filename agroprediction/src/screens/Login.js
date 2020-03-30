import React, { Component } from 'react';
import { View, Text, Image, ScrollView, Dimensions, TouchableOpacity } from 'react-native';
import { connect } from 'react-redux';
import { TextField } from 'react-native-material-textfield';
import { Actions } from 'react-native-router-flux';
import { emailChanged, passwordChanged, loginUser } from '../actions';
import { Spinner } from '../components/common';

class Login extends Component {
  onEmailChange(text) {
  this.props.emailChanged(text);
  }
  onPasswordChange(text) {
  this.props.passwordChanged(text);
  }
  onSignInPress() {
    const { email, password } = this.props;
    this.props.loginUser({ email, password });
  }
  renderError() {
    if (this.props.error) {
      return (
        <View style={{ backgroundColor: '#FFFCF9' }}>
          <Text style={styles.errorTextStyle}>
            {this.props.error}
          </Text>
        </View>
      );
    }
  }
  renderSpinner() {
    if (this.props.loading) {
        return <Spinner size="large" />;
    }
  }
  render() {
    return (
      <View>
        <View style={styles.mainCointaner}>
          <ScrollView
            showsVerticalScrollIndicator={false}
            contentContainerStyle={{ flexGrow: 1 }}
            scrollEnabled={false}
          >
            <View style={styles.header}>
              <View style={styles.logo}>
                <Image
                  style={styles.logoImage}
                  source={require('../images/secondlogo.png')}
                />
              </View>
              <View style={styles.headerText}>
                <Text style={styles.headText}>
                  Sign In
                </Text>
              </View>
            </View>
            <View style={styles.signIn}>
                <View>
                    <TextField
                       label={'Email'}
                       baseColor={'#23B5D3'}
                       textColor={'#0BDE8E'}
                       tintColor={'#FF6978'}
                       labelHeight={20}
                       lineWidth={1}
                       fontSize={16}
                       returnKeyType="next"
                       value={this.props.email}
                       onChangeText={this.onEmailChange.bind(this)}
                       onSubmitEditing={(event) => {
                          this.refs.SecondInput.focus();
                        }}
                    />
                </View>
                <View>
                  <TextField
                      ref='SecondInput'
                      label={'Password'}
                      baseColor={'#23B5D3'}
                      textColor={'#0BDE8E'}
                      tintColor={'#FF6978'}
                      labelHeight={20}
                      lineWidth={1}
                      fontSize={16}
                      returnKeyType="done"
                      secureTextEntry
                      value={this.props.password}
                      onChangeText={this.onPasswordChange.bind(this)}
                  />
                </View>
                <View>
                  {this.renderSpinner()}
                  {this.renderError()}
                    <TouchableOpacity
                      style={styles.signInButton}
                      onPress={this.onSignInPress.bind(this)}
                    >
                      <Text style={styles.signInText}> Sign In </Text>
                    </TouchableOpacity>
                </View>
                <View style={styles.signUpPage}>
                  <View>
                    <Text style={styles.accountText}>
                      Ready have an account?
                    </Text>
                  </View>
                  <View>
                    <TouchableOpacity onPress={() => Actions.signup()}>
                      <Text style={styles.signUpText}> Sign Up </Text>
                    </TouchableOpacity>
                  </View>
                </View>
                <View style={{ paddingTop: 20, justifyContent: 'center' }}>
                  <TouchableOpacity style={styles.skipButton} onPress={() => Actions.home()}>
                    <Text style={styles.skipText}> Skip </Text>
                  </TouchableOpacity>
                </View>
            </View>
          </ScrollView>
        </View>
    </View>
    );
  }
}

const styles = {
    mainCointaner: {
    backgroundColor: '#FFFCF9',
    flexGrow: 1,
    position: 'absolute',
    height: Dimensions.get('window').height,
    width: Dimensions.get('window').width,
  },
    header: {
      backgroundColor: '#0BDE8E',
      alignItems: 'center',
      justifyContent: 'center',
      height: Dimensions.get('window').height / 2.8,
    },
    logo: {
      marginTop: -60,
    },
    headText: {
      color: '#FFFCF9',
      fontSize: 24,
      marginTop: 5,
    },
    signIn: {
      height: Dimensions.get('window').height / 1.5,
      backgroundColor: '#FFFCF9',
      borderRadius: 5,
      shadowOffset: { width: 8, height: 10 },
      shadowOpacity: 0.6,
      shadowRadius: 5,
      elevation: 8,
      marginTop: -60,
      marginLeft: 30,
      marginRight: 30,
      marginBottom: 50,
      padding: 40
    },
    signInButton: {
      alignItems: 'center',
      backgroundColor: '#0BDE8E',
      borderRadius: 30,
      height: 50,
      marginTop: 40,
    },
    signInText: {
        color: '#FFFCF9',
        fontSize: 20,
        fontWeight: '200',
        paddingTop: 10,
        paddingBottom: 10
    },
    signUpPage: {
      marginTop: 50,
      flexDirection: 'row',
      justifyContent: 'center',
    },
    accountText: {
      color: '#0BDE8E',
      fontSize: 12,
    },
    signUpText: {
      color: '#2A92BB',
      fontSize: 14,
    },
    errorTextStyle: {
      color: '#FF6978',
      fontSize: 14,
      alignSelf: 'center',
    },
    skipButton: {
      alignItems: 'center',
      justifyContent: 'center',
    },
    skipText: {
        color: '#FF6978',
        fontSize: 14,
        fontWeight: '200',
        paddingTop: 10,
        paddingBottom: 10,
        textDecorationLine: 'underline'
    },
};
const mapStateToProps = ({ signin }) => {
  const { email, password, error, loading } = signin;
  return { email, password, error, loading };
};

export default connect(mapStateToProps, {
  emailChanged, passwordChanged, loginUser })(Login);
