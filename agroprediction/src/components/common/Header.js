import React from 'react';
import { Text, View, Dimensions, TouchableOpacity, Image } from 'react-native';

const Header = ({ onPress, children }) => {
  const { textStyle,viewStyle,images,headerName,headerCont } = styles;
  return (
    <View style={viewStyle}>
      <View style={images}>
        <Image
          source={require('../../images/secondlogo.png')}
          style ={{width:35, height:35}}
        />
      </View>
        <View style={headerName}>
            <Text style={textStyle}>{children}</Text>
        </View>


  </View>
  );
};

const styles = {
    viewStyle: {
      backgroundColor: '#0BDE8E',
      justifyContent: 'flex-start',
      height: Dimensions.get('window').height / 8,
      shadowColor: '#000',
      shadowOffset: { width: 0, height: 2 }, //what side the shadow to be on
      shadowOpacity: 0.2, //darrkeness
      shadowRadius: 4,
      elevation: 3,
      flexDirection: 'row',
      alignItems:'center',
    },
    textStyle: {
      fontSize: 24,
      color: '#ffffff',
    },

    headerName: {
       justifyContent:'center',
       alignItems:'center',
       paddingLeft: 40
    },
    images: {
        justifyContent: 'flex-start',
        paddingLeft: 10
    }
};
export { Header };
