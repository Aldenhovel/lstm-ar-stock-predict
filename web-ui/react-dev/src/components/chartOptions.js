const option = {
    animation: true,
    animationDuration:200,
    animationDurationUpdate:200,
    dataZoom: [
        {
            show: true,
            type: 'slider',

            bordered: '50px',
            start: 0,
            end: 100
        }
    ],
    tooltip: {
        axisPointer: {
            type: 'cross'
        }
    },
    xAxis: {
        data: ['2017-10-24', '2017-10-25', '2017-10-26', '2017-10-27', '+1', '+2']
    },
    yAxis: {
        min: 'dataMin',
        max: 'dataMax'
    },
    series: [
        {
            type: 'candlestick',
            data: [
                [20, 34, 10, 38],
                [40, 35, 30, 50],
                [31, 38, 33, 44],
                [38, 15, 5, 42]
            ]
        },
        {
            type: 'line',
            data: [undefined, undefined, undefined, undefined, 38, 42],

        }
    ]
};

export {option as defaultGreedySearchOption, option as defaultBeamSearchOption};