document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('work-1').addEventListener('click', function() {
        document.getElementById('overlay').classList.toggle('active');
        document.getElementsByClassName('marquee')[0].classList.toggle('active');
    })
    document.getElementsByClassName('x')[0].addEventListener('click', function() {
        document.getElementById('overlay').classList.toggle('active');
        document.getElementsByClassName('marquee')[0].classList.toggle('active');
    })
});