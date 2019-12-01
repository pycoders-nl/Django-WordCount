from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def count(request):
    my_text = (request.POST['mytext']).lower()
    my_text_list = my_text.split()
    number_of_words = len(my_text_list)

    each_word = {}

    for word in my_text_list:
        if word in each_word:
            each_word[word] +=1
        else:
            each_word[word] = 1
   
    sorted_text = sorted(each_word.items(), key=lambda x:x[1], reverse=True)
    sorted_text_dictionary = dict(sorted_text)
    return render(request, 'count.html', {'text':my_text, 'totalwords':number_of_words, 'eachword':sorted_text_dictionary.items})