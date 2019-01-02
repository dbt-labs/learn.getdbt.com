var ctx = $("#banner");
ctx.height(500);

var t = Date.now();
var chaos = 100;
var charterator = 0;

function randomseries(){
	var points = [];
	for ( var i = 0 ; i < 120 ; i++ ) {
		var rand = 100 + ( 2*i/(chaos) + ( Math.random() - Math.random() ) );
		points.push(rand);
	}
	return points;
}

var scatterChart = new Chart(ctx, {
	type: 'bar',
	data: {
		labels: [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
		datasets: [
			{
				type: 'line',
				data: randomseries(),
				pointBackgroundColor: '#70d4d0',
				pointBorderColor: '#70d4d0',
				backgroundColor: 'transparent',
				borderColor: 'transparent',
				radius: 2,
			},
			{
				type: 'line',
				data: randomseries(),
				pointBackgroundColor: '#0e6b81',
				pointBorderColor: '#0e6b81',
				backgroundColor: 'transparent',
				borderColor: 'transparent',
				borderWidth: 4
			},
			{
				type: 'bar',
				data: randomseries(),
				backgroundColor: '#014963',
			},
		]
	},
	options: {
		scales: {
			xAxes: [{ position: 'bottom', gridLines: { display: false }, ticks: { display: false }, barPercentage: 0.2  }],
			yAxes: [{ display: false }],
		},
		legend: { display: false },
		tooltips: { enabled: false },
		hover: {mode: null},
		maintainAspectRatio: false
	}
});

function mixChart(animate){
	var duration = ( animate ) ? animate : 6000;
	scatterChart.data.datasets[0].data = randomseries();
	scatterChart.data.datasets[2].data = randomseries();
	scatterChart.data.datasets[1].data = randomseries();
	scatterChart.update(duration,true);
}
var timer = setTimeout(function(){ mixChart(); },1000);
setInterval(function(){ mixChart(); },4500);
