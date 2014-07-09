$.fn.editable.defaults.mode = 'inline';

$(document).ready(function() {
    
    //text fields
    $('.firm-name').editable({
    	type: 'text',
    	url: 'edit-firm-name/',
    	params: {
    		csrfmiddlewaretoken: CSRF,
    	},
    });

    $('.contact-name').editable({
    	type: 'text',
    	url: 'edit-contact-name/',
    	params: {
    		csrfmiddlewaretoken: CSRF,
    	},
    });

    $('.contact-position').editable({
    	type: 'text',
    	url: 'edit-contact-position/',
    	params: {
    		csrfmiddlewaretoken: CSRF,
    	},
    });

	//drop-downs    
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
    });
    
    $('.firm-recurring-type').editable({
    	type: 'select',
    	url: 'edit-firm-recurring-type/',
    	params: {
    		csrfmiddlewaretoken: CSRF,
    	},
    	showbuttons: false,
    	source: [' ', 'day(s)', 'week(s)', 'month(s)', 'year(s)'],
    });

    //datepickers
    $('.firm-deadline').editable({
    	type: 'date',
    	url: 'edit-firm-deadline/',
    	params: {
    		csrfmiddlewaretoken: CSRF
    	},
    	viewformat: 'M d, yyyy',
    });

    $('.firm-remind-date').editable({
    	type: 'date',
    	url: 'edit-firm-remind-date/',
    	params: {
    		csrfmiddlewaretoken: CSRF
    	},
    	viewformat: 'M d, yyyy',
    });

});