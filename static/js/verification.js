function hidefields(fields) {
    for (i = 0; i < fields.length; i++) {
        $(fields[i]).hide();
    }
}

function renderResponse(i, len, data) {
    setTimeout(function () {
        count = i + 1;
        total = len - 1;
        message = data.name;
        value = data.status;
        if (i != len - 1) {
            $("#progress-msg").html($("#progress-msg").html() + 'Шаг ' + count.toString() + ' из ' + total.toString() + "... " + message + '</span>');
        }
        setTimeout(function () {
            if (i == len - 1) {
                if (value == "passed" || value == "done") {
                    $("#progress-msg").html($("#progress-msg").html() + "Проверка прошла успешно!")
                    $("#verified").show();
                }
                else {
                    $("#progress-msg").html($("#progress-msg").html() + "Провал!")
                    $("#not-verified").show();
                }
            }
            else {
                $("#progress-msg").html($("#progress-msg").html() + ' [' + markMappings[value] + ']<br>')
            }
        }, 1000)

    }, timeDelay * i);
}

timeDelay = 2000;
markMappings = {"passed": "Успешно", "failed": "Провал", "done": "Закончен", "not_started": "Не начат"}

$(document).ready(function () {
    $("#verify-button").on('click',function () {
        hidefields(["#not-verified", "#verified"]);
        $("#progress-msg").html("");
        var data = $(this).attr('value');
        var uid = JSON.parse(data.replace(/'/g, '"')).uid;
        $.get("/verify/" + uid, function (res) {
            res = JSON.parse(res);
            $("#progress-msg").show();
            if (res == null) {
                $("#progress-msg").html($("#progress-msg").html() + "Oops! There was an issue connecting to the Blockchain.info API")
            }
            else {
                for (i = 0; i < res.length; i++) {
                    renderResponse(i, res.length, res[i])
                }
            }
        });
    });
});
