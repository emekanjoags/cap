from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from account.models import Referral
from authentication.models import Profile
from testimony.models import Testimony

def homePage(request):
    content = Testimony.objects.all().order_by("-time")[:3]
    contex = {
        'content':content
    }
    return render(request, 'index.html', contex)

def faq(request):
    return render(request, 'faq.html')

@login_required(login_url='login-page')
def referral(request):
    profile = Profile.objects.get(user=request.user)
    referral = Referral.objects.filter(referrer=request.user)
    withdraw_btn = 0
    if profile.referred_active % 5 == 0:
        withdraw_btn = 1

    if profile.referred_active == 0:
        withdraw_btn = 0
    context = {
        'referral':referral,
        'profile':profile,
        'withdraw_btn':withdraw_btn
    }
    return render(request, 'referral/referral.html', context)