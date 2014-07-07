from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from models import Firm, Contact


# Create your views here.
@login_required
def index(request):
    firms_list = Firm.objects.filter(user=request.user)
    contacts_dict = {}
    for firm in firms_list:
        sub_contact_list = Contact.objects.filter(firms=firm)
        contacts_dict[firm] = sub_contact_list
    context = {'contacts_dict': contacts_dict}
    return render(request, 'dashboard/index.html', context)