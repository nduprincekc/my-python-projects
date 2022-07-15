from django.shortcuts import render
from gnewsclient import gnewsclient
# Create your views here.
import requests


def scrap(b):
    client = gnewsclient.NewsClient(language='english', location='Ghana', topic=b, use_opengraph=True,
                                    max_results=20)
    news = client.get_news()
    l = []
    for i in news:
        if i['url'] != None and i['title'] != None and i['description'] != None and i['image'] != None:
            l.append(i)
    if len(l) > 9:
        return l
    else:
        for i in news:
            if i['url'] == None:
                i['url'] = "https//news.google.com/topstories?h1=en-GH&gl=GH&ceid=GH:en"
            if i['title'] == None:
                i['title'] = 'Latest News'
            if i['description'] == None:
                i['description'] = 'Latest News'
            if i['image'] == None:
                i['image'] = 'https://images-eu.ssl-images-amazon.com/images/I/911HWG8HUNL.png'
        return news

def index(req):
    news=scrap("World")
    return render(req, 'index.html', {'news':news})

def add1(req):
    if req.POST.get(" "):
        news=scrap(' ')
    else:
        news=scrap('World')
        return render(req, 'index1.html', {'news':news})#renders the world news on the index1.html
def add2(req):
    if req.POST.get(" "):
        news=scrap(' ')
    else:
        news=scrap('Nation')
        return render(req, 'index1.html', {'news':news})#renders the nation news on the index1.html
def add3(req):
    if req.POST.get(" "):
        news=scrap(' ')
    else:
        news=scrap('Business')
        return render(req, 'index1.html', {'news':news})#renders the business news on the index1.html
def add4(req):
    if req.POST.get(" "):
        news=scrap(' ')
    else:
        news=scrap('Technology')
        return render(req, 'index1.html', {'news':news})#renders the tech news on the index1.html
def add5(req):
    if req.POST.get(" "):
        news=scrap(' ')
    else:
        news=scrap('Entertainment')
        return render(req, 'index1.html', {'news':news})#renders the Entertainment news on the index1.html
def add6(req):
    if req.POST.get(" "):
        news=scrap(' ')
    else:
        news=scrap('Sports')
        return render(req, 'index1.html', {'news':news})#renders the Sports news on the index1.html
def add7(req):
    if req.POST.get(" "):
        news=scrap(' ')
    else:
        news=scrap('Science')
        return render(req, 'index1.html', {'news':news})#renders the Science news on the index1.html
def add8(req):
    if req.POST.get(" "):
        news=scrap(' ')
    else:
        news=scrap('Health')
        return render(req, 'index1.html', {'news':news})#renders the Health news on the index1.html