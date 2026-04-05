/**
 * Tab Bar Controller
 * Manages active state and panel visibility for tab navigation
 */

class TabBar {
  constructor(containerId) {
    this.container = document.getElementById(containerId);
    this.buttons = this.container.querySelectorAll('.tab-button');
    this.activeTab = null;

    // Auto-discover panels by data-panel attribute
    this.panels = {};
    this.buttons.forEach((btn) => {
      const panelId = btn.dataset.panel;
      if (panelId) {
        this.panels[panelId] = document.getElementById(panelId);
      }
    });

    this.init();
  }

  init() {
    this.buttons.forEach((btn) => {
      btn.addEventListener('click', () => {
        const tabName = btn.dataset.panel;
        this.toggle(tabName);
      });
    });
  }

  toggle(tabName) {
    if (this.activeTab === tabName) {
      // Deselect — close all panels
      this.deselect();
    } else {
      // Select — open this tab's panel
      this.select(tabName);
    }
  }

  select(tabName) {
    this.activeTab = tabName;

    // Update button states
    this.buttons.forEach((btn) => {
      if (btn.dataset.panel === tabName) {
        btn.classList.add('active');
      } else {
        btn.classList.remove('active');
      }
    });

    // Update panel visibility
    Object.entries(this.panels).forEach(([name, panel]) => {
      if (name === tabName) {
        panel.classList.add('visible');
      } else {
        panel.classList.remove('visible');
      }
    });
  }

  deselect() {
    this.activeTab = null;

    this.buttons.forEach((btn) => {
      btn.classList.remove('active');
    });

    Object.values(this.panels).forEach((panel) => {
      panel.classList.remove('visible');
    });
  }
}

// Auto-initialize all tab bars on page load
document.addEventListener('DOMContentLoaded', () => {
  document.querySelectorAll('[data-tabbar]').forEach((container) => {
    new TabBar(container.id);
  });
});
