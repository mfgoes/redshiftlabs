/**
 * Small site-wide touches: navbar scroll state, scroll reveals, the hero's
 * colony readout, the screenshot lightbox and a note for curious visitors.
 */
(function() {
    'use strict';

    const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

    // Navbar turns solid once the page leaves the hero.
    function trackScroll() {
        document.body.classList.toggle('rl-scrolled', window.scrollY > 40);
    }

    // Sections and cards fade up as they enter. Hidden state is added here,
    // so content stays visible without JS or with reduced motion.
    function setupReveal() {
        if (reduceMotion || !('IntersectionObserver' in window)) return;

        // Grids reveal item by item; everything else reveals as one block.
        const grids = '.rl-cards, .rl-usps, .rl-team, .rl-shots, .rl-pillars, .rl-checklist';
        const targets = [];
        document.querySelectorAll('.rl-section .container > *').forEach(el => {
            if (el.matches(grids)) targets.push(...el.children);
            else targets.push(el);
        });
        const observer = new IntersectionObserver(entries => {
            entries.forEach(entry => {
                if (!entry.isIntersecting) return;
                entry.target.classList.add('is-in');
                observer.unobserve(entry.target);
            });
        }, { rootMargin: '0px 0px -8% 0px' });

        targets.forEach(el => {
            if (el.getBoundingClientRect().top < window.innerHeight) return;
            const siblings = Array.from(el.parentElement.children);
            el.style.setProperty('--rl-delay', `${Math.min(siblings.indexOf(el), 5) * 60}ms`);
            el.classList.add('rl-reveal');
            observer.observe(el);
        });
    }

    // Hero readout: a dust storm is always on its way.
    function setupStormClock() {
        const readout = document.querySelector('.rl-readout');
        const clock = readout && readout.querySelector('[data-storm]');
        if (!clock) return;

        const cycle = 134;
        let remaining = cycle;
        const format = s => `${String(Math.floor(s / 60)).padStart(2, '0')}:${String(s % 60).padStart(2, '0')}`;

        setInterval(() => {
            remaining -= 1;
            if (remaining > 0) {
                readout.classList.remove('is-storm');
                clock.textContent = format(remaining);
                return;
            }
            readout.classList.add('is-storm');
            clock.textContent = 'Inbound';
            if (remaining <= -6) remaining = cycle;
        }, 1000);
    }

    // Screenshot lightbox on a native <dialog>.
    function setupLightbox() {
        const shots = document.querySelectorAll('.rl-shot button');
        if (!shots.length || typeof HTMLDialogElement !== 'function') return;

        const dialog = document.createElement('dialog');
        dialog.className = 'rl-lightbox';
        dialog.innerHTML = '<img alt=""><p></p>';
        document.body.appendChild(dialog);

        shots.forEach(button => {
            button.addEventListener('click', () => {
                const img = button.querySelector('img');
                const caption = button.closest('.rl-shot').querySelector('figcaption');
                dialog.querySelector('img').src = img.src;
                dialog.querySelector('img').alt = img.alt;
                dialog.querySelector('p').textContent = caption ? caption.textContent : '';
                dialog.showModal();
            });
        });
        dialog.addEventListener('click', () => dialog.close());
    }

    // Gameplay pillars: always open on wider screens, a closed accordion on
    // phones. Markup ships with `open` so nothing is hidden without JS.
    function setupPillars() {
        const pillars = document.querySelectorAll('details.rl-pillar');
        if (!pillars.length) return;

        const phone = window.matchMedia('(max-width: 767px)');
        const sync = () => pillars.forEach(p => { p.open = !phone.matches; });
        sync();
        phone.addEventListener('change', sync);

        // Jumping to a pillar (e.g. "The Moon" in the sub-nav) opens it.
        const openTarget = () => {
            const target = location.hash && document.querySelector(location.hash);
            if (target && target.matches('details.rl-pillar')) target.open = true;
        };
        openTarget();
        window.addEventListener('hashchange', openTarget);
    }

    function greet() {
        console.log(
            '%c Redshift Labs %c Small games about big, hostile places.\nWant to playtest Kosmograd? https://discord.gg/RbzwwYn945',
            'background:#c6312f;color:#fff;font-weight:700;padding:2px 6px;',
            'color:inherit;'
        );
    }

    document.addEventListener('DOMContentLoaded', () => {
        trackScroll();
        window.addEventListener('scroll', trackScroll, { passive: true });
        setupReveal();
        setupStormClock();
        setupLightbox();
        setupPillars();
        greet();
    });
})();
