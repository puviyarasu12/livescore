# cricket_scores/views.py

from django.shortcuts import render
import requests
import xml.etree.ElementTree as ET

def home(request):
    return render(request, 'cricket_scores/home.html')

def live_matches(request):
    url = 'http://static.cricinfo.com/rss/livescores.xml'
    response = requests.get(url)
    root = ET.fromstring(response.content)
    matches = []

    for item in root.findall('./channel/item'):
        match = item.find('title').text
        matches.append(match)

    return render(request, 'cricket_scores/live_matches.html', {'matches': matches})
