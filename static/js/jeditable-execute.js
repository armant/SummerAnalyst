$('.edit').each(function(){
	$('.edit.firm-name').editable('/dashboard/edit-firm-name/', {
		submitdata: {csrfmiddlewaretoken: CSRF},
	});

	$('.edit.contact-name').editable('/dashboard/edit-contact-name/', {
		submitdata: {csrfmiddlewaretoken: CSRF},
	});

	$('.edit.contact-position').editable('/dashboard/edit-contact-position/', {
		submitdata: {csrfmiddlewaretoken: CSRF},
	});
});

$('.editable').each(function(){
	$('.editable.app-status').editable('/dashboard/edit-app-status/', {
		submitdata: {csrfmiddlewaretoken: CSRF},
		data: {'C': 'Considering', 'A': 'Applying',
		       '1': 'Preparing for the 1-round', 
		       '2': 'Preparing for the 2-round',
		       '3': 'Preparing for the 3-round',
		       '4': 'Preparing for the 4-round',
		       '5': 'Preparing for the 5-round',
		       '6': 'Preparing for the 6-round',
		       '7': 'Preparing for the 7-round',
		       '8': 'Preparing for the 8-round',
		       '9': 'Preparing for the 9-round',
		       'S': 'Preparing for the Superday',
		},
		type: "select",
		submit: "OK",
	});
});