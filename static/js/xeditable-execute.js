$.fn.editable.defaults.mode = 'inline';

$(document).ready(function() {
    $('.firm-name').editable();
    $('.contact-name').editable();
    $('.contact-position').editable();
    $('.firm-status').editable({
    	showbuttons: false,
    	source: ['Considering', 'Applying', 'Preparing for the 1-round', 
		         'Preparing for the 2-round', 'Preparing for the 3-round',
		         'Preparing for the 4-round', 'Preparing for the 5-round',
		         'Preparing for the 6-round', 'Preparing for the 7-round',
		         'Preparing for the 8-round', 'Preparing for the 9-round',
		         'Preparing for the Superday'],
    });
});