from django.shortcuts import render
from mywatchlist.models import WatchlistItem
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def show_mywatchlist(request):
    data_mywatchlist = WatchlistItem.objects.all()
    context = {
        'list_mywatchlist': data_mywatchlist, 
        'Name': 'Shafa'
    }
    return render(request, 'mywatchlist.html', context)

def show_xml(request) :
    data = WatchlistItem.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = WatchlistItem.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_html(request):
    data = WatchlistItem.objects.all()
    return HttpResponse(serializers.serialize("html", data), content_type="application/html")

def show_json_by_id(request, id):
    data = WatchlistItem.objects.filter(pk=id)
    #Jika JSON
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = WatchlistItem.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")