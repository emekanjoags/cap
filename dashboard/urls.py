from django.urls import path
from django.utils.decorators import decorator_from_middleware
from utilities.general_middleware import AuthCheckMiddleware, AuthCheckLoginMiddleware
from .views import MakeDonation, DashBoard, transactions

user_auth_decorator = decorator_from_middleware(AuthCheckLoginMiddleware)

app_name = 'dashboard'
urlpatterns = [
    path('donate', user_auth_decorator(MakeDonation.as_view()), name="donate" ),
    path('', user_auth_decorator(DashBoard.as_view()), name='dashboard'),
    path('transactions', transactions, name='transactions')
]