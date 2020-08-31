from django.shortcuts import render
from django.views.generic.base import View
from django.contrib.auth.decorators import login_required

class MakeDonation(View):
    def get(self, request):
        context = {}
        return render(request, 'donation/make-donation.html')

class DashBoard(View):
    def get(self, request):
        context = {}
        return render(request, 'donation/dashboard.html')

@login_required(login_url='login-page')
def transactions(request):
    return render(request, 'donation/transactions.html')

    
