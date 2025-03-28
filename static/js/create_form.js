


$('#itemCreationForm').submit(function(event){
    event.preventDefault();
    let form = $(this)
    let formdata = new FormData(document.getElementById('#itemCreationForm'))
       $.ajax(form.attr('action'), {
      'type': 'POST',
      'async': true,
      'dataType': 'json',
      'data': formdata,
      'success': function(response){

        const myModal = new bootstrap.Modal(document.getElementById('#itemCreationForm'))
        myModal.addEventListener('hidden.bs.modal', event)

      },
    });
});