function colorPercentage(percentage) {
    let r, g, b = 0;
    if (percentage < 50) {
        r = 225;
        g = Math.round(5.1 * percentage);
    } else {
        g = 225;
        r = Math.round(510 - 5.1 * percentage);
    }
    // converts rgb to hex
    let hex = r * 0x10000 + g * 0x100 + b * 0x1;
    return '#' + ('000000' + hex.toString(16)).slice(-6);
}

function getTrustScore() {
    let trust = Math.floor(Math.random() * 100) + 1;
    // This is just to test the background/border color using JS
    return trust;
}


$(function () {
    let value = getTrustScore();
    var trustColor = colorPercentage(value);

    $(".progress").each(function () {
        $(this).find('#trust-value').append(value);
        var left = $(this).find('.progress-left .progress-bar');
        var right = $(this).find('.progress-right .progress-bar');
        left.css("border-color", trustColor);
        right.css("border-color", trustColor);


        if (value > 0) {
            if (value <= 50) {
                right.css('transform', 'rotate(' + percentageToDegrees(value) + 'deg)')
            } else {
                right.css('transform', 'rotate(180deg)')
                left.css('transform', 'rotate(' + percentageToDegrees(value - 50) + 'deg)')
            }
        }

    })

    function percentageToDegrees(percentage) {

        return percentage / 100 * 360

    }

});