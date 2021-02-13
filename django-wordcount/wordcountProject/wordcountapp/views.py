from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def result(request):
    text = request.GET['fulltext']
    words = text.split()
    word_dic = {}

    for w in words:
        if w in word_dic:
            word_dic[w]+=1
        else:
            word_dic[w]=1

    return render(request, 'result.html', {'full': text, 'totalwords': len(words), 'dic': word_dic.items()})
    #items() -> (단어 : 몇 번), ...