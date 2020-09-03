from django.contrib import admin
from django import forms

# Register your models here.
from django_test.models import User


class UserForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(), help_text="This is the grey text")
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(), help_text="This is the grey text")

    class Meta:
        model = User
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError(
                "password and confirm_password does not match"
            )


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', )  # field display index
    list_per_page = 10
    form = UserForm


admin.site.register(User, UserAdmin)
