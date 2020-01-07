from django.shortcuts import render
from movie.models import moviedb,category,trailer
import requests
from django.template.response import TemplateResponse
from django.http import HttpResponseRedirect
import json
# Create your views here.

def movie(request,pk):
    args = {}
    movieobj = moviedb.objects.filter(id=pk)
   
    if movieobj != None:
          
        # trailerdb = trailer.objects.filter(id=moviedb.trailer_id)
        # print(moviedb.trailer.id)
        return TemplateResponse(request, 'movie.html', args)
    else:
        return render(request, 'index.html')

def pay(request):

    if request.method == 'POST':
        # defining the api-endpoint  
        number = request.POST.get("number")
        API_ENDPOINT = "https://xpayy.herokuapp.com/payment/"
     
        data = {
            
            'contact': number,
            'amount':  '5555',
            'reference': "t025kk8sd",
            'api_key': '9njrbcqty9ew3cyx4s6k7jvtab134rr6',
            'public_key': '"MIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEAmptSWqV7cGUUJJhUBxsMLonux24u+FoTlrb+4Kgc6092JIszmI1QUoMohaDDXSVueXx6IXwYGsjjWY32HGXj1iQhkALXfObJ4DqXn5h6E8y5/xQYNAyd5bpN5Z8r892B6toGzZQVB7qtebH4apDjmvTi5FGZVjVYxalyyQkj4uQbbRQjgCkubSi45Xl4CGtLqZztsKssWz3mcKncgTnq3DHGYYEYiKq0xIj100LGbnvNz20Sgqmw/cH+Bua4GJsWYLEqf/h/yiMgiBbxFxsnwZl0im5vXDlwKPw+QnO2fscDhxZFAwV06bgG0oEoWm9FnjMsfvwm0rUNYFlZ+TOtCEhmhtFp+Tsx9jPCuOd5h2emGdSKD8A6jtwhNa7oQ8RtLEEqwAn44orENa1ibOkxMiiiFpmmJkwgZPOG/zMCjXIrrhDWTDUOZaPx/lEQoInJoE2i43VN/HTGCCw8dKQAwg0jsEXau5ixD0GUothqvuX3B9taoeoFAIvUPEq35YulprMM7ThdKodSHvhnwKG82dCsodRwY428kg2xM/UjiTENog4B6zzZfPhMxFlOSFX4MnrqkAS+8Jamhy1GgoHkEMrsT5+/ofjCx0HjKbT5NuA2V/lmzgJLl3jIERadLzuTYnKGWxVJcGLkWXlEPYLbiaKzbJb2sYxt+Kt5OxQqC1MCAwEAAQ==',
        }
        # sending post request and saving response as response object 
        r = requests.post(url = API_ENDPOINT, data = data) 
        
        print (number)
        # return HttpResponseRedirect('/thanks/')
        return render(request, 'index.html')

    else:
        return render(request, 'index.html')




    