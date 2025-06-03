


$('#itemCreationForm').submit(function(event){
    event.preventDefault();
    let form = $(this);
    let data = {};
    $.each($(form).serializeArray(), function(index, field){
        data[field.name] = field.value;
    });
    $.ajax(form.attr('action'), {
      'type': 'POST',
      'async': true,
      'dataType': 'json',
      'data': data,
      'success': function(response){

        const myModal = new bootstrap.Modal(document.getElementById('itemCreationForm'))
        myModal.hide();

        document.getElementById('items').innerHTML += response.html;

      },
    });
});