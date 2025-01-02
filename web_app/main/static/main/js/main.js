document.getElementById('registrationForm').addEventListener('submit', function(event) {
    event.preventDefault(); // предотвращаем отправку формы

    const username = document.getElementById('username').value;
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;

    this.reset();
});


function redirectToLogin() {
    window.location.href = '/login'; // '/login' дописать страницу 
}
