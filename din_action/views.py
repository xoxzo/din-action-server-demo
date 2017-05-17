from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import DinAction

g_action_id = 1


def index(request):
    global g_action_id
    actions = DinAction.objects.all()
    context = {'actions': actions, 'selected_id': int(g_action_id) - 1}
    return render(request, 'din_action/index.html', context)


def select_action(request):
    global g_action_id
    g_action_id = request.POST['action_id']
    return HttpResponseRedirect("/din-action/index")


def din_action(request):
    global g_action_id
    caller = request.GET.get('caller',None)
    recipient = request.GET.get('recipient',None)
    action = DinAction.objects.get(id=g_action_id)
    action_text = action.action_text
    print("Caller: ",caller)
    print("Recipient: ",recipient)
    print("Action: ", action_text)
    return HttpResponse(action_text)