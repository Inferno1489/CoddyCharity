$( document ).ready(function() {
    button = document.getElementsByClassName("button")[0];
if(button){
    button.addEventListener("click", function () {
        if (($('div.chbs.required :checkbox:checked').length > 0) && ($('div.chb.mar.required :checkbox:checked').length === 1)){
            $("#sms").removeAttr("required");
            $("#comp").removeAttr("required");
            alertify.alert("Thank you! Our world became a bit better becouse of you!");
        }
        else {
            $("#sms").attr("required","required");
            $("#comp").attr("required","required");
            alertify.alert("Please choose at least one donation method, and sign consent to the processing of personal data");
        }
    }, true)
}
});