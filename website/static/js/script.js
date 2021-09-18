const mobileScreen = window.matchMedia("(max-width: 990px )");
$(document).ready(function () {
    
    $(".menu-toggle").click(function () {
        if (mobileScreen.matches) {
            $(".sidebar-nav").toggleClass("mobile-show");
        } else {
            $(".sidebar").toggleClass("sidebar-compact");
        }
    });
});

