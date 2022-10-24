from django.shortcuts import render
from django.views.generic import View
from django.template.response import TemplateResponse
from .models import Customer


class GenerateCustomerView(View):
    http_method_names = ['get', 'post']

    def get(self, request, *args, **kwargs):
        context = {'customers': Customer.objects.all()}
        return TemplateResponse(request, 'customers/customers_list.html', context)

    def post(self, request, *args, **kwargs):
        customer = Customer()
        customer.save()
        return self.get(request)
