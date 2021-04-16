function handleWorkClick(i) {
    document.getElementById('overlay').classList.toggle('active');
    var marquee = document.getElementById('marquee');
    marquee.classList.toggle('active');
    turnOffMarqueeChildren();
    // turn on work sample with matching id
    marquee.children[i].style.display = "block";
}

function turnOffMarquee() {
    document.getElementById('overlay').classList.toggle('active');
    document.getElementById('marquee').classList.toggle('active');
    turnOffMarqueeChildren();
}

function turnOffMarqueeChildren() {
    for (it = 0; it < marquee.children.length; it++) {
        marquee.children[it].style.display = "none";
    }
}

document.addEventListener('DOMContentLoaded', function() {
    var workEls = document.getElementsByClassName('worksamplebut');

    for (let i = 0; i < workEls.length; i++) {
        workEls[i].addEventListener('click', function() {
            handleWorkClick(i);
        })
    }

    var xEls = document.getElementsByClassName('x');
    for (let i = 0; i < workEls.length; i++) {
        xEls[i].addEventListener('click', function() {
            document.getElementById('overlay').classList.toggle('active');
            document.getElementById('marquee').classList.toggle('active');
            allMarqueeChildrenOff();
        })
    }
});