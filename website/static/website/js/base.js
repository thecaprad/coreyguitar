document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('hamburger').addEventListener('click', function() {
        document.getElementById('links').classList.toggle('active');
    })
})