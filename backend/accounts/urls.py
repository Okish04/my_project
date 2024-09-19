from django.urls import path
from accounts.views import ForgotPasswordView, LoginView, SignupView, LogoutView, UserView

urlpatterns = [
    path('forgot-password', ForgotPasswordView.as_view()),
    path('signup', SignupView.as_view()),
    path('login', LoginView.as_view()),
    path('logout', LogoutView.as_view()),
    path('user', UserView.as_view()),
]
