from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *


urlpatterns = [
    path('', index, name='index'),
    path('login/', login_view, name='login'),
    path('registration/', registration_view, name='registration'),
    path('logout/', logout_view, name='logout'),
    path('profile/', account_view, name='account'),

    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='login/authentication/reset_password.html'), name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name='login/authentication/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='login/authentication/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='login/authentication/password_reset_complete.html'), name='password_reset_complete'),

]

