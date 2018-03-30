$(document).ready(function () {
    var flag = 0;
    function sleep(ms) {
        return new Promise(resolve => setTimeout(resolve, ms));
    }
    $(".dm-icon").click(function () {
        if (flag === 0) {
            $(".dropmenu-active").slideDown();
            flag = 1;
        }
        else {
            $(".dropmenu-active").slideUp();
            flag = 0;
        }
    });
});