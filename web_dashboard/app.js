fetch('http://localhost:5000/temperature')
  .then(res => res.json())
  .then(data => {
    document.getElementById('output').innerHTML = `Temperature: ${data.temperature} °C`;
  });

fetch('http://localhost:5000/humidity')
  .then(res => res.json())
  .then(data => {
    document.getElementById('humidity').innerHTML = `Humidity: ${data.humidity} %`;
  });
