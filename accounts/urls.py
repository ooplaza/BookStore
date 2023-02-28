# This isn't needed anymore because django-allauth did the job already for the routes

from django.urls import path
from . import views


# urlpatterns = [
#     path("signup/", views.SignupPageView.as_view(), name="signup"),
# ]



# This route is already made by the django auth app
# urlpatterns = [
#     path("login/", views.LoginView.as_view(), name="login"),
#     path('logout/', views.LogoutView.as_view(), name="logout"),
    
#     path("password-change/", views.PasswordChangeView.as_view(), name="password_change"),
#     path("password-change/done/", views.PasswordChangeDoneView.as_view(), name="password_change_done"),
#     path("password-reset/", views.PasswordResetView.as_view(), name="password_reset"),
#     path("password-reset/done/", views.PasswordResetDoneView.as_view(), name="password_reset_done"),
#     path("reset/<uidb64>/<token>/", views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
#     path("reset/done/", views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
# ]
