// js/views/boards/list.js
import { createApp } from 'https://unpkg.com/petite-vue?module';
import { getBoards } from '../../api/boards.js';

export function mountBoardList() {
  createApp({
    boards: [],
    async fetch() {
      try {
        this.boards = await getBoards();
      } catch (err) {
        alert('Error during fetch boards: ' + err.message);
      }
    },
    goToDetail(id) {
      const board = this.boards.find(b => b.id === id);
      if (board) {
        window.activeBoard = board;

        const editBtn = document.getElementById('editBtn');
        const deleteBtn = document.getElementById('deleteBtn');

        if (editBtn && deleteBtn) {
          editBtn.disabled = false;
          deleteBtn.disabled = false;

          editBtn.onclick = () => window.loadView(`./forms/boards/update.html?id=${id}`);
          deleteBtn.onclick = () => window.loadView(`./forms/boards/delete.html?id=${id}`);
        }

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

        const editBtn = document.getElementById('editBtn');
        const deleteBtn = document.getElementById('deleteBtn');
        if (editBtn && deleteBtn) {
          editBtn.disabled = false;
          deleteBtn.disabled = false;

          editBtn.onclick = () => window.loadView(`./forms/boards/update.html?id=${board.id}`);
          deleteBtn.onclick = () => window.loadView(`./forms/boards/delete.html?id=${board.id}`);
        }
      };
      nav.appendChild(btn);
    });
  } catch (err) {
    nav.innerHTML = '<span class="text-danger">Error during get boards!</span>';
  }
}
