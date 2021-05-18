from django.http.response import HttpResponse
from random import choice
from string import ascii_lowercase, ascii_letters, digits, punctuation

from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'generator/home.html')

def generate(request):
    try:
        number = int(request.GET.get('simbols', '10'))
    except ValueError:
        return HttpResponse('<h1>Value Error</h1>')
    
    letters = list(ascii_letters) if request.GET.get('uppercase') else list(ascii_lowercase)

    if request.GET.get('numbers'):
        letters.extend(list(digits))

    if request.GET.get('special'):
        letters.extend(list(punctuation))

    password = ''
    for i in range(number):
        password += choice(letters)
        
    return render(request, 'generator/generator.html', {'password': password})