# I have create this file - Parth
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def ex2(request):
    # get the text
    djtext = request.GET.get('text_area', 'default')

    # check checkbox value
    removepunc = request.GET.get('removepunc', 'off')
    fullcaps = request.GET.get('fullcaps', 'off')
    newlineremover = request.GET.get('newlineremover', 'off')
    extraspaceremover = request.GET.get('extraspaceremover', 'off')
    charcounter = request.GET.get('charcounter', 'off')

    # check which checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyze = ""
        for chr in djtext:
            if chr not in punctuations:
                analyze = analyze + chr
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyze}
        djtext = analyze
    if fullcaps == "on":
        analyze = ""
        for char in djtext:
            analyze = analyze + char.upper()
        params = {'purpose': 'changed to uppercase', 'analyzed_text': analyze}
        djtext = analyze
    if newlineremover == "on":
        analyze = ""
        for char in djtext:
            if char != "\n" and char != '\r':
                analyze = analyze + char
            else:
                pass
        params = {'purpose': 'Remove New Lines', 'analyzed_text': analyze}
    if extraspaceremover == "on":
        analyze = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analyze = analyze + char
        params = {'purpose': 'Remove New Lines', 'analyzed_text': analyze}
        djtext = analyze
    if charcounter == "on":
        analyze = len(djtext)
        params = {'purpose': 'Remove New Lines', 'analyzed_text': analyze}

    if (removepunc != "on" and newlineremover != "on" and extraspaceremover != "on" and fullcaps != "on" and charcounter != "on"):
        return HttpResponse("please select any operation and try again")

    return render(request, 'analyze.html', params)
