import { createApp } from 'https://unpkg.com/petite-vue?module';
import { getBoard } from '../../api/boards.js';
import { getTasks, updateTask } from '../../api/tasks.js';

export function mountBoardDetail() {
  const app = {
    board: null,
    tasks: [],
    errorMessage: '',
    statuses: ['todo', 'in progress', 'done'],
    selectedStatus: null,

    sortKey: 'created_at',
    sortOrder: 'desc',

    get filteredTasks() {
      let result = this.tasks;

      if (this.selectedStatus) {
        result = result.filter(t => t.status === this.selectedStatus);
      }

      return result.slice().sort((a, b) => {
        const dateA = a[this.sortKey] ? new Date(a[this.sortKey]) : null;
        const dateB = b[this.sortKey] ? new Date(b[this.sortKey]) : null;

        if (!dateA && !dateB) return 0;
        if (!dateA) return this.sortOrder === 'asc' ? -1 : 1;
        if (!dateB) return this.sortOrder === 'asc' ? 1 : -1;

        return this.sortOrder === 'asc' ? dateA - dateB : dateB - dateA;
      });
    },

    setSort(key, order) {
      this.sortKey = key;
      this.sortOrder = order;
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

    async updateTaskStatus(taskId, status) {
      try {
        const task = this.tasks.find(t => t.id === taskId);

        if (!task) throw new Error('Task not found');

        await updateTask(this.board.id, taskId, null, null, status, null);
        await this.fetchData();

      } catch (err) {
        console.error('Error during update task status:', err);
      }

    },

    async loadCreateTaskForm() {
      await window.loadView(`./forms/tasks/create.html`);
      const { mountCreateTask } = await import('../tasks/create.js');

      mountCreateTask(this.board.id, (newTask) => {
        this.tasks.push(newTask);
      });
    },

    async loadUpdateTaskForm(taskId) {
      const task = this.tasks.find(t => t.id === taskId);

      await window.loadView(`./forms/tasks/update.html`);
      const { mountUpdateTask } = await import('../tasks/update.js');

      mountUpdateTask(this.board.id, task, async (updatedTask) => {
        await this.fetchData();
      });
    },

    async loadDeleteTaskForm(taskId) {
      const task = this.tasks.find(t => t.id === taskId);
      if (!task) {
        console.error('Task not found for deletion:', taskId);
        return;
      }

      await window.loadView(`./forms/tasks/delete.html`);
      const { mountDeleteTask } = await import('../tasks/delete.js');

      mountDeleteTask(this.board.id, task.id, task.title, (deletedTaskId) => {
        this.tasks = this.tasks.filter(t => t.id !== deletedTaskId);
      });
    },
  };

  const vueApp = createApp(app);
  vueApp.mount('#board-detail');

  app.fetchData();
}
