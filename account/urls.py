from django.urls import path
from .views import *



urlpatterns = [
    path('register/', RegistrationView.as_view()),
    path('activate/', ActivationView.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/',LogoutView.as_view()),
    path('forgot-password/',ForgotPasswordView.as_view()),
    path('complete-password-reset/',ForgotPasswordCompleteView.as_view()),

]