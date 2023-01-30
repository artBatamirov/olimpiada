
const ctx3 = document.getElementById('thirdChart').getContext("2d");

  new Chart(ctx3, {
    type: 'line',
    data: {
      labels: ['start', '0:30', '1:00', '1:30', '2:00', '2:30'],
      datasets: [{
        label: 'Sensor 1',
        data: [12, 19, 3, 5, 2, 21],
        borderColor: 'brown',
        cubicInterpolationMode: 'monotone',
        borderWidth: 3,
      },
      {
        label: 'Sensor 2',
        data: [17, 10, 3, 18, 2, 5],
        borderColor: 'MediumSlateBlue',
        cubicInterpolationMode: 'monotone',
        borderWidth: 3,
      },
      {
        label: 'Sensor 3',
        data: [8, 11, 3, 5, 7, 12],
        cubicInterpolationMode: 'monotone',
        borderColor: 'Aquamarine',
        borderWidth: 3,
      },
      {
        label: 'Sensor 4',
        data: [17, 2, 19, 8, 1, 9],
        borderColor: 'Orchid',
        cubicInterpolationMode: 'monotone',
        borderWidth: 3,
      },
      {
        label: 'Sensor 5',
        data: [17, 2, 19, 8, 1, 9],
        borderColor: 'DeepPink',
        cubicInterpolationMode: 'monotone',
        borderWidth: 3,
      },
      {
        label: 'Sensor 6',
        data: [17, 2, 19, 8, 1, 9],
        borderColor: 'LightGreen',
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