from django.shortcuts import render

# Create your views here.
def home(request):
   context = {
      "name": "home"
      }
   return render(request, 'index.html', context)


def contact(request):
   return render(request, 'contact.html', {'nav' : 'contact'})

def about(request):
   return render(request, 'about.html', {'nav' : 'about'})