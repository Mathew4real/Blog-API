from .  import views
from django.urls import path



urlpatterns = [
    path("register/",views.UserRegistration.as_view(), name="register_user"),
    path("create-blog",views.CreateBlog.as_view(),name="create_blog"),
    path("blog",views.BlogList.as_view(),name="list_blogs"),
    path("update_blog/<int:pk>/",views.UpdateBlog.as_view()),
    path("update_blog/<int:pk>/",views.UpdateBlog.as_view()),
    path("delete_blog/<int:pk>/",views.DeleteBlog.as_view()),
    path("user_profile/<int:pk>/",views.UserProfile.as_view()),
]
