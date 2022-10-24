

 const labels ={{k1|safe}}

  const data = {
    labels: labels,
    datasets: [{
      label: 'Data average in ariana',
      backgroundColor: 'rgb(255, 99, 132)',
      borderColor: 'rgb(255, 99, 132)',
      data: {{k|safe}},
    }]
  };

  const config = {
    type: 'line',
    data: data,
    options: {}
  };

   const myChart = new Chart(
    document.getElementById('myChart'),
    config
  );
  console.log('helloworld')