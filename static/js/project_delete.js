
$('.product_delete').click(function(){
    let confirmation = confirm('Are you sure?');
    if (! confirmation){
        return;
    }
    let btn = $(this)
    $.ajax(btn.data('url'), {
      'type': 'POST',
      'async': true,
      'dataType': 'json',
      'data': {
        'csrfmiddlewaretoken': $('[name = "csrfmiddlewaretoken"]').val()
      },
      'success': function(response){
            btn.parent('div').remove();
      }
    })
});


