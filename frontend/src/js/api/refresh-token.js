const API_V1_BASE_URL = 'http://localhost:8000/api/v1'

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
            const text = await response.text();
            throw new Error('Token refresh failed');
        }
        const data = await response.json();
        return data;
    } catch (error) {
        throw error;
    }
}