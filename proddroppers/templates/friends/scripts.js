var lines = document.querySelectorAll('.line');
function updateEqualizer() {
    lines.forEach(function(line) {
        const newHeight = (Math.floor(Math.random() * (150 - 20 + 1)) + 20 )/10;
        line.style.height = `${newHeight}vh`;;
    });
}
setInterval(updateEqualizer, 800);