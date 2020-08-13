from django.shortcuts import render

posts = [
    {
        'author': 'Heath',
        'title': 'Post 1',
        'content': 'First post content',
        'date_posted': 'August 27, 2018',
        'url': 'huskermax.com'
    },
    {
        'author': 'Sabrina',
        'title': 'Post 2',
        'content': 'Second post content',
        'date_posted': 'August 28, 2018',
        'url': 'huskerhaus.com'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'aggregator/home.html', context)

def about(request):
    return render(request, 'aggregator/about.html', {'title': 'About'})
