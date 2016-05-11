$(document).ready(function () {
    var point = 0;
    var sense = [];
    sense.push([]);
    $("#data").click(
    setInterval(function () {
        $.get("/sensordata", function (data) {
            sense[0].push([point, data]);
            point = point + 1;
            console.log(sense);
            $.plot($("#placeholder"), sense);
        });
    },500)
    );
});