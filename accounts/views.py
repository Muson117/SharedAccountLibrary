''' all views for accounts app '''
from django.shortcuts import render, get_object_or_404
from accounts.models import Account #, Employee

# Create your views here.
def index(request):
    ''' landing page '''
    available_account_list = Account.objects.order_by('account_taken_at')
    context = {'available_account_list': available_account_list,}
    return render(request, 'accounts/index.html', context)

def accountlist(request, account_id):
    ''' list all accounts '''
    account = get_object_or_404(Account, pk=account_id)
    context = {'account' : account,}
    return render(request, 'accounts/accountlist.html', context)

def pass_change():
    ''' change password for given account '''
    return
