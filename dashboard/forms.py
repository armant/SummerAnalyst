from django.forms import ModelForm

from models import Firm, Contact 

class BaseModelForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name in self.fields:
            field = self.fields.get(field_name)
            if field:
                field.widget.attrs.update({
                    'placeholder': field_name
                })

class FirmForm(BaseModelForm):
    class Meta:
        model = Firm
        fields = ('name', 'app_status', 'deadline', 'reminder_date', 
                'reminder_recurrence_number', 'reminder_recurrence_type', )

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'position', 'last_contact_date', 
        	    'reminder_recurrence_number', 'reminder_recurrence_type', 
        	    'reminder_date', )
        name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Name'}))