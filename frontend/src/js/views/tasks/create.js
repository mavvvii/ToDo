import { createTask } from '../../api/tasks.js';
import { createApp } from 'https://unpkg.com/petite-vue?module';

export function mountCreateTask(board_id, onTaskCreated) {
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
      this.closeCreateView();
    },

    openModal(title, message) {
      this.modalTitle = title;
      this.modalMessage = message;
      this.showModal = true;
    },

    closeCreateView() {
      const view = document.getElementById('task-create');
      if (view) {
        view.classList.add('fade-out');
        view.addEventListener('animationend', () => {
          view.innerHTML = '';
        }, { once: true });
      }
    },

    async taskCreate() {
      try {
        this.errorMessage = '';

        if (!this.title.trim()) {
          this.errorMessage = 'Title is required';
          return;
        }

        const response = await createTask(board_id, this.title, this.description);

        this.openModal('Success', `Task "${this.title}" has been created!`);

        if (typeof onTaskCreated === 'function') {
          onTaskCreated(response);
        }

        this.title = '';
        this.description = '';

      } catch (err) {
        this.openModal('Error', err.message || 'Unknown error');
      }
    },

  }).mount('#task-create');
}
