document.addEventListener('DOMContentLoaded', () => {
    const path = window.location.pathname;
    const buttons = document.querySelectorAll('.btn-admin-panel');
    const adminContainer = document.getElementById('admin-container');

    buttons.forEach(button => {
        const tabPaneId = button.getAttribute('data-bs-target');
        const tabPane = document.querySelector(tabPaneId);

        if (path === button.getAttribute('data-url')) {
            button.setAttribute('aria-selected', 'true');
            button.classList.add('active');
            if (tabPane) {
                tabPane.classList.add('active', 'show');
            }
        } else {
            button.setAttribute('aria-selected', 'false');
            button.classList.remove('active');
            if (tabPane) {
                tabPane.classList.remove('active', 'show');
            }
        }
    });

    // Remover a classe 'hidden' para mostrar o conteúdo
    adminContainer.classList.remove('hidden');
});
function handleClick(url) {
    window.location.href = url;
}