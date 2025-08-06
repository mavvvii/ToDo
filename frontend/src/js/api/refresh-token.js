const API_V1_BASE_URL = 'http://localhost:8000/api/v1'

export async function refreshToken() {
    console.log('Calling refreshToken()');
    try {
        const response = await fetch(`${API_V1_BASE_URL}/token/refresh/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            credentials: 'include',
            body: JSON.stringify({})  // Pusty body musi być
        });
        console.log('refreshToken response status:', response.status);
        if (!response.ok) {
            const text = await response.text();
            console.error('Token refresh failed:', text);
            throw new Error('Token refresh failed');
        }
        const data = await response.json();
        console.log('refreshToken data:', data);
        return data;
    } catch (error) {
        console.error('refreshToken error:', error);
        throw error;
    }
}