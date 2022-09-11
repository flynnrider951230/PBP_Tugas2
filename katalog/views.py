from django.shortcuts import render
from katalog.models import CatalogItem

# TODO: Create your views here.
def show_katalog(request):
    data_catalog_item = CatalogItem.objects.all()
    context = {
        'list_catalog': data_catalog_item, 
        'name': 'Shafa', 
        'student_id': '2106634534'  
        
}
    return render(request, 'katalog.html', context)