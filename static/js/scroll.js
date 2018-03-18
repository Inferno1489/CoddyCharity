$(".bts").on("click", "a", function(event){
        event.preventDefault();
        $('html, body').stop().animate({
            scrollTop: $("#"+$(this).attr("pre")).position().top - 120
        }, 500, 'swing');
});
/**$(document).ready(function(){
    $(".bts").on("click","a", function (event) {
        event.preventDefault();
        var id  = $(this).attr('href'),
        top = $(id).offset().top;
        $('body').animate({scrollTop: top}, 1500);
        $('html').animate({scrollTop: top}, 1500);
    });
});**/
