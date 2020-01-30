$(document).ready(function() {
    // モンスター生成&仮登録
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
        },
        content_source: '#modal',
        is_locked: true,
        hide_close: true
    });

    // 本登録orキャンセル
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
    $('#select-box').on('click', '.delete-button', function(){
        let key = $(this).data('key');
        let team = $(this).data('team');
        $.ajax({
            type: 'POST',
            url: 'delete',
            data: {
                key: key,
                team: team
            },
        })
        .done(function(response) {
            console.log('info');
            $('#select-box').html(response);
        })
        .fail(function(){
            console.log('fail');
        })
    });
})
