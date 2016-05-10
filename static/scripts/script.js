$(document).ready(function () {
    var point = 0;
    var sense = [];
    $("#data").click(function () {
        $.get("/sensordata", function (data) {
            sense.push([point, data]);
            point = point + 1;
            console.log(sense);
            $.plot($("#placeholder"),sense);
        })
    });
});