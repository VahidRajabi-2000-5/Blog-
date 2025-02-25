from django.urls import path

from . import views


urlpatterns = [
    path("signup/", views.SignUpView.as_view(), name="signup"),
    path("profile/edit/", views.ProfileEditView.as_view(), name="profile_edit"),
    path("<int:pk>/profile/", views.ProfileView.as_view(), name="profile_view"),
]
