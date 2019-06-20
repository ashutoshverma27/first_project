from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    return render(request,'home.html',{'hithere':'this is me best programmer'})

def count(request):
    fulltext=request.GET['fulltext']
    words=fulltext.split()
    length=len(words)
    countword=dict()

    for word in words:
        if word in countword:
            countword[word]+=1
        else:
            countword[word]=1
    newword=[]
    for i,j in zip(countword.keys(),countword.values()):
        newword.append((i,j))
    print(newword)
    newword.sort(key=lambda x:x[1],reverse=True)
    return render(request,'count.html',{'fulltext':fulltext,'length':length,'newword':newword})
