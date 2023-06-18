import chroma from 'chroma-js';


export async function fetchData(l, b, r, t) {
  try {
    const full_response = [];
    const concurrencyLimit = 10;
    let page = 0;
    let activeRequests = 0;
    let finished = false;

    const currentDate = new Date();

    const checkPage = async () => {
      if (finished) {
        return;
      }

      activeRequests++;
      console.log(currentDate.getHours())
      const response = await fetch(`https://33faoddqwe4bjauetiiaatreye0uirjf.lambda-url.eu-central-1.on.aws/db/get_data_from_bounds?l=${l}&b=${b}&r=${r}&t=${t}&page=${page}&time=${currentDate.getHours()}`);
      const data = await response.json();

      if (response.status === 400) {
        throw new Error('Bad request');
      }

      full_response.push(...data);

      if (!data.length) {
        finished = true;
      }

      activeRequests--;
    };

    while (!finished) {
      const requests = [];
      for (let i = 0; i < concurrencyLimit; i++) {
        requests.push(checkPage());
        page++;
      }

      await Promise.all(requests);
    }

    return full_response;
  } catch (error) {
    console.error('Error fetching data: ', error);
    throw error;
  }
}


function getMinMaxValues(data) {
  let minValue = Number.MAX_VALUE;
  let maxValue = Number.MIN_VALUE;

  for (let entry of data) {
    if (entry.data < minValue) {
      minValue = entry.data;
    }
    if (entry.data > maxValue) {
      maxValue = entry.data;
    }
  }

  return { min: minValue, max: maxValue };
}


function calculateFillColor(value, minValue, maxValue) {
  const colorScale = chroma.scale(['black', 'red']).domain([minValue+0.0001, maxValue]);
  return colorScale(value).hex();
}

export async function to_heatmap_data(l, b, r, t, opc = 0.5) {
  const data = await fetchData(l, b, r, t);
  console.log('Fetched data:', data);

  const { min, max } = getMinMaxValues(data);

  const heatmaps = [];

  for (let entry of data) {
    let squareSize = entry.resolution;
    const squareBounds = [
      { lat: entry.center.lat + squareSize / 2, lng: entry.center.lon + squareSize / 2 },
      { lat: entry.center.lat + squareSize / 2, lng: entry.center.lon - squareSize / 2 },
      { lat: entry.center.lat - squareSize / 2, lng: entry.center.lon - squareSize / 2 },
      { lat: entry.center.lat - squareSize / 2, lng: entry.center.lon + squareSize / 2 },
    ];

    const squareOptions = {
      paths: squareBounds,
      options: {
        fillColor: calculateFillColor(entry.data, min, max),
        fillOpacity: opc,
        strokeColor: calculateFillColor(entry.data, min, max),
        strokeOpacity: opc - 0.2,
        strokeWeight: 0,
        clickable: false,
        draggable: false,
        editable: false,
        geodesic: false,
        zIndex: 1
      },
    };

    heatmaps.push(squareOptions);
  }

  console.log(heatmaps);
  return heatmaps;
}