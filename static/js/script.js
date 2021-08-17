// Initialize mob menu nav functionality  - Materialize
$(document).ready(function(){
    $('.sidenav').sidenav({edge: "right"});
  });

// Collapsible accordion
$(document).ready(function(){
  $('.collapsible').collapsible();
});

//tooltip
$(document).ready(function(){
  $('.tooltipped').tooltip();
});

//datepicker
$(document).ready(function(){
  $('.datepicker').datepicker({
    format: "dd mmmm, yyyy",
    yearRange: 3,
    showClearBtn: true,
    i18n: {
      done: "Select"
    }
  });
});