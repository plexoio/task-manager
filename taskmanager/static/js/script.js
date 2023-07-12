document.addEventListener('DOMContentLoaded', function() {
    // Initialize navbar
    let sidenav = document.querySelectorAll('.sidenav');
    M.Sidenav.init(sidenav);
    // Delete Modal (verification)
    let modal_delete = document.querySelectorAll('.modal');
    M.Modal.init(modal_delete, inDuration=250);
  });