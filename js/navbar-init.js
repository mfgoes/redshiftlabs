/**
 * Components initialization script
 * Handles navbar and footer loading, active states, dark mode, and mobile dropdown behavior
 */
document.addEventListener('DOMContentLoaded', async function() {
    try {
        // Load navbar and footer components in parallel
        await window.ComponentLoader.loadMultiple([
            { name: 'navbar', container: '#navbar-container' },
            { name: 'footer', container: '#footer-container' }
        ]);

        // Set active nav link based on current page
        setActiveNavLink();

        // Initialize dark mode toggle (in footer)
        initializeDarkMode();

        // Setup mobile dropdown auto-expand
        setupMobileDropdown();

        console.log('Components initialized successfully');
    } catch (error) {
        console.error('Error initializing components:', error);
    }
});

/**
 * Sets the active class on the current page's nav link
 */
function setActiveNavLink() {
    const currentPage = window.location.pathname.split('/').pop() || 'index.html';
    const navLinks = document.querySelectorAll('.navbar-nav .nav-link');

    navLinks.forEach(link => {
        const linkPage = link.getAttribute('href');
        if (linkPage === currentPage || (currentPage === '' && linkPage === 'index.html')) {
            link.classList.add('active');
        }
    });
}

/**
 * Initializes dark mode toggle functionality (in footer)
 */
function initializeDarkMode() {
    const darkModeToggle = document.getElementById('darkModeToggle');

    if (!darkModeToggle) {
        console.warn('Dark mode toggle button not found');
        return;
    }

    // SVG icons
    const moonIcon = '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"></path></svg>';
    const sunIcon = '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="5"></circle><line x1="12" y1="1" x2="12" y2="3"></line><line x1="12" y1="21" x2="12" y2="23"></line><line x1="4.22" y1="4.22" x2="5.64" y2="5.64"></line><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"></line><line x1="1" y1="12" x2="3" y2="12"></line><line x1="21" y1="12" x2="23" y2="12"></line><line x1="4.22" y1="19.78" x2="5.64" y2="18.36"></line><line x1="18.36" y1="5.64" x2="19.78" y2="4.22"></line></svg>';

    // Check for saved theme preference or default to light mode
    const currentTheme = localStorage.getItem('theme') || 'light';

    // Function to update Bluesky embed theme (if present)
    function updateBskyTheme(isDark) {
        const bskyEmbed = document.getElementById('bskyEmbed');
        if (bskyEmbed) {
            bskyEmbed.setAttribute('mode', isDark ? 'dark' : 'light');
        }
    }

    // Apply saved theme on page load
    if (currentTheme === 'dark') {
        document.body.classList.add('dark-mode');
        darkModeToggle.innerHTML = sunIcon;
        updateBskyTheme(true);
    }

    // Toggle dark mode
    darkModeToggle.addEventListener('click', function() {
        // Add rotation animation
        darkModeToggle.style.transform = 'rotate(360deg)';
        setTimeout(() => {
            darkModeToggle.style.transform = '';
        }, 300);

        document.body.classList.toggle('dark-mode');

        // Update icon and save preference
        if (document.body.classList.contains('dark-mode')) {
            darkModeToggle.innerHTML = sunIcon;
            localStorage.setItem('theme', 'dark');
            updateBskyTheme(true);
        } else {
            darkModeToggle.innerHTML = moonIcon;
            localStorage.setItem('theme', 'light');
            updateBskyTheme(false);
        }
    });
}

/**
 * Sets up mobile dropdown auto-expand behavior
 */
function setupMobileDropdown() {
    const navbarCollapse = document.querySelector('#navbarNav');
    const communityDropdown = document.querySelector('#communityDropdown');

    if (!navbarCollapse || !communityDropdown) {
        console.warn('Navbar collapse or community dropdown not found');
        return;
    }

    console.log('Mobile dropdown setup initialized', {
        navbarCollapse: !!navbarCollapse,
        communityDropdown: !!communityDropdown,
        bootstrapAvailable: typeof bootstrap !== 'undefined'
    });

    // When mobile menu opens, auto-expand Community dropdown
    navbarCollapse.addEventListener('shown.bs.collapse', function() {
        const isMobile = window.matchMedia('(max-width: 991.98px)').matches;

        console.log('Menu opened. Is mobile:', isMobile);

        if (isMobile) {
            const dropdownMenu = communityDropdown.nextElementSibling;

            if (dropdownMenu && dropdownMenu.classList.contains('dropdown-menu')) {
                // Add 'show' class to both toggle and menu
                communityDropdown.classList.add('show');
                communityDropdown.setAttribute('aria-expanded', 'true');
                dropdownMenu.classList.add('show');
                console.log('Dropdown auto-expanded on mobile');
            }
        }
    });

    // When mobile menu closes, reset dropdown state
    navbarCollapse.addEventListener('hide.bs.collapse', function() {
        const isMobile = window.matchMedia('(max-width: 991.98px)').matches;

        if (isMobile) {
            const dropdownMenu = communityDropdown.nextElementSibling;

            if (dropdownMenu && dropdownMenu.classList.contains('dropdown-menu')) {
                // Remove 'show' class from both toggle and menu
                communityDropdown.classList.remove('show');
                communityDropdown.setAttribute('aria-expanded', 'false');
                dropdownMenu.classList.remove('show');
            }
        }
    });
}
