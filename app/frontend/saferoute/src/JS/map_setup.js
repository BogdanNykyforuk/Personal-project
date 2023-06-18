export const mapStyle = 
  [
      {
          "featureType": "all",
          "elementType": "geometry",
          "stylers": [
              {
                  "color": "#202c3e"
              }
          ]
      },
      {
          "featureType": "all",
          "elementType": "labels.text.fill",
          "stylers": [
              {
                  "gamma": 0.01
              },
              {
                  "lightness": 20
              },
              {
                  "weight": "1.39"
              },
              {
                  "color": "#ffffff"
              }
          ]
      },
      {
          "featureType": "all",
          "elementType": "labels.text.stroke",
          "stylers": [
              {
                  "weight": "0.96"
              },
              {
                  "saturation": "9"
              },
              {
                  "visibility": "on"
              },
              {
                  "color": "#000000"
              }
          ]
      },
      {
          "featureType": "all",
          "elementType": "labels.icon",
          "stylers": [
              {
                  "visibility": "off"
              }
          ]
      },
      {
          "featureType": "landscape",
          "elementType": "geometry",
          "stylers": [
              {
                  "lightness": 30
              },
              {
                  "saturation": "9"
              },
              {
                  "color": "#29446b"
              }
          ]
      },
      {
          "featureType": "poi",
          "elementType": "geometry",
          "stylers": [
              {
                  "saturation": 20
              }
          ]
      },
      {
          "featureType": "poi.park",
          "elementType": "geometry",
          "stylers": [
              {
                  "lightness": 20
              },
              {
                  "saturation": -20
              }
          ]
      },
      {
          "featureType": "road",
          "elementType": "geometry",
          "stylers": [
              {
                  "lightness": 10
              },
              {
                  "saturation": -30
              }
          ]
      },
      {
          "featureType": "road",
          "elementType": "geometry.fill",
          "stylers": [
              {
                  "color": "#193a55"
              }
          ]
      },
      {
          "featureType": "road",
          "elementType": "geometry.stroke",
          "stylers": [
              {
                  "saturation": 25
              },
              {
                  "lightness": 25
              },
              {
                  "weight": "0.01"
              }
          ]
      },
      {
          "featureType": "water",
          "elementType": "all",
          "stylers": [
              {
                  "lightness": -20
              }
          ]
      } 
]

export const mapContainerStyle = {
    width: '100vw',
    height: '100vh'
};
  
export const defaultCenter = {
    lat: 38.91,
    lng: -77.05
};

export const defaultOptions = {
    disableDefaultUI: true,
    restriction: {
      latLngBounds: {
        north: 39.13,
        south: 38.55,
        east: -76.4,
        west: -77.6,
      }
    },
    gestureHandling: 'greedy',
    minZoom: 11,
    styles: mapStyle,
    language: 'en'
};

export const bounds = defaultOptions.restriction.latLngBounds;