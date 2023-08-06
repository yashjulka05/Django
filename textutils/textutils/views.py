## this file is created by me, not made directly by django

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
   # return HttpResponse("we are in homepage")

def about(request):
    return HttpResponse("we are in /about")

#creating a pipeline

def analyze(request):
    djtext = request.POST.get('text', 'off')
    removepunc = request.POST.get('removepunc', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    UPPERCASE = request.POST.get('UPPERCASE', 'off')
    countcharacters = request.POST.get('countcharacters', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')

    analyzed = ""
    punct_list = '''.,?!:;'"()[]{}<>+-*/=&^%$#@~_`|§©®™£¥¢¬°'''
    if removepunc == 'on':
        for ch in djtext:
            if ch not in punct_list:
                analyzed = analyzed + ch

    elif newlineremover == 'on':
        for ch in djtext:
            if ch != '\n' and ch != '\r':
                analyzed = analyzed + ch

    elif UPPERCASE == 'on':
        for ch in djtext:
            analyzed = analyzed + ch.upper()

    elif extraspaceremover == 'on':
        for index, ch in enumerate(djtext):
            if not (index[djtext] == ' ' and index[djtext] + 1 == ' '):
                analyzed = analyzed + ch

    elif countcharacters == 'on':
        return HttpResponse(len(djtext))

    else:
        return HttpResponse("Error")

    params = {'purpose': 'Action is done', 'analyzed_text': {analyzed}}
    #return HttpResponse("we are in /analyze")
    return render(request, 'analyze.html', params)
