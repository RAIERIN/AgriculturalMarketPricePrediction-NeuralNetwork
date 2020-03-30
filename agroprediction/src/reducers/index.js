import { combineReducers } from 'redux';
import SignInReducer from './SignInReducer';
import SignUpReducer from './SignUpReducer';

export default combineReducers({
    signin: SignInReducer,
    signup: SignUpReducer,
});
