google.charts.load('current', {'packages':['corechart']});
google.charts.setOnLoadCallback(drawChart);


async function drawChart() {
    let name = document.body.className
    content = await (await fetch(`/graphics/${name}`, {method: 'get'})).json()
    console.log(content)
    
    // .forEach(element => {
    //     console.log(element)
    // });
    
    var data = google.visualization.arrayToDataTable(content)

    var options = {
        title: `${name} graphic`,
        curveType: 'function',
        legend: { position: 'bottom' }
};

var chart = new google.visualization.LineChart(document.getElementById('curve_chart'));

chart.draw(data, options);
}

// ['Year', 'Sales'],
// ['2004',  1000,   ],
// ['2005',  1170, ],
// ['2006',  660, ],
// ['2007',  1030]