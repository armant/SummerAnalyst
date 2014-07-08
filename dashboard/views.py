from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from models import Firm, Contact


# Create your views here.
@login_required
def index(request):
    firms_list = Firm.objects.filter(user=request.user)
    contacts_dict = {}
    for firm in firms_list:
        sub_contact_list = Contact.objects.filter(firms=firm)
        contacts_dict[firm] = sub_contact_list
    context = {'firms_list': firms_list, 'contacts_dict': contacts_dict}
    return render(request, 'dashboard/index.html', context)


@login_required
def edit_firm_name(request):
    new_firm_name = request.POST.get('value')
    firm_id = request.POST.get('id')
    required_firm = Firm.objects.get(id=firm_id)
    required_firm.name = new_firm_name
    required_firm.save()
    return HttpResponse(new_firm_name)


@login_required
def edit_contact_name(request):
    new_contact_name = request.POST.get('value')
    contact_id = request.POST.get('id')
    required_contact = Contact.objects.get(id=contact_id)
    required_contact.name = new_contact_name
    required_contact.save()
    return HttpResponse(new_contact_name)


@login_required
def edit_contact_position(request):
    new_contact_position = request.POST.get('value')
    contact_id = request.POST.get('id')
    required_contact = Contact.objects.get(id=contact_id)
    required_contact.position = new_contact_position
    required_contact.save()
    return HttpResponse(new_contact_position)

@login_required
def edit_app_status(request):
    new_app_status = request.POST.get('value')
    firm_id = request.POST.get('id')
    required_firm = Firm.objects.get(id=contact_id)
    required_firm.app_status = new_app_status
    required_firm.save()
    return HttpResponse(new_app_status)