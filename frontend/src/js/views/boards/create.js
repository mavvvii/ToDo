import { createApp } from 'https://unpkg.com/petite-vue?module';
import { createBoard } from '../../api/boards.js';
import { loadBoardsToNavbar } from './list.js';

export function mountCreateBoard() {
  createApp({
    title: '',
    description: '',
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
      const view = document.getElementById('board-create');
      if (view) {
      view.classList.add('fade-out');
        view.addEventListener('animationend', () => {
          view.innerHTML = '';

        }, { once: true });
      }
    },

    async createBoardAction() {
      try {
        this.errorMessage = ''

        if (!this.title.trim()) {
          this.errorMessage = 'Title is required';
          return;
        }

        await createBoard(this.title, this.description);

        this.openModal('Success', `Board ${this.title} has been created!`);

        await loadBoardsToNavbar();

        this.title = '';
        this.description = '';

      } catch (err) {
        this.openModal('Error', 'Unknown error')
      }
    },
  }).mount('#board-create');
}
