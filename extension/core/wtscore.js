const ENDPOINT_URL = 'https://firestore.googleapis.com/v1/projects/wikitrustapp/databases/(default)/documents/articles/'

let colorPercentage = (percentage) => {
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
            let trust = 96;
            let author = 96;
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

    // Change trust
    let value = $('#trust-value')
    value.html(trust);

    // Change color
    let left = $('.progress-left .progress-bar')
    let right = $('.progress-right .progress-bar')

    left.css("border-color", color);
    right.css("border-color", color);


    if(trust > 0){
        if(trust <= 50){
            right.css('transform', 'rotate(' + percentageToDegrees(trust) + 'deg)')
        } else {
            right.css('transform', 'rotate(180deg)')
            left.css('transform', 'rotate(' + percentageToDegrees(trust - 50) + 'deg)')
        }
    }
}

// Transform to deg
let percentageToDegrees = (percent) => {return percent / 100 * 360};

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

let requestCrawlPromise = (page) => {
    
}