from django.urls import path

from application.account.views import RegistrationView

urlpatterns = [
    path('register/', RegistrationView.as_view())

]