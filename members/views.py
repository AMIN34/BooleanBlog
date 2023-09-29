from django.views import generic
from django.urls import reverse_lazy
from .forms import SignUpForm, EditProfileForm
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.messages.views import SuccessMessageMixin

class ChangePasswordView( SuccessMessageMixin,PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy("home") #This will redirect User to homepage upon successful password change
    success_message = "password changed succesfully!"
    
class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name = "registration/registerUser.html"  # so django don't confuse between the two templates folder
    success_url = reverse_lazy("login")  # makeSure it is login i.e same as your template file name
    
    # def get_success_url(self):
    #     if next_url := self.request.POST.get('next'):
    #         return next_url
    #     else:
    #         return super().get_success_url()
    
# Use Update view to change view
class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = "registration/edit_profile.html"  # so django don't confuse between the two templates folder
    success_url = reverse_lazy("home")
    
    # To fill the form about a particular user
    def get_object(self):
        return self.request.user