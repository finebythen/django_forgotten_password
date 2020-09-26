from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    # --> Login & Logout
    path('login/', views.loginPage, name="Login"),
    path('logout/', views.logoutUser, name="Logout"),

    # --> Main View
    path('', views.MainView, name="Main"),

    # --> Password Reset
    path('reset_password/',
         auth_views.PasswordResetView.as_view(template_name="app_forgotten_pw/password_reset.html"),
         name="reset_password"),

    path('reset_password_sent/',
         auth_views.PasswordResetDoneView.as_view(template_name="app_forgotten_pw/password_reset_sent.html"),
         name="password_reset_done"),

    path('reset/<uid64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name="app_forgotten_pw/password_reset_form.html"),
         name="password_reset_confirm"),

    path('reset_password_complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name="app_forgotten_pw/password_reset_done.html"),
         name="password_reset_complete"),
]
