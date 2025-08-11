import { API_V1_BASE_URL } from './api.js';

export async function refreshToken() {
    try {
        const response = await fetch(`${API_V1_BASE_URL}/token/refresh/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            credentials: 'include',
            body: JSON.stringify({})
        });

        if (!response.ok) {
            throw new Error('Token refresh failed');
        }

        return await response.json();

    } catch (error) {
        throw error;
    }
}
