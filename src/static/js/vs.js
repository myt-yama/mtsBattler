// bgmの再生
$(document).ready( function(){
    document.getElementById('bgm').play();
});

// プレイヤー選択ボタン押下時にチーム選択をさせる
$(function () {
    $('.choose_button').on('click', function () {
        $(this).hide();
        $(this).next('.choose_team').show();
        $(this).parent().find('.chosen_monster').attr('id', 'target')
    });
});

// キャラ選択モーダル
$(document).ready(function() {
    // チーム選択ボタン押下でキャラ選択画面に移る
    $('.modaal').modaal({
        before_open: function() {
            $.ajax({
                type: 'post',
                url: 'battle',
                data: {
                    team: $('#target').parent().prev('.choose_team').find('.team option:selected').data("team"),
                },
            })
            .done(function(response) {
                $('#choice').html(response);
            })
        },
        content_source: '#modal',
        // is_locked: true,
        // hide_close: true
    });

    // キャラ決定
    $('#choice').on('click', '.decide-character', function(){
        $.ajax({
            type: 'POST',
            url: 'battle/register',
            data: {
                id: $(this).data("key"),
            },
        })
        .done(function(response) {
            $('.modaal').modaal('close');
            $('#target').html(response['team'] + '-' + response['name']);
            $('#target').parent().prev('.choose_team').find('.team option:selected', false);
            $('#target').removeAttr('id');
        })
        .fail(function(response) {
            console.log('fail');
        })
    });

    // バトルページへhiddenでモンスター情報を渡す
    $('.wrapper').on('click', '#go-battle', function(){
        var first_character = $('.first-character').find('.chosen_monster').html();
        $('#player1').val(first_character);
        var second_character = $('.second-character').find('.chosen_monster').html();
        $('#player2').val(second_character);
    });

})
