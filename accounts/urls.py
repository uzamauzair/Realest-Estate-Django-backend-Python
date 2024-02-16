from django.urls import path
from .views import SignupView

urlpatterns = [
    path('signup',SignupView.as_view()) #The as_view() method is used when your view is a class-based view.
]
