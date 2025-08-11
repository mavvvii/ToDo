import { API_V1_BASE_URL } from '../api/api.js';

async function checkIfLoggedIn() {
  try {
    const response = await fetch(`${API_V1_BASE_URL}/users/profile/`, {
      credentials: 'include',
    });

    if (response.ok) {
      window.location.href = 'dashboard.html';
    }
  } catch (err) {
    loadView('./forms/login.html');
  }
}
