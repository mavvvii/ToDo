import { refreshToken } from './refresh-token.js';

const API_V1_BASE_URL = 'http://localhost:8000/api/v1'

function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
    return null;
}

const csrfToken = getCookie('csrftoken');

export async function getBoards() {
    let response = await fetch(`${API_V1_BASE_URL}/boards/`, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
        },
        credentials: 'include',
    });

    if (response.status == 401) {
        await refreshToken();
        await getBoards();
    }

  return await response.json();
}

export async function getBoard(board_id) {
  const response = await fetch(`${API_V1_BASE_URL}/boards/${board_id}`, {
    method: 'GET',
    headers: {
      'Content-Type': 'application/json',
    },
    credentials: 'include',
  });

  if (response.status === 401) {
    await refreshToken();
    return await getBoard(board_id);
  }

  if (!response.ok) {
    const errorData = await response.json();
    throw new Error(errorData.detail || 'Error during get boards!');
  }

  return await response.json();
}

export async function createBoard(title, description) {
  const response = await fetch(`${API_V1_BASE_URL}/boards/`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'X-CSRFToken': csrfToken,
    },
    credentials: 'include',
    body: JSON.stringify({
        title,
        description
    }),
  });

  if (!response.ok) {
    const errorData = await response.json();
    throw new Error(errorData.detail || 'Error during create board!');
  }

  return await response.json();
}

export async function updateBoard(board_id, title, description) {
    const data = {};
    if (title && title.trim() !== '') data.title = title;
    if (description && description.trim() !== '') data.description = description;

    const response = await fetch(`${API_V1_BASE_URL}/boards/${board_id}/`, {
        method: 'PATCH',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken,
        },
        credentials: 'include',
        body: JSON.stringify(
            data,
        ),
    });

    if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.detail || 'Error during update board!');
    }

    return await response.json();
}

export async function deleteBoard(board_id) {
    const response = await fetch(`${API_V1_BASE_URL}/boards/${board_id}/`, {
        method: 'DELETE',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken,
        },
        credentials: 'include',
    });

    if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.detail || 'Error during delete board!');
    }

    return true;
}