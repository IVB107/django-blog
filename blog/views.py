from django.http import HttpResponse

def homePage(request):
  return HttpResponse('home')

def aboutPage(request):
  return HttpResponse('about')
