from django.shortcuts import render, redirect
from django.template import loader
from .models import Name, Text
from django.utils.datastructures import MultiValueDictKeyError
from django.http import Http404


# Create your views here.
def index(request):

    # context = {
    #     "words": Name.objects.all()                  # database models.py deki class ismi Todo oldugu icin bu sekilde yazdik
    # }
    return render(request, 'index.html')


def page_details(request):
    # context = {
    #     "word": Name.objects.get(id=textId)
    # }
    return render(request, "page_details.html")


def textAdd(request):
    return render(request, "textAdd.html")        # sadece sayfayi yazdiriyor


def page_show(request):
    if request.method == "POST":
        text = request.POST['message']                  # veriyi yollama kontrolu. Message kismina ne yazdiysak burada gorunsun
        
        if text == "":
            context={'word_count':"EMPTY",
                'repeat_word':"EMPTY",
                'repeat_wcount':"EMPTY",
                'ozgun_sayi':"EMPTY",
                }
            return render(request, "page_show.html", context)

        else:
            text=text.split()
            wcount=str(len(text))
            maxi={}
            ozgun=[]
            for i in text:
                ozgun+=[i]
                maxi[text.count(i)]=i
            repeat_wcount=max(maxi.keys())
            repeat_word=maxi[repeat_wcount]
            repeat_word=str(repeat_word)

            #print(len(ozgun))
            ozgun=list(set(ozgun))
            ozgun_sayi=len(ozgun)
            #print(ozgun_sayi)
            context={'word_count':wcount,
                    'repeat_word':repeat_word,
                    'repeat_wcount':repeat_wcount,
                    'ozgun_sayi':ozgun_sayi,
                    }


            print(wcount, repeat_word, repeat_wcount)
            return render(request, "page_show.html", context)   
        return render(request, "page_show.html")



