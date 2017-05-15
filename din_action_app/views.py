from django.shortcuts import render
from django.http import HttpResponse


def din_action(request):
    caller = request.GET.get('caller',None)
    recipient = request.GET.get('recipient',None)
    return HttpResponse("Hello, world. You're at the DIN Action index.")