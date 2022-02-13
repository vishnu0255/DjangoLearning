from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import AccessRecords,Topic,Webpage

# Create your views here.
def index(request):
    return HttpResponse("hello world!!!!!!")

def help(request):
    topics = Topic.objects.all()
    topics_list = {'all_topics':topics}
    return render(request,'first_app/help.html',context=topics_list)
