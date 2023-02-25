"""BookStore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),
    # User management
    #path('accounts/', include("django.contrib.auth.urls")), # This line of code has already a pre-defined routes like login,logout ...
    path("accounts/", include("allauth.urls")), # Since we're using all-auth we need to changed routes as well
    # path("accounts/", include("accounts.urls")),
    path('', include('pages.urls')),
]


# This route is already made by the django.contrib.auth.urls
# urlpatterns = [
#     path("login/", views.LoginView.as_view(), name="login"),
#     path('logout/', views.LogoutView.as_view(), name="logout"),
#     
#         
#     path("password-change/", views.PasswordChangeView.as_view(), name="password_change"),
#     path("password-change/done/", views.PasswordChangeDoneView.as_view(), name="password_change_done"),
#     path("password-reset/", views.PasswordResetView.as_view(), name="password_reset"),
#     path("password-reset/done/", views.PasswordResetDoneView.as_view(), name="password_reset_done"),
#     path("reset/<uidb64>/<token>/", views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
#     path("reset/done/", views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
# ]