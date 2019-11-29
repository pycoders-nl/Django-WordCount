from django.shortcuts import render
from .models import Kelime
# Create your views here.
def index(request):
    

    return render(request,"index.html")
    
def sonuc(request):
    kelime=Kelime.objects.all()
    if request.method =="POST":
                        
        text=request.POST['text']
        kaydet=Kelime(metin_text=text)
        kaydet.save()
        text=text.split()
        kelime_sayisi=str(len(text))
        maxi={}
        ozgun=[]
        for i in text:
            ozgun+=[i]

            maxi[text.count(i)]=i
        tekrar_kelime_sayisi=max(maxi.keys())
        tekrar_kelime=maxi[tekrar_kelime_sayisi]
        tekrar_kelime=str(tekrar_kelime)
        print(len(ozgun))
        ozgun=list(set(ozgun))
        ozgun_sayi=len(ozgun)
        print(ozgun_sayi)
        context={'kelime_sayisi':kelime_sayisi,
                'tekrar_kelime':tekrar_kelime,
                'tekrar_kelime_sayisi':tekrar_kelime_sayisi,
                'ozgun_sayi':ozgun_sayi,
                }
        

        print(kelime_sayisi,tekrar_kelime,tekrar_kelime_sayisi)
        
    return render(request,"sonuc.html",context)
