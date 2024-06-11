from django.shortcuts import render
from django.http import HttpResponse



def seller_index_view(request):
    return HttpResponse("I am from seller side")