$(function(){
    "use strict";
    $(document).ready(function() {
        // Bar Chart 2
        function d2c_barChart_2() {
            var options = {
                chart: {
                    type: 'bar',
                    toolbar: {
                        show: false,
                    },
                },
                series: [{
                        name: 'Income',
                        data: [80, 85, 105, 100, 92, 80, 120, 102, 98, 45, 92, 82],
                    },
                    {
                        name: 'Expense',
                        data: [60, 65, 60, 80, 80, 60, 85, 47, 65, 25, 86, 62],
                    }
                ],
                colors: ['#6F6AF8', '#1C1955'],
                legend: {
                    show: false,
                    position: 'top',
                    horizontalAlign: 'right',
                },
                title: {
                    text: "",
                    align: 'left',
                    margin: 0,
                    offsetX: 0,
                    offsetY: 15,
                    floating: false,
                    style: {
                        fontSize: '18px',
                        fontWeight: 'bold',
                        color: '#263238'
                    },
                },
                plotOptions: {
                    heatmap: {
                        radius: 30,
                    }
                },
                dataLabels: {
                    enabled: false,
                },
                yaxis: {
                    lines: {
                        show: false,
                    }
                },
                xaxis: {
                    categories: ["Jan", "Feb", "Marc", "April", "May", "Jun", "July", "Aug", "Sep", "Oct", "Nov", "Dec"]
                },
                plotOptions: {
                    bar: {
                        borderRadius: 10,
                    },
                }
            }

            var chart = new ApexCharts(document.querySelector("#bar-Chart-2"), options);

            chart.render();
        }
        d2c_barChart_2();

    })
})

// Line Chart 2
function d2c_lineChart_2() {
    var options = {
        series: [{
                name: "Session Duration",
                data: [45, 52, 38, 24, 33, 26, 21, 20, 6, 8, 15, 10]
            },
            {
                name: 'Total Visits',
                data: [87, 57, 74, 99, 75, 38, 62, 47, 82, 56, 45, 47]
            }
        ],
        chart: {
            type: 'line',
            zoom: {
                enabled: false
            },
            toolbar: {
                show: false
            },
        },
        colors: ['#EF233C', '#686699'],
        dataLabels: {
            enabled: false
        },
        markers: {
            size: 2,
        },
        stroke: {
            width: 2,
            curve: 'smooth',
            dashArray: [0, 4]
        },
        legend: {
            show: false
        },
        markers: {
            size: 0,
            hover: {
                sizeOffset: 2
            }
        },
        xaxis: {
            categories: ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'],
        },
        grid: {
            borderColor: '#f1f1f1',
        }
    };

    var chart = new ApexCharts(document.querySelector("#dashboard-line-Chart"), options);
    chart.render();
}
d2c_lineChart_2();

// Area Chart
function d2c_areaChart_2() {
    var options = {
        series: [{
                name: 'South',
                data: [30, 80, 82, 56, 58, 130, 80, 90, 64, 27, 94, 100],
            },
            {
                name: 'North',
                data: [100, 20, 45, 15, 60, 5, 85, 95, 5, 34, 80, 105],
            }
        ],
        chart: {
            type: 'area',
            height: 350,
            stacked: true,
            toolbar: {
                show: false,
            }
        },
        colors: ['rgba(103, 58, 183, 0.8)', 'rgba(63, 81, 181, 0.8)'],
        dataLabels: {
            enabled: false
        },
        stroke: {
            curve: 'smooth'
        },
        fill: {
            type: 'gradient',
            gradient: {
                opacityFrom: 0.6,
                opacityTo: 1,
            }
        },
        legend: {
            show: false
        },
        xaxis: {
            type: 'Month',
            categories: ["Jan", "Feb", "Marc", "April", "May", "Jun", "July", "Aug", "Sep", "Oct", "Nov", "Dec"]
        },
    };

    var chart = new ApexCharts(document.querySelector("#dashboard-area-chart"), options);
    chart.render();
}
d2c_areaChart_2();

// Pai Chart 2
function d2c_paiChart_2() {
    var options = {
        series: [82, 18],
        chart: {
            type: 'pie',
        },
        colors: ['#1C1955', '#686699'],
        labels: ["Positive", "Negative"],
        dataLabels: {
            formatter(val, opts) {
                const name = opts.w.globals.labels[opts.seriesIndex]
                return [name, val.toFixed(1) + '%']
            }
        },
        responsive: [{
            breakpoint: 480,
            options: {
              legend: {
                show: false
              }
            }
        }],
        legend: {
            position: 'top',
            horizontalAlign: 'left',   
        },
    };

    var chart = new ApexCharts(document.querySelector("#dashboard-pai-Chart"), options);
    chart.render();
}
d2c_paiChart_2();

// Pai Chart
function d2c_paiChart() {
    var options = {
        series: [42, 33, 24],
        chart: {
            type: 'pie',
        },
        colors: ['#6F6AF8', '#1C1955', '#FFC107'],
        labels: ["Refund", "Margin", "Sale"],
        dataLabels: {
            formatter(val, opts) {
                const name = opts.w.globals.labels[opts.seriesIndex]
                return [name, val.toFixed(1) + '%']
            }
        },
        legend: {
            position: 'top',
            horizontalAlign: 'left',   
        },
    };

    var chart = new ApexCharts(document.querySelector("#dashboard-product-sold-pai-Chart"), options);
    chart.render();
}
d2c_paiChart();

