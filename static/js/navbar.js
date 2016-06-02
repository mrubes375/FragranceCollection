$(document).ready(function() {
  if (window.location.pathname=='/') {
    $('a:first').addClass('active');
  }
  else if (window.location.pathname=='/about/') {
    $('li:first').addClass('active');
  }
  else if (window.location.pathname=='/collection/') {
    $('li')[1].addClass('active');
  }
  else {
    $('li:last').addClass('active');
  }
});
