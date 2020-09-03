from django.contrib import admin
from django import forms

# Register your models here.
from django_test.models import Post
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

class PostAdmin(admin.ModelAdmin):
    list_display = ('uuid', 'title', 'created_at', 'updated_at') # field display index
    list_per_page = 10
    form = PostForm

admin.site.register(Post, PostAdmin)