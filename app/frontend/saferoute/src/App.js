import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Map from './map';
import About from './about';
import UsedData from './used_data';
import { Amplify} from 'aws-amplify';
import awsConfig from './aws-exports';
import { withAuthenticator, ThemeProvider, Theme } from '@aws-amplify/ui-react';
import '@aws-amplify/ui-react/styles.css'; 
import './css/login.css'


Amplify.configure(awsConfig);


function App({ signOut, user }) {
  return (
    <ThemeProvider >
        <Router>
            <Routes>
              <Route path="/" element={<Map />} />
              <Route path="/map/*" element={<Map />} />
              <Route path="/about" element={<About />} />
              <Route path="/used_data" element={<UsedData />} />
            </Routes>
        </Router>
      </ThemeProvider>
  );
}

export default withAuthenticator(App, {
  socialProviders: ['google']
}); 