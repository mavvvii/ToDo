import { refreshToken } from './refresh-token.js';

const API_V1_BASE_URL = 'http://localhost:8000/api/v1'

function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
    return null;
}

const csrfToken = getCookie('csrftoken');

export async function getTasks(board_id) {
    const response = await fetch(`${API_V1_BASE_URL}/boards/${board_id}/tasks`, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
        },
        credentials: 'include',
    });

    if (response.status == 401) {
        await refreshToken();
        return await getTasks(board_id);
    }

  return await response.json();
}

export async function getTask(board_id, task_id) {
  const response = await fetch(`${API_V1_BASE_URL}/boards/${board_id}/task/${task_id}`, {
    method: 'GET',
    headers: {
      'Content-Type': 'application/json',
    },
    credentials: 'include',
  });

  if (response.status === 401) {
    await refreshToken();
    return await getTask(board_id);
  }

  if (!response.ok) {
    const errorData = await response.json();
    throw new Error(errorData.detail || 'Error during get tasks!');
  }

  return await response.json();
}

export async function createTask(board_id, title, description) {
  const response = await fetch(`${API_V1_BASE_URL}/boards/${board_id}/tasks/`, {
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
    throw new Error(errorData.detail || 'Error during create task!');
  }

  return await response.json();
}

export async function updateTask(board_id, task_id, title, description, status, completed) {
    const data = {};
    if (title && title.trim() !== '') data.title = title;
    if (description && description.trim() !== '') data.description = description;
    if (status && status.trim() !== '') data.status = status;
    if (completed && completed.trim() !== '') data.completed = completed;


    const response = await fetch(`${API_V1_BASE_URL}/boards/${board_id}/tasks/${task_id}/`, {
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
        throw new Error(errorData.detail || 'Error during update task!');
    }

    return await response.json();
}

export async function deleteTask(board_id, task_id) {
    const response = await fetch(`${API_V1_BASE_URL}/boards/${board_id}/tasks/${task_id}`, {
        method: 'DELETE',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken,
        },
        credentials: 'include',
    });


    if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.detail || 'Error during delete task!');
    }

    return true;
}