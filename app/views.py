from django.shortcuts import render



# Create your views here.
from app.forms import *
from django.http import HttpResponse
def insert_topic(request):
    d={'ETFO':TopicForm()}
    if request.method=='POST':
        TFDO=TopicForm(request.POST)
        if TFDO.is_valid():
            tn=TFDO.cleaned_data['topic_name']
            TO=Topic.objects.get_or_create(topic_name=tn)[0]
            TO.save()
            return HttpResponse('topic is created')
        else:
            return HttpResponse('not done')
    return render(request,'insert_topic.html',d)

def insert_webpage(request):
    EWFO=WebpageForm()
    d={'EWFO':EWFO}
    if request.method=='POST':
        WFDO=WebpageForm(request.POST)
        if WFDO.is_valid():
            TO=WFDO.cleaned_data['tn']
            na=WFDO.cleaned_data['na']
            em=WFDO.cleaned_data['em']
            u=WFDO.cleaned_data['u']
            #WO=webpage.objects.get_or_create(topic_name=TO,name=na,email=em,url=u)[0]
            #WO.save()
            return HttpResponse(str(WFDO.cleaned_data))
        else:
            return HttpResponse('invalid')
    return render(request,'insert_webpage.html',d)


