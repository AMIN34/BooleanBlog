from django.urls import path
from .views import UserRegisterView, UserEditView, ChangePasswordView
# from django.contrib.auth import views as auth_view

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name="register"),
    path('edit_profile/', UserEditView.as_view(), name="edit_profile"),
    # path('password/', auth_view.PasswordChangeView.as_view(template_name="registration/password_change.html")),
    path('password/', ChangePasswordView.as_view(template_name="registration/password_change.html")),
]
