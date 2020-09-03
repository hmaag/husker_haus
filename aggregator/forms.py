from django.forms import ModelForm
from .models import Post, Comment
from urllib.parse import urlparse

class CreateForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(CreateForm, self).__init__(*args, **kwargs)
        self.fields['title'].label = "title"
        self.fields['url'].label = "url"

    class Meta:
        model = Post
        fields = ['title', 'url']

class CommentForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['content'].label = ""

    class Meta:
        model = Comment
        fields = ['content']