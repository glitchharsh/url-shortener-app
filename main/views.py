from django.shortcuts import render, redirect
from .models import Url
import uuid


def index(request):
    link = None
    slug = None
    if request.method == 'POST':
        link = request.POST.get('link')
        if len(link) != 0:
            slug = str(uuid.uuid4())[:6]
            obj = Url(link=link, uid=slug)
            obj.save()
    var = {
        'link': link,
        'slug': slug,
    }
    return render(request, 'index.html', var)


def site(request, pk):
    url_details = Url.objects.get(uid=pk)
    link = url_details.link
    if link[:8] == 'https://' or link[:7] == 'http://':
        return redirect(url_details.link)
    return redirect('http://' + url_details.link)
