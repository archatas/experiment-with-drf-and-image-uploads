let userToken;

document.getElementById('login_form').addEventListener('submit', function(event) {
    event.preventDefault();
    let email = document.getElementById('id_email').value;
    let password = document.getElementById('id_password').value;

    fetch('http://127.0.0.1:8000/api/auth-token/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            "username": email,
            "password": password,
        })
    }).then( response => {
        return response.json();
    }).then(data => {
        console.log(data);
        userToken = data.token;
        console.log('Logged in. Got the token.');
    }).catch((error) => {
        console.error('Error:', error);
    });
});

document.getElementById('avatar_form').addEventListener('submit', function(event) {
    event.preventDefault();
    let input = document.getElementById('id_avatar');

    let data = new FormData();
    data.append('avatar', input.files[0]);

    fetch('http://127.0.0.1:8000/api/user-avatar/', {
        method: 'POST',
        headers: {
            'Authorization': `Token ${userToken}`
        },
        body: data
    }).then(response => {
        return response.json();
    }).then(data => {
        console.log(data);
    }).catch((error) => {
        console.error('Error:', error);
    });
});