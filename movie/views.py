from django.shortcuts import render
from movie.models import moviedb,category,trailer
from django.template.response import TemplateResponse
from django.http import HttpResponseRedirect

# Create your views here.

def movie(request,pk):
    args = {}
    movieobj = moviedb.objects.filter(id=pk)
   
    if movieobj != None:
          
        trailerdb = trailer.objects.filter(title=moviedb.trailer)
        
        print(trailerdb)
        return TemplateResponse(request, 'movie.html', args)
    else:
        return render(request, 'index.html')

def pay(request):

    if request.method == 'POST':
        number = request.POST.get("number")
        print (number)
        # return HttpResponseRedirect('/thanks/')
        return render(request, 'index.html')

    else:
        return render(request, 'index.html')




    