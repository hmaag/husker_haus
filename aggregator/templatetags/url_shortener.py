from urllib.parse import urlparse
from django import template

register = template.Library()

@register.filter
def url_shortener(value):
    parsed = urlparse(value)
    shortend = parsed.scheme + "://" + parsed.netloc
    return shortend