/**
 * Mission Log Controller
 * Manages expand/collapse and prerequisite hints
 */

class MissionLog {
  constructor(containerId) {
    this.container = document.getElementById(containerId);
    this.init();
  }

  init() {
    // Completed missions: toggle body expand/collapse
    this.container.querySelectorAll('.ml-row--done').forEach((row) => {
      row.addEventListener('click', () => this.toggleDoneRow(row));
    });

    // Locked-next missions: toggle prerequisite message
    this.container.querySelectorAll('.ml-row--locked-next').forEach((row) => {
      row.addEventListener('click', () => this.toggleLockedNext(row));
    });
  }

  toggleDoneRow(row) {
    const body = row.querySelector('.ml-row-body');
    const chev = row.querySelector('.ml-chev');

    if (!body) return;

    const wasOpen = !body.hidden;
    body.hidden = wasOpen;

    if (chev) {
      chev.textContent = wasOpen ? '▸' : '▾';
    }
  }

  toggleLockedNext(row) {
    const msg = row.querySelector('.ml-locked-msg');
    if (msg) {
      msg.hidden = !msg.hidden;
    }
  }
}

// Auto-initialize all mission logs on page load
document.addEventListener('DOMContentLoaded', () => {
  document.querySelectorAll('[data-mission-log]').forEach((container) => {
    new MissionLog(container.id);
  });
});
