from django.shortcuts import render
from django.http import HttpResponse
from .models import DinAction


def index(request):
    #DinAction(action_text='playback http://anonaka.github.io/100baigaeshi.mp3').save()
    actions = DinAction.objects.all()

    context = {'actions': actions}
    return render(request, 'din_action/index.html', context)


def din_action(request):
    caller = request.GET.get('caller',None)
    recipient = request.GET.get('recipient',None)

    mp3_file = "http://anonaka.github.io/100baigaeshi.mp3"
    action_str = "playback %s" % mp3_file

    print("Caller: ",caller)
    print("Recipient: ",recipient)
    print("Action: ",action_str)
    return HttpResponse(action_str)