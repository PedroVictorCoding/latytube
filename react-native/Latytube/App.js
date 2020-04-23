import 'react-native-gesture-handler';
import React from 'react';
import { StyleSheet, Text, View, TextInput, Button, AsyncStorage } from 'react-native';
import { AppLoading, Asset } from 'expo';
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';
import Home from './screens/home';
const AuthContext = React.createContext();

const axios = require('axios').default;
const Stack = createStackNavigator();

function SignInScreen({ navigation }) {
  const [email, setEmail] = React.useState('');
  const [username, setUsername] = React.useState('');
  const [password, setPassword] = React.useState('');
  const [password2, setPassword2] = React.useState('');

  const { signIn } = React.useContext(AuthContext);

  return (
    <View>
      <TextInput
        placeholder="Username"
        value={username}
        onChangeText={setUsername}
      />
      <TextInput
        placeholder="Password"
        value={password}
        onChangeText={setPassword}
        secureTextEntry
      />
      <Button style={{ backgroundColor:"#23E8A5"}} title="Sign in" onPress={() => signIn({ username, password }).then(navigation.navigate('Home', {name: 'Home'}))} />
    </View>
  );
}

export default function App({ navigation }) {
  const [state, dispatch] = React.useReducer(
    (prevState, action) => {
      switch (action.type) {
        case 'RESTORE_TOKEN':
          return {
            ...prevState,
            userToken: action.token,
            isLoading: false,
          };
        case 'SIGN_IN':
          return {
            ...prevState,
            isSignout: false,
            userToken: action.token,
          };
        case 'SIGN_OUT':
          return {
            ...prevState,
            isSignout: true,
            userToken: null,
          };
      }
    },
    {
      isLoading: true,
      isSignout: false,
      userToken: null,
    }
  );

  const authContext = React.useMemo(
    () => ({
      signIn: async data => {
        console.log(data);

        fetch("https://www.notatish.com/api/login/", {
          method: 'POST',
          //{"username":["This field is required."],"password":["This field is required."]}
          body: JSON.stringify({ username: data.username, password: data.password }),
          headers: new Headers({
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Connection': 'keep-alive',
          }),
        })
        .then((response) => response.text())
        .catch(function(error) {
          console.log('There has been a problem with your fetch operation: ' + error.message);
           // ADD THIS THROW error
            throw error;
          })
        .then((response) => response.substring(10, response.length - 2))
        .then((result) => AsyncStorage.setItem('userToken', result));
      },
    }),
  
  );

  return (
    <NavigationContainer>
    <AuthContext.Provider value={authContext}>
      <Stack.Navigator>
        {state.userToken == null ? (
          <Stack.Screen name="SignIn" component={SignInScreen} />
        ) : (
          <Stack.Screen name="Home" component={Home} />
        )}
      <Stack.Screen name="Home" component={Home}
      options={{
        headerShown: false,
      }}
      />
      </Stack.Navigator>
    </AuthContext.Provider>
    </NavigationContainer>
  );
}