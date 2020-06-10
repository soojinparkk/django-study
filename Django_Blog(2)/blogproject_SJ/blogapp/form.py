from django import forms
from .models import Blog

class BlogPost(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'body']
        

# 이렇게 Model에 의존하지 않고 From 형식으로 변형 가능
# class BlogPost(forms.Form):
#    email = forms.EmailField()
#    files = forms.FileField()
#    url = forms.URLField()
#    words = forms.CharField(max_length=200)
#    max_number = form.ChoiceField(choices=[('1','one'),('2','two'),('3','three')])