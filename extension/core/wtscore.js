function colorPercentage(percentage){
    let r, g, b = 0;
    if (percentage < 50){
        r = 255;
        g = Math.round(5.1 * percentage);
    }else{
        g = 255;
        r = Math.round(510 - 5.1 * percentage);
    }
    // converts rgb to hex
    let hex = r * 0x10000 + g * 0x100 + b *0x1;
    return '#' + ('000000' + hex.toString(16)).slice(-6);
}

function getTrustScore(){
    let trust = Math.floor(Math.random() * 100) + 1;
    return trust;
}

window.onload = function(){
    score = this.getTrustScore();
    color = this.colorPercentage(score);
    let gradient = this.document.getElementById('gradient')

    gradient.style.backgroundColor = color
    gradient.style.background = 'linear-gradient' + '(to right,' + color + ', #fef9ee)';
    this.document.getElementById('trust-score').innerHTML = this.score;
    this.document.getElementById('author-score').innerHTML = this.getTrustScore();

}