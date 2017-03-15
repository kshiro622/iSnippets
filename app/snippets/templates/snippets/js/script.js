$(document).ready(function () {
    $('.btn-delete').on('click', function () {
        var snippetId = $(this).attr('data-id');
        console.log(snippetId);
    });
});