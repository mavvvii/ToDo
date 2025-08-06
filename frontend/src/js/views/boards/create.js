import { createApp } from 'https://unpkg.com/petite-vue?module';
import { createBoard } from '../../api/boards.js';

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
        this.errorMessage = ''
        const response = await createBoard(this.title, this.description);
        this.openModal('Success', `Board ${this.title} has been created!`);
      } catch (err) {
        this.openModal('Error', 'Unknown error')
      }
    },
  }).mount('#board-create');
}
