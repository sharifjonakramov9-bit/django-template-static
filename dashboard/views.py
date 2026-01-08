from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


def home_page(request: HttpRequest) -> HttpResponse:
    data = {
        'user': {
            'name': 'Ali'
        },
        'dashboard': {
            'total_revenue': 30_450.00
        }
    }
    return render(request=request, template_name='index.html', context=data)
    