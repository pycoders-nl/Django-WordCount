from django.shortcuts import render

# Create your views here.

def anasayfa(request):
    return render(request,'anasayfa.html') 

def text(request):        
    
    return render(request, 'text.html')

def analiz(request):
    if request.method == 'POST':
        metin = request.POST['comment']

        metin=metin.split()
        sozluk={}
        sozluk1={}
        kelime_sayısı=len(metin)

        for i in metin:
            sozluk[i]=metin.count(i)
            metin.remove(i)
        
        ozgun_kelime = list(sozluk.values()).count(1)        
        n=sorted(list(set(sozluk.values())),reverse= True)
        
        k=i=0
        while i<2 and k<4:
            for j in sozluk.keys():
                if sozluk[j]==n[i]:
                    sozluk1[j]=n[i]
                    k+=1
            i+=1       

        context = {            
            'kelime_sayısı': kelime_sayısı,
            'ozgun_kelime': ozgun_kelime,
            'sozluk1': sozluk1,
        }

    return render(request, 'analiz.html', context)