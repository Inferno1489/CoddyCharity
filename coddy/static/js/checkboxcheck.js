$( document ).ready(function() {
    button = document.getElementsByClassName("button")[0];
if(button){
    button.addEventListener("click", function () {
        if (($('div.chbs.required :checkbox:checked').length > 0) && ($('div.chb.mar.required :checkbox:checked').length === 1)){
            $("#sms").removeAttr("required");
            $("#comp").removeAttr("required");
            alertify.alert("Спасибо! Благодаря вам мир стал немного добрее!");
        }
        else {
            $("#sms").attr("required","required");
            $("#comp").attr("required","required");
            alertify.alert("Пожалуйста выберити способ пожертвования, и примите соглашение на обработку персональных данных");
        }
    }, true)
}
});