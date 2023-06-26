from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    data = {}
    text = request.GET.get('inputText')
    upper_text = text.upper()
    data = {
        'upper_text':upper_text
    }
    ans = 'kuch hai!!'
    return render(request,"index.html",data)