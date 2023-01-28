
const ctx = document.getElementById('myChart');

  new Chart(ctx, {
    type: 'line',
    data: {
      labels: ['start', '0:30', '1:00', '1:30', '2:00', '2:30'],
      datasets: [{
        label: 'Sensor 1',
        data: [12, 19, 3, 5, 2, 21],
        borderColor: 'green',
        cubicInterpolationMode: 'monotone',
        borderWidth: 3,
      },
      {
        label: 'Sensor 2',
        data: [17, 10, 3, 18, 2, 5],
        borderColor: 'red',
        backgroundColor: 'red',
        cubicInterpolationMode: 'monotone',
        borderWidth: 3,
      },
      {
        label: 'Sensor 3',
        data: [8, 11, 3, 5, 7, 12],
        cubicInterpolationMode: 'monotone',
        borderColor: 'blue',
        borderWidth: 3,
      },
      {
        label: 'Sensor 4',
        data: [17, 2, 19, 8, 1, 9],
        borderColor: 'pink',
        cubicInterpolationMode: 'monotone',
        borderWidth: 3,
      }]
    },
    options: {
      scales: {
        y: {
          beginAtZero: true
        }
      }
    }
  });