document.addEventListener('DOMContentLoaded', function() {
  const mobileUserMenuToggle = document.getElementById('mobileUserMenuToggle');
  const mobileUserDropdown = document.getElementById('mobileUserDropdown');

  if (mobileUserMenuToggle && mobileUserDropdown) {
    mobileUserMenuToggle.addEventListener('click', function(event) {
      mobileUserDropdown.classList.toggle('show');
      event.stopPropagation();
    });

    document.addEventListener('click', function(event) {
      if (!mobileUserDropdown.contains(event.target) &&
          event.target !== mobileUserMenuToggle) {
        mobileUserDropdown.classList.remove('show');
      }
    });
  }

  const mobileSidebarToggle = document.getElementById('mobileSidebarToggle');
  const sidebar = document.querySelector('.sidebar');

  if (mobileSidebarToggle && sidebar) {
    const sidebarOverlay = document.createElement('div');
    sidebarOverlay.className = 'sidebar-overlay';
    document.body.appendChild(sidebarOverlay);

    mobileSidebarToggle.addEventListener('click', function() {
      sidebar.classList.toggle('show');
      sidebarOverlay.classList.toggle('active');
      document.body.classList.toggle('sidebar-open');
    });

    sidebarOverlay.addEventListener('click', function() {
      sidebar.classList.remove('show');
      sidebarOverlay.classList.remove('active');
      document.body.classList.remove('sidebar-open');
    });

    const submenuToggles = document.querySelectorAll('.sidebar-link[data-bs-toggle="collapse"]');
    submenuToggles.forEach(toggle => {
      toggle.addEventListener('click', function(e) {
        e.stopPropagation();
      });
    });
  }

  function setMobileHeight() {
    const vh = window.innerHeight * 0.01;
    document.documentElement.style.setProperty('--vh', `${vh}px`);
  }

  setMobileHeight();
  window.addEventListener('resize', setMobileHeight);
});
