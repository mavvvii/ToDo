import { loadBoardsToNavbar } from '../views/boards/list.js';

const container = document.getElementById('content-area');

async function removeViewByUrl(url) {
    const existingView = container.querySelector(`.loaded-view[data-view="${url}"]`);
    if (existingView) {
    existingView.remove();
    }
}

async function loadView(url) {
    if (url.includes('detail.html')) {
    container.innerHTML = '';
    }

    await removeViewByUrl(url);

    try {
    const response = await fetch(url);
    const html = await response.text();

    const viewWrapper = document.createElement('div');
    viewWrapper.classList.add('loaded-view');
    viewWrapper.dataset.view = url;
    viewWrapper.innerHTML = html;
    container.appendChild(viewWrapper);

    function waitForElement(selector) {
        return new Promise((resolve) => {
        if (document.querySelector(selector)) {
            return resolve();
        }
        const observer = new MutationObserver(() => {
            if (document.querySelector(selector)) {
            resolve();
            observer.disconnect();
            }
        });
        observer.observe(document.body, { childList: true, subtree: true });
        });
    }

    requestAnimationFrame(async () => {
        if (url.includes('create.html')) {
        const { mountCreateBoard } = await import('../views/boards/create.js');
        await waitForElement('#board-create');
        mountCreateBoard();
        } else if (url.includes('list.html')) {
        const { mountBoardList } = await import('../views/boards/list.js');
        await waitForElement('#board-list');
        mountBoardList();
        } else if (url.includes('detail.html')) {
        const { mountBoardDetail } = await import('../views/boards/detail.js');
        await waitForElement('#board-detail');
        mountBoardDetail();
        } else if (url.includes('update.html')) {
        const { mountUpdateBoard } = await import('../views/boards/update.js');
        await waitForElement('#board-update');
        mountUpdateBoard();
        } else if (url.includes('delete.html')) {
        const { mountDeleteBoard } = await import('../views/boards/delete.js');
        await waitForElement('#board-delete');
        mountDeleteBoard();
        }
    });

    } catch (err) {
    const errorDiv = document.createElement('div');
    errorDiv.className = 'alert alert-danger';
    errorDiv.textContent = `Error during loading view: ${err.message}`;
    container.appendChild(errorDiv);
    }
}

window.loadView = loadView;

window.addEventListener('DOMContentLoaded', () => {
    loadBoardsToNavbar();
});
