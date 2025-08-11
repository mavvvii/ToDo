import { API_V1_BASE_URL } from './api.js';

export async function loginUser(username, password, remember_me) {
    const response = await fetch(`${API_V1_BASE_URL}/auth/login/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        credentials: 'include',
        body: JSON.stringify({
            username,
            password,
            remember_me,
        }),
    });

    const data = await response.json();

    if (response.ok) {
        window.location.href = 'dashboard.html';

        return data;
    } else {
        const detail = data.detail || 'Unknown error';
        const message = data.message || '';
        const statusCode = response.status;

        throw new Error(`[${statusCode}] ${detail}${message ? ` - ${message}` : ''}`);
    }
}
