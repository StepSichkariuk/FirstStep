from django.shortcuts import render
from django.views import View
from random import choice

class Home(View):
    def get(self, request):
        ch = ['Enjoy every moment', 'Feel the rain on your skin.', 'Never look back.', 'Hello world with django',]
        return render(request, 'home.html', context={'text': choice(ch), 'name':'Home page'})
    