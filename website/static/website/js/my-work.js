function handleWorkClick(i) {
    document.getElementById('overlay').classList.toggle('active');
    document.getElementsByTagName('body')[0].style.overflow = "hidden";
    turnOffArticles();
    // turn on work articles with matching id
    document.getElementById('work-articles').children[i].style.display = "block";
}

function turnOffOverlay() {
    pauseVideo();
    var overlay = document.getElementById('overlay');
    if (overlay.className == 'active') {
        overlay.classList.toggle('active');
        document.getElementsByTagName('body')[0].style.overflow = "scroll";
    }
}

function turnOffArticles() {
    var articles = document.getElementById('work-articles').children;
    for (it = 0; it < articles.length; it++) {
        articles[it].style.display = 'none';
    }
}

document.addEventListener('DOMContentLoaded', function() {
    turnOffArticles();

    var workEls = document.getElementsByClassName('worksamplebut');

    for (let i = 0; i < workEls.length; i++) {
        workEls[i].addEventListener('click', function(e) {
            e.preventDefault();
            handleWorkClick(i);
        })
    }

    document.getElementById('work-close').addEventListener('click', function(e) {
        turnOffOverlay();
    })

    document.addEventListener('keydown', function(e) {
        if (e.key === "Escape") {
            turnOffOverlay();
        }
    })
});