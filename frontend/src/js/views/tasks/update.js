import { getTask, updateTask } from '../../api/tasks.js';

export function mountUpdateTask() {
  const params = new URLSearchParams(window.location.search);
  const board_id = params.get('board_id');
  const task_id = params.get('task_id');

  const titleInput = document.getElementById('title');
  const descInput = document.getElementById('description');
  const statusInput = document.getElementById('status');
  const completedInput = document.getElementById('completed');

  async function populateForm() {
    const task = await getTask(board_id, task_id);
    titleInput.value = task.title;
    descInput.value = task.description || '';
    statusInput.value = task.status || '';
    completedInput.checked = task.completed;
  }

  populateForm();

  const form = document.getElementById('task-form');
  form.addEventListener('submit', async (e) => {
    e.preventDefault();

    try {
      await updateTask(
        board_id,
        task_id,
        titleInput.value,
        descInput.value,
        statusInput.value,
        completedInput.checked
      );
      alert('Task has beed updated!');
      window.loadView(`./forms/boards/detail.html?id=${board_id}`);
    } catch (err) {
      alert('Error during update: ' + err.message);
    }
  });
}
