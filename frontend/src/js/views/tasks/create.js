import { createTask } from '../../api/tasks.js';
import { createApp } from 'https://unpkg.com/petite-vue?module';

export function mountCreateTask(board_id) {
  if (!board_id) {
    return;
  }

  createApp({
    title: '',
    description: '',
    board_id,
    errorMessage: '',
    showModal: false,
    modalTitle: '',
    modalMessage: '',

    closeModal() {
      this.showModal = false;
    },

    openModal(title, message) {
      this.modalTitle = title;
      this.modalMessage = message;
      this.showModal = true;
    },

    closeCreateView() {
      const container = document.getElementById('content-area');
      if (container) {
        container.innerHTML = '';
      }
    },

    async save() {
      try {
        this.errorMessage = '';
        if (!this.title.trim()) {
          this.errorMessage = 'Title is required';
          return;
        }

        await createTask(board_id, this.title, this.description);
        this.openModal('Success', `Task "${this.title}" has been created!`);
        this.title = '';
        this.description = '';
      } catch (err) {
        this.openModal('Error', err.message || 'Unknown error');
      }
    },

  }).mount('#task-create');
}
