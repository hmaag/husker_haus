from django.forms import ModelForm
from .models import Post
from urllib.parse import urlparse

class CreateForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(CreateForm, self).__init__(*args, **kwargs)
        self.fields['title'].label = "title"
        self.fields['url'].label = "url"

    class Meta:
        model = Post
        fields = ['title', 'url']

    # def clean(self):
    #     parsed = urlparse(self.cleaned_data['url'])
    #     shortend = parsed.scheme + "://" + parsed.netloc
    #     self.cleaned_data['url'] = shortend