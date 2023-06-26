from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    ans = ''
    try:
        if request.method == "POST":
            num = eval(request.POST.get('num'))
            if num % 2 == 0:
                ans = "Number is Even"
            else:
                ans = "Number is Odd"
    except:
        ans = "Please enter the value "
    return render(request, "index.html", {'ans': ans})
