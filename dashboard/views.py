from django.shortcuts import *
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseBadRequest
import json
from django.template import RequestContext
from django.views.generic import TemplateView


from models import Firm, Contact
from forms import *


# Create your views here.
@login_required(login_url='/login/')
def index(request):
    firms_list = Firm.objects.filter(user=request.user)
    contacts_dict = {}
    for firm in firms_list:
        sub_contact_list = Contact.objects.filter(firms=firm)
        contacts_dict[firm] = sub_contact_list
    context = {'firms_list': firms_list, 'contacts_dict': contacts_dict}
    return render(request, 'dashboard/index.html', context)


@login_required(login_url='/login/')
def edit_firm_name(request):
    new_firm_name = request.POST.get('value')
    firm_id = request.POST.get('pk')
    required_firm = Firm.objects.get(pk=firm_id)
    required_firm.name = new_firm_name
    required_firm.save()
    return HttpResponse(new_firm_name)


@login_required(login_url='/login/')
def edit_contact_name(request):
    new_contact_name = request.POST.get('value')
    contact_id = request.POST.get('pk')
    required_contact = Contact.objects.get(pk=contact_id)
    required_contact.name = new_contact_name
    required_contact.save()
    return HttpResponse(new_contact_name)


@login_required(login_url='/login/')
def edit_contact_position(request):
    new_contact_position = request.POST.get('value')
    contact_id = request.POST.get('pk')
    required_contact = Contact.objects.get(pk=contact_id)
    required_contact.position = new_contact_position
    required_contact.save()
    return HttpResponse(new_contact_position)


@login_required(login_url='/login/')
def edit_firm_recurring_number(request):
    new_firm_recurring_number = request.POST.get('value')
    firm_id = request.POST.get('pk')
    required_firm = Firm.objects.get(pk=firm_id)
    try:
        converted = int(new_firm_recurring_number)
        if (converted < 0) or (converted > 32767):
            return HttpResponseBadRequest('Please enter a number between 0 and 32767.')
        else:
            required_firm.reminder_recurrence_number = converted
            required_firm.save()
            return HttpResponse(new_firm_recurring_number)
    except ValueError:
        if new_firm_recurring_number == '':
            required_firm.reminder_recurrence_number = 0
            required_firm.save()
            return HttpResponse('0')
        else:
            return HttpResponseBadRequest('Please enter a number between 0 and 32767.')


@login_required(login_url='/login/')
def edit_firm_status(request):
    new_app_status = request.POST.get('value')
    firm_id = request.POST.get('pk')
    required_firm = Firm.objects.get(pk=firm_id)
    for symbol, name in Firm.STATUSES:
        if name == new_app_status:
            required_firm.app_status = symbol
            break
    required_firm.save()
    return HttpResponse(new_app_status)


@login_required(login_url='/login/')
def edit_firm_recurring_type(request):
    new_type = request.POST.get('value')
    firm_id = request.POST.get('pk')
    required_firm = Firm.objects.get(pk=firm_id)
    for symbol, name in Firm.PERIODS:
        if name == new_type:
            required_firm.reminder_recurrence_type = symbol
            break
    required_firm.save()
    return HttpResponse(new_type)


@login_required(login_url='/login/')
def edit_firm_deadline(request):
    new_firm_deadline = request.POST.get('value')
    firm_id = request.POST.get('pk')
    required_firm = Firm.objects.get(pk=firm_id)
    if new_firm_deadline == '':
        required_firm.deadline = None
    else:
        required_firm.deadline = new_firm_deadline
    required_firm.save()
    return HttpResponse(new_firm_deadline)


@login_required(login_url='/login/')
def edit_firm_remind_date(request):
    new_firm_remind_date = request.POST.get('value')
    firm_id = request.POST.get('pk')
    required_firm = Firm.objects.get(pk=firm_id)
    if new_firm_remind_date == '':
        required_firm.reminder_date = None
    else:
        required_firm.reminder_date = new_firm_remind_date
    required_firm.save()
    return HttpResponse(new_firm_remind_date)


@login_required(login_url='/login/')
def edit_contact_last_contact(request):
    new_contact_last_contact = request.POST.get('value')
    contact_id = request.POST.get('pk')
    required_contact = Contact.objects.get(pk=contact_id)
    if new_contact_last_contact == '':
        required_contact.last_contact_date = None
    else:
        required_contact.last_contact_date = new_contact_last_contact
    required_contact.save()
    return HttpResponse(new_contact_last_contact)


@login_required(login_url='/login/')
def edit_contact_recurring_number(request):
    new_contact_recurring_number = request.POST.get('value')
    contact_id = request.POST.get('pk')
    required_contact = Contact.objects.get(pk=contact_id)
    try:
        converted = int(new_contact_recurring_number)
        if (converted < 0) or (converted > 32767):
            return HttpResponseBadRequest('Please enter a number between 0 and 32767.')
        else:
            required_contact.reminder_recurrence_number = converted
            required_contact.save()
            return HttpResponse(new_contact_recurring_number)
    except ValueError:
        if new_contact_recurring_number == '':
            required_contact.reminder_recurrence_number = 0
            required_contact.save()
            return HttpResponse('0')
        else:
            return HttpResponseBadRequest('Please enter a number between 0 and 32767.')


@login_required(login_url='/login/')
def edit_contact_recurring_type(request):
    new_type = request.POST.get('value')
    contact_id = request.POST.get('pk')
    required_contact = Contact.objects.get(pk=contact_id)
    for symbol, name in Contact.PERIODS:
        if name == new_type:
            required_contact.reminder_recurrence_type = symbol
            break
    required_contact.save()
    return HttpResponse(new_type)


@login_required(login_url='/login/')
def edit_contact_remind_date(request):
    new_contact_remind_date = request.POST.get('value')
    contact_id = request.POST.get('pk')
    required_contact = Contact.objects.get(pk=contact_id)
    if new_contact_remind_date == '':
        required_contact.reminder_date = None
    else:
        required_contact.reminder_date = new_contact_remind_date
    required_contact.save()
    return HttpResponse(new_contact_remind_date)


@login_required(login_url='/login/')
def nullify_contact_remind_date(request):
    contact_id = request.POST.get('contact_id')
    required_contact = Contact.objects.get(pk=contact_id)
    required_contact.reminder_date = None
    required_contact.save()
    return HttpResponse('')


@login_required(login_url='/login/')
def nullify_contact_remind_periodic(request):
    contact_id = request.POST.get('contact_id')
    required_contact = Contact.objects.get(pk=contact_id)
    required_contact.reminder_recurrence_number = 0
    required_contact.reminder_recurrence_type = 'B'
    required_contact.save()
    return HttpResponse('')


class NewFirmView(TemplateView):
    template_name = 'dashboard/index.html'

    def get_context_data(self, **kwargs):
        context = super(NewFirmView, self).get_context_data(**kwargs)
        context.update(firm_form = NgSlugForm(scope_prefix='firm_model'))
        return context



'''@login_required
@csrf_protect
def new_firm(request):
    firm_name = request.POST.get('new-firm-name')
    new_firm = Firm(firm_name)
    new_firm.user = request.user
    if not request.POST.get('new-firm-status'):
        new_firm.app_status = "B"
    else:
        new_firm.app_status = request.POST.get('new-firm-status')
    new_firm.deadline = request.POST.get('new-firm-deadline')
    new_firm.reminder_date = request.POST.get('new-firm-remind-date')
    new_firm.reminder_recurrence_number = request.POST.get('new-firm-recurring-number')
    new_firm.reminder_recurrence_type = request.POST.get('new-firm-recurring-type')
    if not request.POST.get('new-firm-recurring-type'):
        new_firm.reminder_recurrence_type = "B"
    else:
        new_firm.reminder_recurrence_type = request.POST.get('new-firm-recurring-type')
    new_firm.save()
    data = {}
    data['id'] = new_firm.id
    data['new-firm-name'] = new_firm.name
    data['new-firm-status'] = new_firm.app_status
    data['new-firm-deadline'] = new_firm.deadline
    data['new-firm-remind-date'] = new_firm.reminder_date
    data['new-firm-recurring-number'] = new_firm.reminder_recurrence_number
    data['new-firm-recurring-type'] = new_firm.reminder_recurrence_type
    return HttpResponse(json.dumps(data), content_type="application/json")
    return HttpResponse('')

@login_required(login_url='/login/')
def new_firm(request):
    if request.method == "POST":
        form = FirmForm(request.POST)

        if(form.is_valid()):
            print(request.POST['title'])
            message = request.POST['title']

        return HttpResponse(json.dumps({'message': message}))

    return render_to_response('contact/advert.html',
            {'form':AdvertForm()}, RequestContext(request))


    context = RequestContext(request)
    
    if request.method == 'POST':
        form = CandidatesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/dashboard/')
        else:
            print form.errors
    else:
        form = CandidatesForm()
    return render_to_response('add.html', {'CandidatesForm': CandidatesForm, 'form': form}, context)'''
