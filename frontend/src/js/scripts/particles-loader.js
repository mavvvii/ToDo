fetch('components/particles.html')
  .then(res => res.text())
  .then(html => {
    document.getElementById('particles-placeholder').innerHTML = html;
  })
  .catch(err => console.error('Failed to load particles:', err));
