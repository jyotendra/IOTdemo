$(document).ready(function () {
    var point = 0;
    var sense = [];
    sense.push([]);
    var placeholder = $("#placeholder");
    var markings = [{ color: '#000', lineWidth: 1, yaxis: { from: 800, to: 800} },
        { color: '#000', lineWidth: 1, yaxis: { from: 100, to: 100}}];

    var o;
    $("#data").click(
    setInterval(function () {
        $.get("/sensordata", function (data) {
            sense[0].push([point, data]);
            point = point + 1;
            console.log(sense);
            var plot = $.plot(placeholder, sense, {
                xaxis: { ticks: [], autoscaleMargin: 0.02 },
                yaxis: { min: 0, max: 1023 },
                grid: { markings: markings }
            });
            o = plot.pointOffset({ x: 0, y: 999 });
            placeholder.append('<div style="position:absolute;left:' + (o.left + 4) + 'px;top:' + o.top + 'px;color:#666;font-size:smaller">Pitch Dark</div>');
            o = plot.pointOffset({ x: 0, y: 100 });
            placeholder.append('<div style="position:absolute;left:' + (o.left + 4) + 'px;top:' + o.top + 'px;color:#666;font-size:smaller">Very Bright</div>'); 

        });
    }, 500)
    );
});