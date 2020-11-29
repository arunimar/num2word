from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from num2words import num2words


class DashboardView(View):

    def get(self, request):
        return render(request, 'dashboard.html', context={})

    def post(self, request):
        context = {}
        number = request.POST.get('number')
        if number and number.isnumeric() and int(number) <= 1000000:
            context['result'] = num2words(request.POST.get('number')).title()
            context['number'] = request.POST.get('number')
        return render(request, 'dashboard.html', context)
