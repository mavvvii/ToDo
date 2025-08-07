import { createApp } from 'https://unpkg.com/petite-vue?module';
import { getBoards, deleteBoard } from '../../api/boards.js';

export function mountDeleteBoard() {
  const app = {
    boards: [],
    selectedBoardID: '',
    errorMessage: '',
    showModal: false,
    modalTitle: '',
    modalMessage: '',

    async fetchBoards() {
      try {
        const data = await getBoards();
        this.boards = data;
      } catch (err) {
        this.errorMessage = 'Error during fetch boards: ' + err.message;
      }
    },

    closeDeleteView() {
      const container = document.getElementById('content-area');
      if (container) {
        container.innerHTML = '';
      }
    },

    openModal(title, message) {
      this.modalTitle = title;
      this.modalMessage = message;
      this.showModal = true;
    },

    closeModal() {
      this.showModal = false;
    },

    async deleteBoardAction() {
      try {
        this.errorMessage = '';
        if (!this.selectedBoardID) {
          this.openModal('Error', 'You have to select board!');
          return;
        }
        await deleteBoard(this.selectedBoardID);
        this.openModal('Success', 'Board has been created!');
        this.fetchBoards();
        this.selectedBoardID = '';
      } catch (err) {
        this.openModal('Error', 'Unknown error');
      }
    },
  };

  createApp(app).mount('#board-delete');
  app.fetchBoards();
}
