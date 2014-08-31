from django import forms
from djangular.forms.angular_model import NgModelFormMixin

from models import Firm

class FirmForm(NgModelFormMixin, forms.ModelForm):
    class Meta:
        model = Firm
        fields = ('name', 'app_status', 'deadline', 'reminder_date', 
                'reminder_recurrence_number', 'reminder_recurrence_type', )