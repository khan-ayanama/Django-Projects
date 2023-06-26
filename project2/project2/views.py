from django.http import HttpResponse
from django.shortcuts import render


# Rendering html page
# def home(request):
#     return render(request, "index.html")

# Rending HTML page with dynamic data

def home(request):
    data = {
        'title': 'Master Page',
        'clist': ['Python', 'Javascript', 'C++'],
        'personDetail': [
            {'name': 'Ayan', 'Phone': 9888888888},
            {'name': 'Naeem', 'Phone': 944488888}
        ],
        'num': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    }
    return render(request, "index.html", data)


def aboutUs(request):
    return HttpResponse("You called about us function")


def course(request):
    return HttpResponse("You called course page")


def courseDetails(request, courseId):
    return HttpResponse(courseId)
