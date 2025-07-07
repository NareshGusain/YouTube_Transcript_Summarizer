from django.shortcuts import render, redirect
from django.http import HttpResponse
from summarizeApp.PyFunctions import helper


def index(request):
    if request.method == "POST":
        youtube_link = request.POST.get('youtube_link')
        link_id = helper.extract_youtube_id(youtube_link)
        print(f"Extracted video ID: {link_id}")
        transcript, word_count = helper.generate_transcript(link_id)
        cleaned_transcript = helper.clean_transcript(transcript)
        return render(request, 'index.html', {'transcript': cleaned_transcript})
    return render(request, 'index.html')
