
userid = sessionStorage.getItem('userid');
var xhr = new XMLHttpRequest();

// Настройка запроса (GET-запрос по указанному URL)
xhr.open('GET', 'http://127.0.0.1:8000/users/profile/'+userid+'/', true);

// Установка обработчика события загрузки
xhr.onload = function () {
  if (xhr.status >= 200 && xhr.status < 300) {
    // Обработка данных в формате JSON
    var responseData = JSON.parse(xhr.responseText);
    console.log(responseData);
    var usernameHeadings = document.querySelectorAll('[id="username"]');
    usernameHeadings.forEach(function (heading) {
        heading.textContent = responseData.username; // Замените "Новое значение" на ваше новое значение
    });

    var usernameHeadings = document.querySelectorAll('[id="email"]');
    usernameHeadings.forEach(function (heading) {
        heading.textContent = responseData.email; // Замените "Новое значение" на ваше новое значение
    });
  } else {
    // Обработка ошибок
    alert('There was a problem with the request:', xhr.statusText);
  }
};

// Отправка запроса
xhr.send();


document.addEventListener('DOMContentLoaded', function () {
    // Получаем элементы с классами Lines и navigation-bar
    var linesElement = document.querySelector('.Lines');
    var navigationBarElement = document.querySelector('.navigation-bar');

    // Добавляем переменную для отслеживания состояния
    var isNavigationBarVisible = false;

    // Добавляем обработчик события для клика на элемент с классом Lines
    linesElement.addEventListener('click', function () {
        // Изменяем состояние переменной и свойство display соответственно
        if (isNavigationBarVisible) {
            navigationBarElement.style.display = 'none';
        } else {
            navigationBarElement.style.display = 'flex';
        }

        // Инвертируем значение переменной
        isNavigationBarVisible = !isNavigationBarVisible;
    });
});
