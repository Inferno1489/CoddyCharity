$( document ).ready(function() {
    button = document.getElementsByClassName("button")[0];
if(button){
    button.addEventListener("click", function () {
        if ($('div.chb.mar :checkbox:checked').length === 1){
            alertify.alert("Спасибо! Мы обязательно свяжемся с вами!");
        }
        else {
            alertify.alert("Пожалуйста, примите соглашение на обработку персональных данных");
        }
    }, true)
}
});