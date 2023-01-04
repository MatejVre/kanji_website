$(function () {
    'use strict'

  $("[data-trigger]").on("click", function(){
      var trigger_id =  $(this).attr('data-trigger');
      $(trigger_id).toggleClass("show");
      $('body').toggleClass("offcanvas-active");
  });

  // close if press ESC button 
  $(document).on('keydown', function(event) {
      if(event.keyCode === 27) {
         $(".navbar-collapse").removeClass("show");
         $("body").removeClass("overlay-active");
      }
  });

  // close button 
  $(".btn-close").click(function(e){
      $(".navbar-collapse").removeClass("show");
      $("body").removeClass("offcanvas-active");
  }); 


})

    function mouseOver(id, meanings){
    meaning = meanings.split(",");

    document.getElementById(id).innerText = meaning[0].split(";")[0];
}
    function mouseOut(id, symbol){
        document.getElementById(id).innerText = symbol;
    }
//onmouseover="mouseOver('{{char.id}}','{{char.meaning}}')" onmouseleave="mouseOut('{{char.id}}','{{char.symbol}}')"