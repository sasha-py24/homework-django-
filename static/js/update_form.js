$('.item-update').click(function(event){
    event.preventDefault();
    let btn = $(this);
    $.ajax(btn.data('url'), {
      'type': 'GET',
      'async': true,
      'dataType': 'json',
      'success': function(response){
            $('#itemUpdateModalBody').html(response.html);
      }
    })
});

