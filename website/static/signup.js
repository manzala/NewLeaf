$('input[type="submit"]').click(function(){
  $('.login').addClass('test')
  setTimeout(function(){
    $('.login').addClass('testtwo')
  },300);
 
  setTimeout(function(){
    $('.login').removeClass('test') 
  },500);
  
});




