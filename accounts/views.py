from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.template import loader
from accounts.models import Account, Employee

# Create your views here.
def index(request):
    available_account_list = Account.objects.order_by('account_taken_at')
    context = { 'available_account_list': available_account_list, }
    return render(request, 'accounts/index.html', context)
    

def login(request, account_id):
    account = get_object_or_404(Account, pk=account_id)
    '''
    try:
        account = Account.objects.get(pk=account_id)
    except Account.DoesNotExist:
        raise Http404("Account does not exist")
    '''
    return HttpResponse("Available account is %s." % account)

