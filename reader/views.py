from django.shortcuts import render
from django.shortcuts import HttpResponse
import feedparser

def index(request):
    if request.method == 'POST':
        url = request.POST.get('url')
        parsed = feedparser.parse(url)
        feed = parsed['feed']
        all_entries = parsed['entries']
        entries = []
        for entry in all_entries:
            if 'media_thumbnail' in entry.keys():
                entries.append({
                    'link' : entry['link'],
                    'title' : entry['title'],
                    'description' : entry['description'],
                    'published' : entry['published'],
                    'media_thumbnail' : entry['media_thumbnail'][0]['url'],
                })
            else:
                entries.append({
                    'link' : entry['link'],
                    'title' : entry['title'],
                    'description' : entry['description'],
                    'published' : entry['published'],
                })

        error_msg = "Oops! Please check if you have entered a valid Feed URL"
        return render(request, 'index.html', {'entries':entries,'feed':feed, 'error_msg':error_msg})
    else:
        return render(request, 'index.html')
