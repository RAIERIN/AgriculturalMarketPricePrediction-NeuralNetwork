import { Actions } from 'react-native-router-flux';
import firebase from 'firebase';
import {
  SIGNUP_USER_SUCCESS,
  SIGNUP_EMAIL,
  SIGNUP_PASSWORD,
  REPASSWORD_CHANGED,
  SIGNUP_USER,
  PASSWORD_UNMATCH,
  SIGNUP_USER_FAIL,
  EMPTY_FIELD
} from './types';

export const signupEmail = (text) => {
  return {
    type: SIGNUP_EMAIL,
    payload: text
  };
};
export const signupPassword = (text) => {
  return {
    type: SIGNUP_PASSWORD,
    payload: text
  };
};
export const rePassword = (text) => {
  return {
    type: REPASSWORD_CHANGED,
    payload: text
  };
};
export const signupUser = ({ email, password, confirmPassword }) => {
  return (dispatch) => {
    dispatch({ type: SIGNUP_USER });
    if (email !== '' && password !== '' && confirmPassword !== '') {
      if (password === confirmPassword) {
        firebase.auth().createUserWithEmailAndPassword(email, password)
          .then(user => signupUserSuccess(dispatch, user))
          .catch(() => signupUserFail(dispatch));
      } else {
          dispatch({ type: PASSWORD_UNMATCH });
        }
      } else {
      dispatch({ type: EMPTY_FIELD });
    }
  };
};

const signupUserFail = (dispatch) => {
  dispatch({
    type: SIGNUP_USER_FAIL,
  });
};

const signupUserSuccess = (dispatch, user) => {
  dispatch({
    type: SIGNUP_USER_SUCCESS,
    payload: user,
  });
  Actions.login();
};
