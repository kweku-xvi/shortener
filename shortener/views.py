import pyshorteners
from django.contrib import messages
from django.shortcuts import render


def url_shortener(request):
    if request.method == 'POST':
        shortener = pyshorteners.Shortener()
        url = request.POST.get('url')
        short_url = shortener.tinyurl.short(url)
        messages.success(request, 'URL Shortened!')

        context = {
            'url':url,
            'short_url':short_url
        }

        return render(request, 'shortener/url_shortener.html', context)
    return render(request, 'shortener/url_shortener.html')