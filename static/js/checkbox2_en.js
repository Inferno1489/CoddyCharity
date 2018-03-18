$( document ).ready(function() {
    button = document.getElementsByClassName("button")[0];
if(button){
    button.addEventListener("click", function () {
        if ($('div.chb.mar :checkbox:checked').length === 1){
            alertify.alert("Thank you! We will contact you soon!");
        }
        else {
            alertify.alert("Please, sign consent to the processing of personal data");
        }
    }, true)
}
});