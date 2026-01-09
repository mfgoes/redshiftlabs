/**
 * ComponentLoader - Modular component loading system
 * Loads HTML components and injects them into specified containers
 */
(function() {
    'use strict';

    const ComponentLoader = {
        /**
         * Loads a component from the components directory
         * @param {string} componentName - Name of the component (e.g., 'navbar')
         * @param {string} containerSelector - CSS selector for the container element
         * @returns {Promise<HTMLElement>} - Promise that resolves with the container element
         */
        async load(componentName, containerSelector) {
            try {
                const container = document.querySelector(containerSelector);

                if (!container) {
                    throw new Error(`Container not found: ${containerSelector}`);
                }

                // Fetch the component HTML
                const response = await fetch(`components/${componentName}.html`);

                if (!response.ok) {
                    throw new Error(`Failed to load component: ${componentName} (${response.status})`);
                }

                const html = await response.text();

                // Inject the HTML into the container
                container.innerHTML = html;

                console.log(`Component loaded: ${componentName}`);

                return container;
            } catch (error) {
                console.error('ComponentLoader error:', error);
                throw error;
            }
        },

        /**
         * Loads multiple components in parallel
         * @param {Array<{name: string, container: string}>} components - Array of component configs
         * @returns {Promise<Array<HTMLElement>>} - Promise that resolves with array of container elements
         */
        async loadMultiple(components) {
            try {
                const promises = components.map(({ name, container }) =>
                    this.load(name, container)
                );

                return await Promise.all(promises);
            } catch (error) {
                console.error('ComponentLoader.loadMultiple error:', error);
                throw error;
            }
        }
    };

    // Expose ComponentLoader globally
    window.ComponentLoader = ComponentLoader;

    console.log('ComponentLoader initialized');
})();
