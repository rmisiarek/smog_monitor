let socket = io();
let smogChart = null;           // pm10, pm2.5
let weatherChart = null;        // temperature, humidity


socket.on('connect', function() {
  socket.emit('get_initial_data', {data: 'connected'});
});

socket.on('initial_data', function(data) {
  smogChart = createSmogChart(
    data.smog_data.pm10,
    data.smog_data.pm25,
    data.smog_data.categories,
    data.colors,
  );

  weatherChart = createWeatherChart(
    data.weather_data.temperature,
    data.weather_data.humidity,
    data.weather_data.categories,
    data.colors
  );
});

socket.on('smog', function(data) {
  smogChart.series[0].setData(data.pm10);
  smogChart.series[1].setData(data.pm25);
  smogChart.xAxis[0].setCategories(data.categories)
});


socket.on('weather', function(data) {
  weatherChart.series[0].setData(data.temperature);
  weatherChart.series[1].setData(data.humidity);
  weatherChart.xAxis[0].setCategories(data.categories)
});


function createSmogChart(pm10Data, pm25Data, categoriesData, colors) {
    let chart = Highcharts.chart('dust-chart', {
        chart: {
            height: 'auto',
            zoomType: 'xy',
        },
        title: {
            text: 'PM10 & PM2.5'
        },
        subtitle: {
            text: null,
        },
        xAxis: [{
            categories: categoriesData,
            crosshair: true
        }],
        yAxis: [{
            labels: {
                format: '{value} μg/m3',
            },
            title: {
                text: 'PM10',
            }
        }, {
            title: {
                text: 'PM2.5',
            },
            labels: {
                format: '{value} μg/m3',
            },
            opposite: true
        }],
        tooltip: {
            shared: true
        },
        series: [{
            color: colors.first,
            name: 'PM10',
            type: 'spline',
            yAxis: 1,
            data: pm10Data,
            tooltip: {
                valueSuffix: 'μg/m3'
            }

        }, {
            color: colors.second,
            name: 'PM2.5',
            type: 'spline',
            data: pm25Data,
            tooltip: {
                valueSuffix: 'μg/m3'
            }
        }]
    });
    return chart;
}


function createWeatherChart(temperatureData, humidityData, categoriesData, colors) {
    let chart = Highcharts.chart('temperature-chart', {
        chart: {
            height: 'auto',
            zoomType: 'xy',
        },
        title: {
            text: 'Temparature and Humidity'
        },
        subtitle: {
            text: null,
        },
        xAxis: [{
            categories: categoriesData,
            crosshair: true
        }],
        yAxis: [{
            labels: {
                format: '{value}°C',
            },
            title: {
                text: 'Temperature',
            }
        }, {
            title: {
                text: 'Humidity',
            },
            labels: {
                format: '{value} %',
            },
            opposite: true
        }],
        tooltip: {
            shared: true
        },
        series: [{
            color: colors.second,
            name: 'Temperature',
            type: 'column',
            yAxis: 1,
            data: temperatureData,
            tooltip: {
                valueSuffix: '°C'
            }
        }, {
            color: colors.first,
            name: 'Humidity',
            type: 'spline',
            data: humidityData,
            tooltip: {
                valueSuffix: ' %'
            }
        }]
    });
    return chart;
}