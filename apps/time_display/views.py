from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime, strptime, localtime

def index(request):
    context = {
        "time": strftime('%b %d %Y %I:%M%p', localtime())
        
        #("%Y-%m-%d %H:%M %p", gmtime())
    }
    return render(request, 'time_display/index.html', context)