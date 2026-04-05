// Mission log tab switching
document.addEventListener('DOMContentLoaded', () => {
  const tabBars = document.querySelectorAll('.mission-tabs');
  tabBars.forEach(bar => {
    const list = bar.closest('.game-panel').querySelector('.mission-list');
    if (!list) return;
    bar.addEventListener('click', e => {
      const tab = e.target.closest('.mission-tab');
      if (!tab) return;
      bar.querySelectorAll('.mission-tab').forEach(t => t.classList.remove('is-active'));
      tab.classList.add('is-active');
      const filter = tab.dataset.tab;
      list.querySelectorAll('.quest-item').forEach(item => {
        const state = item.dataset.state;
        const show =
          filter === 'all' ||
          (filter === 'active'    && (state === 'active' || state === 'locked')) ||
          (filter === 'completed' && state === 'completed');
        item.classList.toggle('tab-hidden', !show);
      });
    });
  });
});

// Highlight active nav link on scroll
const sections = document.querySelectorAll('section[id]');
const links = document.querySelectorAll('nav a');
const observer = new IntersectionObserver(entries => {
  entries.forEach(e => {
    if (e.isIntersecting) {
      links.forEach(l => l.classList.remove('active'));
      const a = document.querySelector(`nav a[href="#${e.target.id}"]`);
      if (a) a.classList.add('active');
    }
  });
}, { rootMargin: '-40% 0px -55% 0px' });
sections.forEach(s => observer.observe(s));
