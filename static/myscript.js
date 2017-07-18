// Скрипт для скрытия панели с регистрацией
$(document).ready(function () {
    $('.topic').hide();
    $('#reg').click(function () {
        $('.topic').show('slow');
    });
    $('.cross').click(function () {
        $('.topic').hide('slow');
    });
});

/*
$(document).ready(function () {
    $('.dark_fon').hover( $('.dark_fon').css(opasity=0.9), $('.dark_fon').css(opasity=0.1));
};
*/
// Скрипт покзывает оштбки
function show_errors(errors) {
    for (var error_name in errors) {
        for (var error in errors[error_name]){
            $('[name=' + error_name + ']', $('#user_form')).closest('td').prepend('<li class="error">'+ errors[error_name][error].message + '</li>');
        }
        $('[name=' + error_name + ']', $('#user_form')).parent().addClass('error');
    }
}

function getFormData(form) {
    //функция по обработке данных в форме 
    var unindexed_array = form.serializeArray();
    // .serializeArray() - jQuery функция которая вытаскивает значения формы
    var indexed_array = {};
    $.map(unindexed_array, function (n, i) {
        indexed_array[n['name']] = n['value'];
    });
    // создаем и возвращаем объект для отправки
    return indexed_array;
};

function send_data() {
    var id = $('#userid').html();
    // получаем элемент id
    var user_data = getFormData($('#user_form'));
    // подучаем содержимое формы 
    var prefix =  (id != undefined) ? id : '';
    //  получаем префикс
    $.ajax({
        url: 'create/user/' + prefix,
        type: 'POST',
        data: user_data,
        dataType: 'json',
        success: function (response) {   
                if (response.errors) {
                    $('#user_form').find('li.error').remove();
                    show_errors(response.errors);
                    console.log("errors = ", errors);
                } else {
                 $("#user_id").html(response.html);
                 $("input").val('')  
                };                   
         
        }
        
    });
};
// Скрипт для того чтобы загрузить информацию о юзере в форму
function fill_form(id){
   
    $.ajax({
        url: 'get_user_form/' + id,
        type: 'GET',
        dataType: 'json',
        success: function (response) {
            if (response.errors) {
                console.log("errors = ", errors);
            } else {
                $('#user_form').html(response.html);
            }
        },
        error: function (xhr, status, error) {
        }
    });
};

