const API_V1_BASE_URL = 'http://localhost:8000/api/v1'

export async function login(username, password, remember_me) {
    const response = await fetch(`${API_V1_BASE_URL}/auth/login/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        credentials: 'include',
        body: JSON.stringify({
            username: username,
            password: password,
            remember_me: remembe_me,
        }),


});

const result = await response.json();
    if (response.ok) {
        const csrfToken = result.data.csrf_token;

        if (remember_me) {
            localStorage.setItem('csrf_token', csrfToken);
        }else {
            sessionStorage.setItem('csrf_token', csrfToken);
        }

        console.log('Login successful');
    } else {
        console.error(result.data);
    }
}
