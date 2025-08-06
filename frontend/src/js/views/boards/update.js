import { createApp } from 'https://unpkg.com/petite-vue?module';
import { getBoards, updateBoard } from '../../api/boards.js';

export function mountUpdateBoard() {
  const app = {
    boards: [],
    selectedBoardID: '',
    title: '',
    description: '',
    errorMessage: '',
    showModal: false,
    modalTitle: '',
    modalMessage: '',

    async fetchBoards() {
      try {
        const data = await getBoards();
        this.boards = data;
        this.onBoardChange();
      } catch (err) {
        this.errorMessage = 'Error during fetch boards: ' + err.message;
      }
    },

    onBoardChange() {
      if (!this.selectedBoardID) {
        this.title = '';
        this.description = '';
        return;
      }
      const board = this.boards.find(b => b.id === this.selectedBoardID);
      if (board) {
        this.title = board.title || '';
        this.description = board.description || '';
      } else {
        this.title = '';
        this.description = '';
      }
    },

    closeUpdateView() {
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

    async update() {
      try {
        this.errorMessage = '';
        if (!this.selectedBoardID) {
          this.openModal('Error', 'You have to select board!');
          return;
        }
        await updateBoard(this.selectedBoardID, this.title, this.description);
        this.openModal('Success', 'Board has been updated!');
      } catch (err) {
        this.openModal('Error', 'Unknown error');
      }
    },
  };

  createApp(app).mount('#board-update');
  app.fetchBoards();
}
