from django.shortcuts import render, redirect, get_object_or_404
from .models import URL
from .utils import generate_short_code


def shorten_url(request):
    if request.method == 'POST':
        long_url = request.POST.get('long_url')
        existing_url = URL.objects.filter(long_url=long_url)
        if existing_url:
            short_code = existing_url.short_code 
        else:
            short_code = generate_short_code() 
            new_url = URL(long_url=long_url, short_code=short_code)  
            new_url.save()
        return render(request, 'shortener/result.html', {'short_code': short_code})  
    return render(request, 'shortener/shorten.html') 




def redirect_url(request, short_code):
    url_entry = get_object_or_404(URL, short_code=short_code)
    url_entry.clicks += 1
    url_entry.save()
    return redirect(url_entry.long_url)
