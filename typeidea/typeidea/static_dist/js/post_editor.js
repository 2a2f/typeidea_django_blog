(function($){
    var $content_md = $('#div_id_content_md');
    var $content_ck = $('#div_id_content_ck');
    var $is_md = $('input[name=is_md]');
    var switch_editor = function(is_md) {
        if (is_md) {
            $content_md.show();
            $content_ck.hide();
        } else {
            $content_md.hide();
            $content_ck.show();
        }
    }
    $is_md.on('click', function() {
        switch_editor($(this).is(':checked'));
    });
    switch_editor($is_md.is(':checked'));
})(jQuery);

<script
    src="https://code.jquery.com/jquery-3.3.1.min.js"
    integrity="sha256-FgpCb/KJQlLNfOu91ta32o/NMZxltwRo8QtmkMRdAu8="
    crossOrigin="anonymous"></script>