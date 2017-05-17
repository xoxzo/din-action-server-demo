from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def index(request):
    template = loader.get_template('din_action/index.html')
    return HttpResponse(template.render(request))

def din_action(request):
    caller = request.GET.get('caller',None)
    recipient = request.GET.get('recipient',None)

    mp3_file = "http://anonaka.github.io/100baigaeshi.mp3"
    action_str = "playback %s" % mp3_file

    print("Caller: ",caller)
    print("Recipient: ",recipient)
    print("Action: ",action_str)
    return HttpResponse(action_str)