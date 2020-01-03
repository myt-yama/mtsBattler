$(document).ready(function() {
    $('#summon_button').modaal({
        before_open: function() {
            $.ajax({
                type: 'POST',
                url: 'summon',
                data: {
                    name: $('#name').val(),
                    team: $('#team').val()
                },
            })
            .done(function(response) {
                $('#status').html(response);
            })
            // .fail(function(response) {
            //   alert("false");
            // })
        },
        content_source: '#modal',
        // is_locked: true,
        // hide_close: true
    });

    $('#status').on('click', '.register', function(){
        let register_flg = $(this).val();
        let id = $('#id').val();
        $.ajax({
            type: 'POST',
            url: 'register',
            data: {
                id: id,
                register_flg: register_flg
            },
        })
        $('#summon_button').modaal('close');
    });
})
