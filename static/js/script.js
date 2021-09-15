$(document).ready(function () {
  // sidenav for mob init
  $(".sidenav").sidenav({
    edge: "right"
  });

  //Collapsible component
  $(".collapsible").collapsible();

  // datepicker
  $(".datepicker").datepicker({
    format: "dd mmmm, yyyy",
    yearRange: 3,
    showClearBtn: true,
    i18n: {
      done: "Select"
    }
  });

  // Tooltip
  $(".tooltipped").tooltip();

  // Select dropdown
  $("select").formSelect();

  // Carousel
  $('.carousel.carousel-slider').carousel({
    fullWidth: true,
    indicators: true
  });
});