import React from 'react';
import { GoogleMap, LoadScript, useJsApiLoader, Polygon, HeatmapLayer } from '@react-google-maps/api';
import { mapContainerStyle, defaultOptions, defaultCenter, bounds } from './JS/map_setup';
import {Header} from './JS/ui_components';
import { to_heatmap_data } from './JS/load_data';
import { withAuthenticator } from '@aws-amplify/ui-react';
import ReactLoading from 'react-loading';
import css from './css/style.css';
import signoutImage from './images/signout.png';
import logo from './images/logo.png';

const API_KEY = process.env.REACT_APP_API_KEY;


const MapComponent = () => {
  const [map, setMap] = React.useState(null);
  const [heatmaps, setHeatmaps] = React.useState([]);
  const [isLoading, setIsLoading] = React.useState(true);

  const onLoad = React.useCallback(function callback(mapInstance) {
    setMap(mapInstance);
  }, []);

  const onUnmount = React.useCallback(function callback() {
    setMap(null);
  }, []);

  React.useEffect(() => {
    const fetchData = async () => {
      setIsLoading(true);
      const heatmapData = await to_heatmap_data(bounds.west, bounds.south, bounds.east, bounds.north);
      setHeatmaps(heatmapData);
      setIsLoading(false);
    };
    fetchData();
  }, []);

  return (
    <GoogleMap
      mapContainerStyle={mapContainerStyle}
      center={defaultCenter}
      zoom={12}
      options={defaultOptions}
      onLoad={onLoad}
      onUnmount={onUnmount}
    >
      {heatmaps.map((squareOptions, index) => (
        <Polygon key={index} {...squareOptions} />
      ))}
      {isLoading && (
        <div
          style={{
            position: 'absolute',
            top: -80,
            left: 0,
            right: 0,
            bottom: 0,
            backgroundColor: 'rgba(0, 0, 0, 0.4)',
            display: 'flex',
            justifyContent: 'center',
            alignItems: 'center',
            zIndex: 9999,
          }}
        >
          <ReactLoading type="spinningBubbles" color="#eff1f5" height={80} width={80} />
        </div>
      )}
    </GoogleMap>
  );
};



const Map = ({ signOut, user }) => {
  const isLoaded = !!API_KEY;
  return (
    <div>
      <Header>
      </Header>
      {isLoaded ? (
        <LoadScript googleMapsApiKey={API_KEY} language="en"  libraries={['visualization']}>
          <MapComponent />
        </LoadScript>
      ) : (
        <h2>LOADING MAP</h2>
      )}
    </div>
  );
};

export default withAuthenticator(Map, {
  socialProviders: ['google']
});
