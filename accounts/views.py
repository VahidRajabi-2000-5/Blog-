from django.views import generic
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.urls import reverse_lazy

    
    


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy("login")

class ProfileView(generic.DetailView):
    model = User
    template_name = "registration/profile_view.html"

class ProfileEditView(generic.UpdateView):
    model = User
    fields = [
        "username",
        "first_name",
        "last_name",
        "email",
    ]
    template_name = "registration/profile_change.html"
    success_url = reverse_lazy("profile_edit")

    def get_object(self, queryset=None):
        return self.request.user
