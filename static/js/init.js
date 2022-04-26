(function($){
  $(function(){

    $('.sidenav').sidenav();

    $('.slider').slider({
      fullWidth: true,
      indicators: false,
      height: 600
      
    });

    $('.sliderb').slider({
      fullWidth: true,
      indicators: false,
      height: 284
      
    });

    $('.sliderv').slider({
      fullWidth: true,
      indicators: false,
      height: 284
      
    });

    $("option").each(function(i){
        if($(this).val()==='-'){
          $(this).prop('disabled',true);
        }
    });

    $('select').formSelect();

  }); // end of document ready
})(jQuery); // end of jQuery name space
