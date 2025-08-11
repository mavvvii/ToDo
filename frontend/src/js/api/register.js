import { API_V1_BASE_URL } from './api.js';

export async function registerUser(username, email, password) {
    const response = await fetch(`${API_V1_BASE_URL}/auth/register/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            username: username,
            email: email,
            password: password,
        }),
    });

    const data = await response.json();

    if (!response.ok) {
        const detail = data.detail || 'Unknown error';
        const message = data.message || '';
        const statusCode = response.status;

        throw new Error(`[${statusCode}] ${detail}${message ? ` - ${message}` : ''}`);
    }

    return data;
}
