from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect


def home(request):
    add_ans = 0
    data = {}
    try:
        # n1 = int(request.GET['num1'])
        # n2 = int(request.GET['num2'])

        # other method to get the value
        # n1 = int(request.GET.get('num1'))
        # n2 = int(request.GET.get('num2'))
        # add_ans = n1+n2

        # POST Method
        if request.method == 'POST':
            n1 = int(request.POST.get('num1'))
            n2 = int(request.POST.get('num2'))
            add_ans = n1+n2
            data = {
                'n1': n1,
                'n2': n2,
                'output': add_ans
            }

            url = f"/ans/?output={add_ans}"
            # return HttpResponseRedirect(url)
            return redirect(url)

    except:
        pass
    return render(request, 'index.html', data)


def ans(request):
    if request.method == 'GET':
        output = request.GET.get('output')

    return render(request, "ans.html", {'output': output})


def submitform(request):
    add_ans = 0
    data = {}
    try:
        if request.method == 'POST':
            n1 = int(request.POST.get('num1'))
            n2 = int(request.POST.get('num2'))
            add_ans = n1+n2
            data = {
                'n1': n1,
                'n2': n2,
                'output': add_ans
            }

            return HttpResponse(add_ans)

    except:
        pass
