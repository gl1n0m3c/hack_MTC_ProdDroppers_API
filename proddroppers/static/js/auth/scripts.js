login_type = "Register"
// Сохранение имени пользователя в sessionStorage

function registerError(error){
    Swal.fire({
        icon: 'error',
        title: 'Ошибка',
        text: error,
        timer: 3000, 
        showConfirmButton: false,
    });
}


function registerSuccess(){
    Swal.fire({
        icon: 'success',
        title: 'Аккаунт зарегистрирован',
        timer: 3000,
        showConfirmButton: false, 
    });
}

function loginSuccess(){
    Swal.fire({
        icon: 'success',
        title: 'Вы успешно вошли в аккаунт',
        timer: 3000,
        showConfirmButton: false, 
    });
}
function login(){
    if (login_type == "Register"){
        registerUser()
    } else {
        loginUser()
    }
}
function loginUser(){
    var email = document.getElementById('email').value;
    var password = document.getElementById('password').value;
    var emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(email)) {
        registerError('Некорректный формат электронной почты');
        return;
    }

    var userData = {
        username: email,
        password: password,
    };

    var xhr = new XMLHttpRequest();
    xhr.open('POST', 'http://127.0.0.1:8000/auth/login/', true);
    xhr.setRequestHeader('Content-Type', 'application/json');

    xhr.onreadystatechange = function () {
        if (xhr.readyState == 4) {
            // var jsonResponse = JSON.parse(xhr.responseText);
            if (xhr.status == 200 || xhr.status == 201) {
                // registerSuccess();
                loginSuccess();
                var jsonResponse = JSON.parse(xhr.responseText);
                sessionStorage.setItem('userid', jsonResponse.id);
                // file:///C:/Users/Juonior/Desktop/templates/profile/index.html
                window.location.pathname = "////C:/Users/Juonior/Desktop/templates/profile/index.html";
            } else {
                var jsonResponse = JSON.parse(xhr.responseText);
                registerError(jsonResponse.description);
            }
        }
    };
    var jsonData = JSON.stringify(userData);

    // Send the request with the JSON data
    xhr.send(jsonData);
}
function registerUser() {
    var email = document.getElementById('email').value;
    var password = document.getElementById('password').value;
    var password2 = document.getElementById('password2').value;

    var emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

    if (!emailRegex.test(email)) {
        registerError('Некорректный формат электронной почты');
        return;
    }

    if (password !== password2) {
        registerError('Пароли не совпадают');
        return;
    }
    var passwordRegex = /^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$/;

    if (!passwordRegex.test(password)) {
        registerError('Пароль должен содержать не менее 8 символов, хотя бы одну букву, одну цифру и один спецсимвол');
        return;
    }

    var userData = {
        email: email,
        password: password,
    };

    var xhr = new XMLHttpRequest();
    xhr.open('POST', 'http://127.0.0.1:8000/auth/register/', true);
    xhr.setRequestHeader('Content-Type', 'application/json');

    xhr.onreadystatechange = function () {
        if (xhr.readyState == 4) {
            if (xhr.status == 200 || xhr.status == 201) {
                registerSuccess();
            } else {
                var jsonResponse = JSON.parse(xhr.responseText);
                registerError(jsonResponse.description);
            }
        }
    };
    var jsonData = JSON.stringify(userData);

    // Send the request with the JSON data
    xhr.send(jsonData);
}
document.getElementById('enter_btn').addEventListener('click', function() {
    document.getElementById('reg_label').style.color = "gray";
    document.getElementById('login_btn').value = "Войти"
    document.getElementById('enter_btn').style.color = "black";
    document.getElementById('password2').style.display = "None";
    document.getElementById('accounts_label').style.display = "None";
    login_type = "Login"
});

document.getElementById('reg_label').addEventListener('click', function() {
    document.getElementById('reg_label').style.color = "black";
    document.getElementById('login_btn').value = "Зарегистрироваться"
    document.getElementById('enter_btn').style.color = "gray";
    document.getElementById('password2').style.display = "flex";
    document.getElementById('accounts_label').style.display = "inline";
    login_type = "Register"
});

