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
})
