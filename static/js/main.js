const body = document.body;
const collapseButton = document.querySelector('.collapse-button');
const mobileMenu = document.querySelector('.mobile-menu');

collapseButton?.addEventListener('click', () => {
  body.classList.toggle('sidebar-collapsed');
  collapseButton.setAttribute('aria-expanded', String(!body.classList.contains('sidebar-collapsed')));
  collapseButton.textContent = body.classList.contains('sidebar-collapsed') ? '→' : '←';
});

mobileMenu?.addEventListener('click', () => {
  body.classList.toggle('sidebar-open');
  mobileMenu.setAttribute('aria-expanded', String(body.classList.contains('sidebar-open')));
});

document.querySelectorAll('.side-link').forEach(link => {
  link.addEventListener('click', () => body.classList.remove('sidebar-open'));
});
