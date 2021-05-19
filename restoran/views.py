from django.shortcuts import render
from kasir.models import Makanan, Minuman
# Create your views on here

def index(request):
    makanan = Makanan.objects.all()
    minuman = Minuman.objects.all()
    # a = (minuman[3])
    # print(a.imageMinuman)
    context = {
        'judul':'Home',
        'nav': [
            ['/','Home'],
        ],
        'menuMakanan': makanan,
        'menuMinuman': minuman
    
    }
    return render(request,'index.html', context)