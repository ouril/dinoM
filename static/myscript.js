$(document).ready(function () {
    $('.topic').hide();
    $('.reg').click(function () {
        $('.topic').show('slow');
    });
    $('.cross').click(function () {
        $('.topic').hide('slow');
    });
});

function update_page(new_html) {
    // console.log('new_html -->', new_html);
    $('#users_list').html(new_html)
};

function getFormData(form) {
    var unindexed_array = form.serializeArray();
    var indexed_array = {};

    $.map(unindexed_array, function (n, i) {
        indexed_array[n['name']] = n['value'];
    });

    return indexed_array;
};

function send_data() {
    var id = $('#userid').html();
    var user_data = getFormData($('#user_form'));
    
    var prefix =  (id != undefined) ? id : '';
   
    $.ajax({
        url: 'create/user/' + prefix,
        type: 'POST',
        data: user_data,
        dataType: 'json',
        success: function (response) {   
                if (response.errors) {
                } else {
                 $('#user_id').html(response.html);
                 $('input').val('')  
                };                   
         
        }
        
    });
};

function fill_form(id){
   
    $.ajax({
        url: 'get_user_form/' + id,
        type: 'GET',
        dataType: 'json',
        success: function (response) {
            if (response.errors) {
            } else {
                $('#user_form').html(response.html);
            }
        },
        error: function (xhr, status, error) {
        }
    });
};

