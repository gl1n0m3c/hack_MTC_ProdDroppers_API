var lines = document.querySelectorAll('.line');
function updateEqualizer() {
    lines.forEach(function(line) {
        const newHeight = (Math.floor(Math.random() * (150 - 20 + 1)) + 20 )/10;
        line.style.height = `${newHeight}vh`;;
    });
}
setInterval(updateEqualizer, 800);


login_type = "Register"

document.getElementById('login_btn').addEventListener('click', function() {
    document.getElementById('reg_btn').style.color = "gray";
    document.getElementById('enter').innerHTML = "Войти"
    document.getElementById('login_btn').style.color = "black";
    document.getElementById('password2').style.display = "None";
    document.getElementById('account_label').innerHTML = "Нет аккаунта?";
    document.getElementById('account_btn').innerHTML = "Зарегистрироваться";
    login_type = "Login"
});



document.getElementById('reg_btn').addEventListener('click', function() {
    document.getElementById('login_btn').style.color = "gray";
    document.getElementById('enter').innerHTML = "Зарегистрироваться"
    document.getElementById('reg_btn').style.color = "black";
    document.getElementById('password2').style.display = "inline";
    document.getElementById('account_label').innerHTML = "Уже есть аккаунт?";
    document.getElementById('account_btn').innerHTML = "Войти";
    login_type = "Login"
});