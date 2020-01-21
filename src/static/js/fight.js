$(document).ready(function() {
    $('#battle_button').click(function(){
        let battle_commands = {
            P1: $('#P1-command').val(),
            P2: $('#P2-command').val(),
        }
        $.ajax({
            type: 'POST',
            url: 'battle',
            data: {
                battle_id: $('#battle_id').val(),
                battle_commands: battle_commands,
            },
        })
        .done(function(response) {
            // TODO:結果反映
            $('html').html(response);
        })
    });
})
