from django.urls import path
from .views import login_request, LogoutPage, register_request, edit


app_name="users"

urlpatterns = [
    path("edit/" ,edit, name="edit"),
    path("login/", login_request, name="login"),
    path("logout/", LogoutPage, name="logout"),
    path("register/", register_request, name="register"),
    
]
