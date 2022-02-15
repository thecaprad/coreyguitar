document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('hamburger').addEventListener('click', function() {
        document.getElementById('links').classList.toggle('active');
        document.getElementById('top-link').classList.toggle('active');
    })
})