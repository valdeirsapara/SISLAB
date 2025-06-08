// Adicione este script para controlar um menu por vez
document.addEventListener('DOMContentLoaded', function() {
  // Function to close all submenus except the one being clicked
  function handleSubmenuToggle() {
    const allSubmenus = document.querySelectorAll('.sidebar-submenu.show');
    const currentTarget = this.getAttribute('href');
    
    // Close all other open submenus
    allSubmenus.forEach(submenu => {
      // Skip if this is the submenu we just clicked
      if ('#' + submenu.id !== currentTarget) {
        // Find the controlling link
        const controlLink = document.querySelector(`a[href="#${submenu.id}"]`);
        if (controlLink) {
          controlLink.setAttribute('aria-expanded', 'false');
        }
        
        // Use Bootstrap's collapse functionality
        if (typeof bootstrap !== 'undefined') {
          const bsCollapse = bootstrap.Collapse.getInstance(submenu);
          if (bsCollapse) {
            bsCollapse.hide();
          }
        } else {
          // Fallback for jQuery version
          $(submenu).collapse('hide');
        }
      }
    });
  }
  
  // Add click event to all submenu toggle links
  const submenuToggles = document.querySelectorAll('.sidebar-link[data-bs-toggle="collapse"], .sidebar-link[data-toggle="collapse"]');
  submenuToggles.forEach(toggle => {
    toggle.addEventListener('click', handleSubmenuToggle);
  });
  
  // Handle mobile view - Toggle sidebar
  const sidebarToggle = document.getElementById('sidebarToggle');
  const sidebar = document.querySelector('.sidebar');
  const content = document.querySelector('.content');
  
  if (sidebarToggle) {
    sidebarToggle.addEventListener('click', function() {
      sidebar.classList.add('show');
      content.classList.add('sidebar-open');
    });
  }
});




