import { createApp } from 'https://unpkg.com/petite-vue?module';
import { getBoards } from '../../api/boards.js';

export function mountBoardList() {
  createApp({
    boards: [],

    goToDetail(id) {
      const board = this.boards.find(b => b.id === id);
      if (board) {
        window.activeBoard = board;
        window.loadView(`./forms/boards/detail.html?id=${id}`);
      }
    }
  }).mount('#board-list');
}

export async function loadBoardsToNavbar() {
  const nav = document.getElementById('board-nav');
  nav.innerHTML = '';

  try {
    const boards = await getBoards();

    boards.forEach(board => {
      const btn = document.createElement('button');

      btn.textContent = board.title;
      btn.className = 'btn btn-outline-secondary btn-sm mx-1';

      btn.onclick = () => {
        window.activeBoard = board;
        window.loadView(`./forms/boards/detail.html?id=${board.id}`);
      };

      nav.appendChild(btn);
    });

  } catch (err) {
    nav.innerHTML = '<span class="text-danger">Error during get boards!</span>';
  }
}
