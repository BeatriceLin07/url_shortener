from django.shortcuts import render, redirect, get_object_or_404
from .models import URL
from .utils import generate_short_code
from django.db.models import F


def shorten_url(request):
    if request.method == 'POST':
        long_url = request.POST.get('long_url')
        existing_url = URL.objects.filter(long_url=long_url).first()
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
    URL.objects.filter(short_code=short_code).update(clicks=F('clicks') + 1)
    return redirect(url_entry.long_url)
