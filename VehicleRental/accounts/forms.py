from django.contrib.auth import forms as auth_forms, get_user_model
from django import forms

UserModel = get_user_model()

class UserEditForm(auth_forms.UserChangeForm):

    class Meta:
        model = UserModel
        fields = '__all__'
        field_classes = {"username": auth_forms.UsernameField}



class UserCreateForm(auth_forms.UserCreationForm):
    class Meta:
        model = UserModel
        fields = ("username", "email",)
        field_classes = {"username": auth_forms.UsernameField}

    # password1 = forms.CharField(
    #     label= "Email",
    # )