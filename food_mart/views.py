from django.shortcuts import render

# Create your views here.
def home(request):
   context = {'name': 'home'}
   return render(request, 'index.html', context)
