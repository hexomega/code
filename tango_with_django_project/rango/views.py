from django.http import HttpResponse

def index(request):
    return HttpResponse("About Page: <a href='/rango/about'>About</a>")

def about(request):
    return HttpResponse("Rango Says: Here is the about page. <a href='/rango/'>Index</a>")
