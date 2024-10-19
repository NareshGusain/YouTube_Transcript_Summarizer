from django.shortcuts import render, redirect
from django.http import HttpResponse
from summarizeApp.PyFunctionsPyFunctions import applyRegex , linkTovideo


def index(request):
    if request.method == "POST":
        youtube_link = request.POST.get('youtube_link')
        link_id = applyRegex.extract_youtube_id(youtube_link)
        transcript = linkTovideo.generate_transcript(link_id)
        
        return render(request, 'index.html', {'transcript': transcript})
    return render(request, 'index.html')
