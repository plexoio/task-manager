document.addEventListener('DOMContentLoaded', function () {

  // Initialize navbar
  let sidenav = document.querySelectorAll('.sidenav');
  M.Sidenav.init(sidenav);

  // Delete Modal (verification)
  let modal_delete = document.querySelectorAll('.modal');
  M.Modal.init(modal_delete, inDuration = 250);

  // Date Picker
  let datepicker = document.querySelectorAll('.datepicker');
  M.Datepicker.init(datepicker, {
    format: 'mmm dd, yyyy',
    autoClose: false,
    i18n: {
      done: 'Select'
    }
  });

  // Select
  let selects = document.querySelectorAll('select');
  M.FormSelect.init(selects);

  // Collapsable
  let collapse = document.querySelectorAll('.collapsible');
  M.Collapsible.init(collapse);

});