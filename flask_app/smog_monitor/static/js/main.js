var socket = io();

socket.on('connect', function() {
  socket.emit('my event', {data: 'I\'m connected!'});
});


socket.on('dust_and_temperature', function(data) {
  console.log('dust_and_temperature', data);
});


socket.on('temperature', function(data) {
  console.log('temperature: ', data);
  document.getElementById("temperature").innerHTML = data.temperature;
  document.getElementById("humidity").innerHTML = data.humidity;
});
