$.fn.editable.defaults.mode = 'inline';

$(document).ready(function() {
    
  // text fields
  $('.firm-name').editable({
  	type: 'text',
   	url: 'edit-firm-name/',
   	params: {
      csrfmiddlewaretoken: CSRF,
    },
    emptytext: 'company/group name',
  });

  $('.contact-name').editable({
   	type: 'text',
   	url: 'edit-contact-name/',
   	params: {
      csrfmiddlewaretoken: CSRF,
    },
    emptytext: 'contact name',
  });

  $('.contact-position').editable({
   	type: 'text',
   	url: 'edit-contact-position/',
   	params: {
      csrfmiddlewaretoken: CSRF,
    },
    emptytext: 'position',
  });

  $('.firm-recurring-number').editable({
   	type: 'text',
   	url: 'edit-firm-recurring-number/',
   	params: {
      csrfmiddlewaretoken: CSRF,
    },
    emptytext: '0',
  });

  $('.contact-recurring-number').editable({
   	type: 'text',
   	url: 'edit-contact-recurring-number/',
   	params: {
  	  csrfmiddlewaretoken: CSRF,
    },
    emptytext: '0',
  });

  // drop-downs    
  $('.firm-status').editable({
   	type: 'select',
   	url: 'edit-firm-status/',
   	params: {
      csrfmiddlewaretoken: CSRF,
    },
    showbuttons: false,
    source: [' ', 'Considering', 'Applying', 'Preparing for the 1-round', 
	    'Preparing for the 2-round', 'Preparing for the 3-round',
	    'Preparing for the 4-round', 'Preparing for the 5-round',
	    'Preparing for the 6-round', 'Preparing for the 7-round',
        'Preparing for the 8-round', 'Preparing for the 9-round',
        'Preparing for the Superday', 'Got an offer'],
    emptytext: 'no app status',
  });
    
  $('.firm-recurring-type').editable({
   	type: 'select',
   	url: 'edit-firm-recurring-type/',
   	params: {
      csrfmiddlewaretoken: CSRF,
    },
   	showbuttons: false,
   	source: [' ', 'day(s)', 'week(s)', 'month(s)', 'year(s)'],
    emptytext: 'no default periodic reminder ',
  });

  $('.contact-recurring-type').editable({
   	type: 'select',
   	url: 'edit-contact-recurring-type/',
   	params: {
      csrfmiddlewaretoken: CSRF,
    },
    showbuttons: false,
    source: [' ', 'day(s)', 'week(s)', 'month(s)', 'year(s)'],
    emptytext: 'no periodic reminder',
  });

  // datepickers
  $('.firm-deadline').editable({
   	mode: 'popup',
   	type: 'date',
   	url: 'edit-firm-deadline/',
   	params: {
      csrfmiddlewaretoken: CSRF
    },
    viewformat: 'M d, yyyy',
    datepicker: {
      todayBtn: 'linked',
      todayHighlight: true,
    },
    showbuttons: false,
    emptytext: 'no deadline',
  });

  $('.firm-remind-date').editable({
   	mode: 'popup',
   	type: 'date',
   	url: 'edit-firm-remind-date/',
   	params: {
      csrfmiddlewaretoken: CSRF
    },
    viewformat: 'M d, yyyy',
    datepicker: {
      todayBtn: 'linked',
      todayHighlight: true,
    },
    showbuttons: false,
    emptytext: 'no reminder',
  });

  $('.contact-last-contact').editable({
  	mode: 'popup',
   	type: 'date',
   	url: 'edit-contact-last-contact/',
   	params: {
      csrfmiddlewaretoken: CSRF
    },
    viewformat: 'M d, yyyy',
    datepicker: {
      todayBtn: 'linked',
      todayHighlight: true,
    },
    showbuttons: false,
    emptytext: 'never',
  });

  $('.contact-remind-date').editable({
   	mode: 'popup',
   	type: 'date',
   	url: 'edit-contact-remind-date/',
   	params: {
      csrfmiddlewaretoken: CSRF
    },
    viewformat: 'M d, yyyy',
    datepicker: {
      todayBtn: 'linked',
      todayHighlight: true,
    },
    showbuttons: false,
    emptytext: 'no specific date reminder',
  });

  // Periodic contact reminder and specific date contact reminder:
  // nullify one when the other one is clicked on.
  $('.contact-recurring-number, .contact-recurring-type').click(function() {
    $('#' + $(this).attr('data-pk') +
        '-remind-date').text('no specific date reminder');
    
    $.post('nullify-contact-remind-date/', {
      csrfmiddlewaretoken: CSRF,
      'contact_id': $(this).attr('data-pk'),
    });
  });

  $('.contact-remind-date').click(function() {
    $('#' + $(this).attr('data-pk') + '-recurring-number').text('0');
    $('#' + $(this).attr('data-pk') + 
        '-recurring-type').text('no periodic reminder');
        
    $.post('nullify-contact-remind-periodic/', {
      csrfmiddlewaretoken: CSRF,
      'contact_id': $(this).attr('data-pk'),
    });
  });

});


/*
  //Create a new firm: init editables 
  $('.new-firm').editable({
    url: 'new-firm-update/' //this url will not be used for creating new
                            //user, it is only for update
  });
 
  //Create a new firm: automatically show next editable
  $('.new-firm').on('save.newuser', function() {
    var that = this;
    setTimeout(function() {
      $(that).closest('a').next().find('.new-firm').editable('show');
    }, 200);
  });

  //Create a new firm: send input data to server
  $('#save-btn').click(function() {
    $('.new-firm').editable('submit', { 
      url: 'new-firm/', 
      ajaxOptions: {
        //dataType: 'json', //assuming json response
        //data: {csrfmiddlewaretoken: CSRF},
      },
            
      success: function(data, config) {
        if(data && data.id) { //record created, response like {"id": 2}
          //set pk
          $(this).editable('option', 'pk', data.id);
          //remove unsaved class
          $(this).removeClass('editable-unsaved');
          //show messages
          var msg = 'A new firm/group is saved.';
          $('#msg').addClass('alert-success').removeClass('alert-error').html(msg).show();
          $('#save-btn').hide(); 
          $(this).off('save.newuser');                     
        } 
        else if(data && data.errors){ 
          //server-side validation error, response like {"errors": {"username": "username already exist"} }
          config.error.call(this, data.errors);
        }               
      },
       
      error: function(errors) {
        var msg = '';
        if(errors && errors.responseText) { //ajax error, errors = xhr object
          msg = errors.responseText;
        } 
        else { //validation error (client-side or server-side)
          $.each(errors, function(k, v) { msg += k+": "+v+"<br>"; });
        } 
                
        $('#msg').removeClass('alert-success').addClass('alert-error').html(msg).show();
      },
    });
  });*/