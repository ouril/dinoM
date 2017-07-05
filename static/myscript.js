$(document).ready(function () {
    $('.topic').hide();
    $('.reg').click(function () {
        $('.topic').show('slow');
    });
    $('.cross').click(function () {
        $('.topic').hide('slow');
    });
});
