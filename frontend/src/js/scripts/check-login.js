async function checkIfLoggedIn() {
  try {
    const response = await fetch('http://localhost:8000/api/v1/profile/', {
      credentials: 'include',
    });

    if (response.ok) {
      window.location.href = 'dashboard.html';
    }
  } catch (err) {
    console.error('Błąd sprawdzania sesji:', err);
    loadView('./forms/login.html');
  }
}
