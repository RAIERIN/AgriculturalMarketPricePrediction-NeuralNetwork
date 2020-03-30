import {
  SIGNUP_USER_SUCCESS,
  SIGNUP_EMAIL,
  SIGNUP_PASSWORD,
  REPASSWORD_CHANGED,
  SIGNUP_USER,
  PASSWORD_UNMATCH,
  SIGNUP_USER_FAIL,
  EMPTY_FIELD
} from '../actions/types';

const INITIAL_STATE = {
  email: '', password: '', user: null, error: '', loading: false, confirmPassword: '' };

export default (state = INITIAL_STATE, action) => {
  switch (action.type) {
    case SIGNUP_EMAIL:
      return { ...state, email: action.payload };
    case SIGNUP_PASSWORD:
      return { ...state, password: action.payload };
    case REPASSWORD_CHANGED:
      return { ...state, confirmPassword: action.payload };
    case EMPTY_FIELD:
      return {
        ...state,
        loading: false,
        error: 'Please Fill all the Fields!'
      };
    case PASSWORD_UNMATCH:
      return {
        ...state,
         loading: false,
         error: 'Password unmatch!',
         password: '',
         confirmPassword: '' };
    case SIGNUP_USER:
      return { ...state, loading: true, error: '' };
    case SIGNUP_USER_SUCCESS:
      return { ...state,
              ...INITIAL_STATE,
              user: action.payload };
    case SIGNUP_USER_FAIL:
      return { ...state, error: 'Creating Account Failed!', loading: false };
    default:
      return state;
  }
};
