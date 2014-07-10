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

    $('.firm-recurring-number').editable({
    	type: 'text',
    	url: 'edit-firm-recurring-number/',
    	params: {
    		csrfmiddlewaretoken: CSRF,
    	},
    });

    $('.contact-recurring-number').editable({
    	type: 'text',
    	url: 'edit-contact-recurring-number/',
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

    $('.contact-recurring-type').editable({
    	type: 'select',
    	url: 'edit-contact-recurring-type/',
    	params: {
    		csrfmiddlewaretoken: CSRF,
    	},
    	showbuttons: false,
    	source: [' ', 'day(s)', 'week(s)', 'month(s)', 'year(s)'],
    });

    //datepickers
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
        } ,
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
        } ,
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
        } ,
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
        } ,
    });

});