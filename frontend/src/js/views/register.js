// js/views/register.js
import { createApp } from 'https://unpkg.com/petite-vue?module';
import { registerUser } from '../api/register.js';

export function mountRegisterView() {
  createApp({
    username: '',
    email: '',
    password: '',
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

    closeRegisterView() {
      const container = document.getElementById('content-area');
      if (container) {
        container.innerHTML = '';
      }
    },

    async register() {
      try {
        this.errorMessage = '';
        const data = await registerUser(this.username, this.email, this.password);
        this.openModal(data.detail || 'Sukces', data.message || '');
      } catch (err) {
        this.openModal('Błąd', err.message || 'Nieznany błąd');
      }
    }
  }).mount('#register-app');
}
