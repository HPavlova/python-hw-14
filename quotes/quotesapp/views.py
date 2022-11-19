from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
from .models import Quotes


# Create your views here.
def index(request):
    return render(request, 'quotesapp/quotesapp.html')


def filter_by_author(request):
    print(request)
    if request.method == 'POST':
        author_name = request.POST['author_name']
        print(author_name)
        if author_name == '':
            messages.add_message(request, messages.ERROR, 'Enter author name!')
            return redirect((reverse('quotesapp/quotesapp.html')))
        if author_name == 'undefined':
            messages.add_message(request, messages.INFO,
                                 'There is no author with this name!')
            return redirect((reverse('quotesapp/quotesapp.html')))
        quotes = Quotes.objects.filter(author=[author_name])
        return render(request, 'quotesapp/quotesapp.html', quotes)
    return redirect((reverse('quotesapp/quotesapp.html')))
