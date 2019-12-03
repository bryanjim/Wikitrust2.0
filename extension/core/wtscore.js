const ENDPOINT_URL = 'https://firestore.googleapis.com/v1/projects/wikitrustapp/databases/(default)/documents/articles/'

// Entry point of app
window.onload = function(){
    loadDummyScores();
    loadRealScores("HIV");
}

// Preloads ui w/ fake data
let loadDummyScores = () => {
    let props = {
        'overall_trust': 0.00,
        'author_trust': 0.00,
        'moves':  0,
        'insertions': 0,
        'deletes': 0,
        'time': 'Jan 1st 1970 12:00:00'
    }
    updateUI(props);
}

// Fetches data then updates ui
let loadRealScores = (page) => {
    dataPromise(page)
        .then((res) => {

            let props = {
                'overall_trust': getDoubleField(res, "overall_trust"),
                'author_trust': getDoubleField(res, "author_trust"),
                'moves':  getIntField(res, "moves"),
                'insertions': getIntField(res, "insertions"),
                'deletes': getIntField(res, "deletes"),
                'time': getTimestamp(res)
            }

            updateUI(props);
            updateDebug(props);
        });
}

let getTimestamp = (res) => {return res['updateTime'] || '!2:00am Jan 1st'}
let getIntField = (res, id) => {return res['fields'][id]['integerValue'] || 0}
let getDoubleField = (res, id) => {return res['fields'][id]['doubleValue'] || 0.00}

// Just for debugging so we can see the output
let updateDebug = (res) => {
    this.document.getElementById('debug').innerHTML = JSON.stringify(res);
}

// Updates the UI
// Call updateUI(trust, author, moves, ins, dele) with values
let updateUI = (props) => {

    let trust = props['overall_trust'];
    let author = props['author_trust'];
    let moves = props['moves'];
    let insertions = props['insertions'];
    let deletes = props['deletes'];
    let time = props['time'];

    // Change trust
    let value = $('#trust-value')
    let date = getDisplayDate(time);

    value.html(Math.floor(trust));
    $('#author-value').html(author);
    $('#date-posted').html(date);

    // Change color
    let left = $('.progress-left .progress-bar')
    let right = $('.progress-right .progress-bar')

    let hexColor = getColorHex(trust)

    left.css("border-color", hexColor);
    right.css("border-color", hexColor);

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

// gets hexcode
let getColorHex = (percentage) => {
    let r, g, b = 0;
    if (percentage < 50) {
        r = 225;
        g = Math.round(5.1 * percentage);
    } else {
        g = 195;
        r = Math.round(510 - 5.1 * percentage);
    }
    // converts rgb to hex
    let hex = r * 0x10000 + g * 0x100 + b * 0x1;
    return '#' + ('000000' + hex.toString(16)).slice(-6);
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

let requestCrawlPromise = (page) => {
    
}

let getDisplayDate = (date) => {
    today = new Date();
    today.setHours(0);
    today.setMinutes(0);
    today.setSeconds(0);
    today.setMilliseconds(0);
    compDate = new Date(date);
    
    // Gets the difference between today and the date
    diff = today.getTime() - compDate.getTime(); 
    // 24 * 60 * 60 * 1000 represents a day in seconds
    if (compDate.getTime() == today.getTime()) {
        return "Today";
    } else if (diff <= (24 * 60 * 60 *1000)) {
        return "Yesterday";
    } else if (diff <= (29 * 24 * 60 * 60 *1000)) { 
        let days = diff / (24 * 60 * 60 *1000);
        return Math.floor(days) + " days ago"
    } else{
       return "30+ days ago"
    }
}