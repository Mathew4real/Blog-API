from .  import views
from django.urls import path,include





urlpatterns = [
    path("register/",views.UserRegistration.as_view(), name="register user"),
    path("",views.CreateBlog.as_view())
]
