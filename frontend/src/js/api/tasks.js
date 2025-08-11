import { refreshToken } from './refresh-token.js';
import { getCsrfToken } from '../scripts/get-csrf-token.js';
import { API_V1_BASE_URL } from './api.js';

const csrfToken = getCsrfToken();

export async function getTasks(board_id, isRetry = false) {
    const response = await fetch(`${API_V1_BASE_URL}/boards/${board_id}/tasks/`, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
        },
        credentials: 'include',
    });

    if (response.status == 401 && !isRetry) {
        await refreshToken();
        return await getTasks(board_id, true);
    }

    if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.detail || 'Error during get tasks!');
    }

  return await response.json();
}

export async function getTask(board_id, task_id, isRetry = false) {
  const response = await fetch(`${API_V1_BASE_URL}/boards/${board_id}/tasks/${task_id}/`, {
    method: 'GET',
    headers: {
      'Content-Type': 'application/json',
    },
    credentials: 'include',
  });

  if (response.status === 401 && !isRetry) {
    await refreshToken();
    return await getTask(board_id, task_id, true);
  }

  if (!response.ok) {
    const errorData = await response.json();
    throw new Error(errorData.detail || 'Error during get task!');
  }

  return await response.json();
}

export async function createTask(board_id, title, description, isRetry = false) {
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

  if (response.status === 401 && !isRetry) {
    await refreshToken();
    return await createTask(board_id, title, description, true);
  }

  if (!response.ok) {
    const errorData = await response.json();
    throw new Error(errorData.detail || 'Error during create task!');
  }

  return await response.json();
}

export async function updateTask(board_id, task_id, title, description, status, completed, isRetry = false) {
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

    if (response.status === 401 && !isRetry) {
      await refreshToken();
      return await updateTask(board_id, task_id, title, description, status, completed, true);
    }

    if (!response.ok) {
      const errorData = await response.json();
      throw new Error(errorData.detail || 'Error during update task!');
    }

    return await response.json();
}

export async function deleteTask(board_id, task_id, isRetry = false) {
    const response = await fetch(`${API_V1_BASE_URL}/boards/${board_id}/tasks/${task_id}/`, {
        method: 'DELETE',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken,
        },
        credentials: 'include',
    });

    if (response.status === 401 && !isRetry) {
        await refreshToken();
        return await deleteTask(board_id, task_id, true);
    }

    if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.detail || 'Error during delete task!');
    }

    if (response.status === 204) {
      return;
    }

    return await response.json();
}
