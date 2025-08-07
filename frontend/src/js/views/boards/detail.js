import { createApp } from 'https://unpkg.com/petite-vue?module';
import { getBoard } from '../../api/boards.js';
import { getTasks, deleteTask } from '../../api/tasks.js';

export function mountBoardDetail() {
  const app = {
    board: null,
    tasks: [],
    errorMessage: '',
    statuses: ['todo', 'in progress', 'done'],
    selectedStatus: null,

    get filteredTasks() {
      if (!this.selectedStatus) return this.tasks;
      return this.tasks.filter(t => t.status === this.selectedStatus);
    },

    async fetchData() {
      const boardId = window.activeBoard?.id;
      if (!boardId) {
        this.errorMessage = 'No active board!';
        return;
      }

      try {
        this.board = await getBoard(boardId);
      } catch (err) {
        this.errorMessage = 'Error during fetch borad: ' + err.message;
        return;
      }

      try {
        this.tasks = await getTasks(boardId);
      } catch (err) {
        this.errorMessage = 'Error during fetch task: ' + err.message;
      }
    },

    async deleteTask(taskId) {
      if (!confirm('Are you sure you want to delete the task?')) return;
      try {
        await deleteTask(this.board.id, taskId);
        this.tasks = await getTasks(this.board.id);
      } catch (err) {
        console.error('Error during delete task:', err);
      }
    },

    async loadCreateTaskForm() {
      await window.loadView(`./forms/tasks/create.html`);
      const { mountCreateTask } = await import('../tasks/create.js');
      mountCreateTask(this.board.id);
    },

    editTask(task) {
      window.loadView(
        `./forms/tasks/update.html?board_id=${this.board.id}&task_id=${task.id}`
      );
    }
  };

  const vueApp = createApp(app);
  vueApp.mount('#board-detail');
  app.fetchData();
}
