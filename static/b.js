var chart = null; 
var data = {};
$(document).ready(function () {
    $.get({
        url: '/get_data/',
        'success': function (point) {
            data = point;
        },
    });
    chart = chartfunc();
    chart.credits.update({
				text: 'jimmyzhang',
				href: 'https://www.cnblogs.com/jimmyzhang2020/',
			});
    return data;
});


function chartfunc(){
    chart = Highcharts.chart('container', {
        chart: {
            type: 'spline',
        },
        title: {
            text: '新冠肺炎患者动态走势图'
        },
        xAxis: {
            type: 'category',
        },
        yAxis: {
            minPadding: 0.2,
            maxPadding: 0.2,
            title: {
                text: '患者人数',
                margin: 80
            }
        },
        series: [{
            name: '每日新增',
            data: []
        },
            {
                name: '累计确诊',
                data: []
            },{
                name: '累计疑似病例',
                data: []
            },{
                name: '累计治愈病例',
                data: []
            }
            ]
    });
    return chart;
}


$('#button').click(function () {
    var req_data = data;
    
    var index=0;
    var handler = setInterval(function () {
        funt();
    },500);
    function funt() {
        if(index<req_data['today'].length){
        index++;
        if(index>=req_data['today'].length){
            clearInterval(handler); 
        }
        chart.series[0].addPoint(req_data['today'][index]);
        chart.series[1].addPoint(req_data['total'][index]);
        chart.series[2].addPoint(req_data['total_sus'][index]);
        chart.series[3].addPoint(req_data['total_heal'][index]);

    }
    }
});
