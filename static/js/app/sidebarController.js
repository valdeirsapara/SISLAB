// $(document).ready(function() {
//   // Quando um link de submenu é clicado
//   $('.sidebar-link[data-bs-toggle="collapse"], .sidebar-link[data-toggle="collapse"]').on('click', function() {
//     // Obtenha o ID do alvo
//     const targetId = $(this).attr('href');
    
//     // Feche todos os outros submenus
//     $('.sidebar-submenu.show').not(targetId).collapse('hide');
    
//     // Atualize os atributos aria-expanded
//     $('.sidebar-link[aria-expanded="true"]').not(this).attr('aria-expanded', 'false');
//   });
// });



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


// mobile-header.js
document.addEventListener('DOMContentLoaded', function() {
  // Mobile user dropdown functionality
  const mobileUserMenuToggle = document.getElementById('mobileUserMenuToggle');
  const mobileUserDropdown = document.getElementById('mobileUserDropdown');
  
  if (mobileUserMenuToggle && mobileUserDropdown) {
    mobileUserMenuToggle.addEventListener('click', function(event) {
      mobileUserDropdown.classList.toggle('show');
      event.stopPropagation();
    });
    
    // Close dropdown when clicking outside
    document.addEventListener('click', function(event) {
      if (!mobileUserDropdown.contains(event.target) && 
          event.target !== mobileUserMenuToggle) {
        mobileUserDropdown.classList.remove('show');
      }
    });
  }
  
  // Mobile sidebar toggle
  const mobileSidebarToggle = document.getElementById('mobileSidebarToggle');
  const sidebar = document.querySelector('.sidebar');
  
  if (mobileSidebarToggle && sidebar) {
    // Create sidebar overlay element
    const sidebarOverlay = document.createElement('div');
    sidebarOverlay.className = 'sidebar-overlay';
    document.body.appendChild(sidebarOverlay);
    
    mobileSidebarToggle.addEventListener('click', function() {
      sidebar.classList.toggle('show');
      sidebarOverlay.classList.toggle('active');
      document.body.classList.toggle('sidebar-open');
    });
    
    // Close sidebar when clicking on overlay
    sidebarOverlay.addEventListener('click', function() {
      sidebar.classList.remove('show');
      sidebarOverlay.classList.remove('active');
      document.body.classList.remove('sidebar-open');
    });
    
    // Handle submenu toggles in mobile view
    const submenuToggles = document.querySelectorAll('.sidebar-link[data-bs-toggle="collapse"]');
    submenuToggles.forEach(toggle => {
      toggle.addEventListener('click', function(e) {
        // Don't close sidebar when opening submenus on mobile
        e.stopPropagation();
      });
    });
  }
  
  // Adjust viewport height for mobile browsers
  function setMobileHeight() {
    const vh = window.innerHeight * 0.01;
    document.documentElement.style.setProperty('--vh', `${vh}px`);
  }
  
  setMobileHeight();
  window.addEventListener('resize', setMobileHeight);
});