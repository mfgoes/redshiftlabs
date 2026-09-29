/**
 * Components initialization script
 * Handles navbar and footer loading, active states and the dark theme
 */
document.addEventListener('DOMContentLoaded', async function() {
    try {
        // Load navbar and footer components in parallel
        await window.ComponentLoader.loadMultiple([
            { name: 'navbar', container: '#navbar-container' },
            { name: 'footer', container: '#footer-container' },
            { name: 'bottom-navbar', container: '#bottom-navbar-container' }
        ]);

        // Set active nav link based on current page
        setActiveNavLink();

        // Apply the (dark-only) theme
        initializeDarkMode();
    } catch (error) {
        console.error('Error initializing components:', error);
    }
});

/**
 * Sets the active class on the current page's nav link
 */
function setActiveNavLink() {
    const currentPage = window.location.pathname.split('/').pop() || 'index.html';
    const navLinks = document.querySelectorAll('.navbar-nav .nav-link, .rl-bottom-nav-link');

    navLinks.forEach(link => {
        const linkPage = link.getAttribute('href');
        if (linkPage === currentPage || (currentPage === '' && linkPage === 'index.html')) {
            link.classList.add('active');
        }
    });
}

/**
 * The site is dark-only: always apply the dark theme styles.
 */
function initializeDarkMode() {
    document.body.classList.add('dark-mode');
}
