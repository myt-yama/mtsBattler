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
})
