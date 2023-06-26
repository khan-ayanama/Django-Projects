from django.http import HttpResponse
from django.shortcuts import render
from .forms import userForm


def home(request):
    final_ans = 0
    fn = userForm()
    # print(fn.num1+fn.num2)
    data = {
        'form': fn
    }
    # n1 = int(request.POST.get('num1'))
    # n2 = int(request.POST.get('num1'))
    # print(n1+n2)
    # try:
    #     if request.method == 'POST':
    #         n1 = int(request.POST.get('num1'))
    #         n2 = int(request.POST.get('num1'))
    #         final_ans = n1 + n2
    #         data = {
    #             'forms': fn,
    #             'ouput': final_ans
    #         }
    # except:
    #     pass
    return render(request, 'index.html', data)
