from django.shortcuts import render
from django.http import HttpResponse


def din_action(request):
    caller = request.GET['caller']
    recipient = request.GET['recipient']
    return HttpResponse("Hello, world. You're at the DIN Action index.")