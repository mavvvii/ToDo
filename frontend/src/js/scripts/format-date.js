function formatDate(dateStr) {
  if (!dateStr) return 'None';
  const date = new Date(dateStr);
  return date.toLocaleString();
}
