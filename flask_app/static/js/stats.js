async function updateLineChart() {

  try {

    const response = await fetch("http://127.0.0.1:5000/get-stats-line");
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    data = await response.json();
    let parsedData = data.map((item) => {
      const [year, month, day] = item.fecha
        .split("-")
        .map((part) => parseInt(part, 10));
      return [
        Date.UTC(year, month - 1, day), // javascript month indices start from 0 !
        item.count,
      ];
    });

    // Get the chart by ID
    const chart = Highcharts.charts.find(
      (chart) => chart && chart.renderTo.id === "container-1"
    );

    if (chart) {
    // Update the chart with new data
    chart.update({
      series: [
        {
          data: parsedData,
        },
      ],
    });
    } else {
        throw new Error("Chart with ID 'container-1' not found.");
    }
  } catch (error) {
    console.error("There has been a problem with your fetch operation:", error);
    throw error;
  }
}

async function updatePieChart() {
    try {

    const response = await fetch("http://127.0.0.1:5000/get-stats-pie");
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    data = await response.json();
   
    // Get the chart by ID
    const chart = Highcharts.charts.find(
      (chart) => chart && chart.renderTo.id === "container-2"
    );

    if (chart) {
    // Update the chart with new data
    chart.update({
      series: [
        {
          data: data,
        },
      ],
    });
    } else {
        throw new Error("Chart with ID 'container-2' not found.");
    }
  } catch (error) {
    console.error("There has been a problem with your fetch operation:", error);
    throw error;
  }

  
}

async function updateBarChart() {
    try {

    const response = await fetch("http://127.0.0.1:5000/get-stats-bar");
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    data = await response.json();
   
    // Get the chart by ID
    const chart = Highcharts.charts.find(
      (chart) => chart && chart.renderTo.id === "container-3"
    );

    if (chart) {
        const catSeriesData = data.find(d => d.name.toLowerCase() === "gato")?.data || [];
        const dogSeriesData = data.find(d => d.name.toLowerCase() === "perro")?.data || [];
    // Update the chart with new data
        chart.series[0].update({
         
            data: catSeriesData
        });

        // Update the series for dogs
        chart.series[1].update({
          
            data: dogSeriesData
        });;
    } else {
        throw new Error("Chart with ID 'container-3' not found.");
    }
  } catch (error) {
    console.error("There has been a problem with your fetch operation:", error);
    throw error;
  }

  
}



//Line Chart
Highcharts.chart("container-1", {
  chart: {
    type: "line",
  },
  title: {
    text: "Cantidad de Avisos de Adopción por Día",
  },
  xAxis: {
    type: "datetime",
    dateTimeLabelFormats: {
      month: "%b %e, %Y",
    },
    title: {
      text: "Fecha",
    },
  },
  yAxis: {
    title: {
      text: "Cantidad de Avisos",
    },
  },
  legend: {
    align: "left",
    verticalAlign: "top",
    borderWidth: 0,
  },

  tooltip: {
    shared: true,
    crosshairs: true,
  },

  series: [
    {
      name: "Avisos",
      data: [],
      lineWidth: 1,
      marker: {
        enabled: true,
        radius: 4,
      },
      color:"#2150e0",
    },
  ],
});

// Pie Chart
Highcharts.chart('container-2', {
    chart: {
        type: 'pie'
    },
    title: {
        text: 'Distribución de Avisos de Adopción'
    },
    series: [{
        name: 'Avisos de Adopción',
        data: []
    }],
    tooltip: {
        pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
    }
});

//Bar Chart
Highcharts.chart('container-3', {
    chart: {
        type: 'column'
    },
    title: {
        text: 'Avisos de Adopción por Mes'
    },
    xAxis: {
        categories: ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic'],
        title: {
            text: 'Meses'
        }
        
    },
    yAxis: {
        min: 0,
        title: {
            text: 'Cantidad de Avisos'
        }
    },
   series: [{
        name: 'Gatos',
        data: [] // Initial empty data for cats
    }, {
        name: 'Perros',
        data: [] // Initial empty data for dogs
    }],
    tooltip: {
        shared: true,
        valueSuffix: ' avisos'
    }
});



document.addEventListener("DOMContentLoaded", () => {
  updateLineChart();
  updatePieChart();
  updateBarChart();
});
