$(document).ready(function(){
  var $cp = $('.fa-copyright');
  $('.hovercolor').hover(function(){
      var gh_color = $(this).css("color");
      $cp.css("color", gh_color);
      });
    });
