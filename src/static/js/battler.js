$(document).ready( function(){
    document.getElementById('bgm').play();
});
// PURESS ANY BUTTONを押すと選択肢に切り替わる
$(function () {
    $('#press-any-button').click(function () {
        $('#press-any-button').hide();
        $('#menu_choice').show();
        $('#press-any-button input').prop('checked', false);
        $('#move-farm input').prop('checked', true);
        $('#move-farm input').focus();
    });
});

// 選択肢移動で移動音を出す
$(function () {
    $('label').mouseover(function() {
        document.getElementById("move").currentTime = 0;
		document.getElementById("move").play();
    });
});

// クリックした時に音を出す
$(function () {
    $('label').click(function() {
        document.getElementById('decide').play();
    });
});

// クリックイベントとエンターイベントを同じ動作にしたい
$(element).on("keydown", function(e) {
    if(e.keyCode === 13) {
        $(this).trigger("click");
    }
});