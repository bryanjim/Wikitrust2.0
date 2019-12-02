<<<<<<< HEAD
const ENDPOINT_URL = 'https://firestore.googleapis.com/v1/projects/wikitrustapp/databases/(default)/documents/articles/'

let colorPercentage = (percentage) => {
=======
function colorPercentage(percentage) {
>>>>>>> 0d8363e6d43040b8404e6c6964255992a19764c6
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

<<<<<<< HEAD
// Entry point of app
window.onload = function(){
    loadDummyScores();
    loadRealScores("837852180");
}

// Preloads ui w/ fake data
let loadDummyScores = () => {updateUI("Loading...", "Loading...", colorPercentage(0));}

// Fetches data then updates ui
let loadRealScores = (page) => {
    dataPromise(page)
        .then((res) => {
            let trust = 101;
            let author = 101;
            let color = colorPercentage(trust)
            updateUI(trust, author, color);
            updateDebug(res);
        });
}


// Just for debugging so we can see the output
let updateDebug = (res) => {
    this.document.getElementById('debug').innerHTML = JSON.stringify(res);
}

// Updates the UI
// Call updateUI(trust, author, color) with values
let updateUI = (trust, author, color) => {
    // Update text
    this.document.getElementById('trust-score').innerHTML = trust;
    this.document.getElementById('author-score').innerHTML = author;

    // Update color
    let gradient = this.document.getElementById('gradient');
    gradient.style.backgroundColor = color;
    gradient.style.background = 'linear-gradient' + '(to right,' + color + ', #fef9ee)';
}

// Promise for data
// dataPromise.then(data => use(data))
let dataPromise = (page) => {
    return new Promise((resolve, reject) => {
        fetch(ENDPOINT_URL + page)
        .then(res => {
            if(!res.ok) reject("error"); 
            else return res})
        .then(res => res.json())
        .then(res => resolve(res));
    })
}
=======
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
>>>>>>> 0d8363e6d43040b8404e6c6964255992a19764c6
