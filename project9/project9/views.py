from django.http import HttpResponse
from django.shortcuts import render
from service.models import Service
from news.models import News
from django.core.paginator import Paginator


def home(request):
    service_data = Service.objects.all().order_by(
        'service_title')  # Ascending order
    service_data = Service.objects.all().order_by(
        '-service_title')  # Descending order
    news_data = News.objects.all()
    paginator = Paginator(service_data, 2)
    page_number = request.GET.get('page')
    ServiceDatatfinal = paginator.get_page(page_number)
    # service_data = Service.objects.all().order_by('service_title')
    # if request.method == 'GET':
    #     st = request.GET.get('servicename')
    #     if st != None:
    #         # service_data = Service.objects.filter(service_title=st)
    #         service_data = Service.objects.filter(service_title__icontains=st)
    data = {
        'service_data': ServiceDatatfinal,
        # 'news_data': news_data,
    }
    return render(request, "index.html", data)


def about_us(request):
    return render(request, "about-us.html")


def contact(request):
    return render(request, "contact-us.html")


def service(request):
    return render(request, "our-services.html")


def newsDetails(request, slug):
    news_detail = News.objects.get(news_slug=slug)
    data = {
        'news_detail': news_detail
    }
    return render(request, 'newsdetail.html', data)
