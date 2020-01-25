$(document).ready(function() {
    $('#battle_button').click(function(){
        $.ajax({
            type: 'POST',
            url: 'battle',
            data: {
                battle_id: $('#battle_id').val(),
                battle_command_P1: $('#P1-command').val(),
                battle_command_P2: $('#P2-command').val(),
            },
        })
        .done(function(response) {
            // TODO:結果反映
            $('html').html(response);
        })
    });
})
