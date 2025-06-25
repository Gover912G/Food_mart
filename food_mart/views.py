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

def shop(request):
   return render(request, 'shop.html', {'nav' : 'shop'})

def singleProduct(request):
   return render(request, 'single_product.html', {'nav' : 'single-post'})

def cart(request):
   return render(request, 'cart.html', {'nav':'cart'})

def checkOut(request):
   return render(request, 'check_out.html', {'nav' : 'check-out'})

def blog(request):
   return render(request, 'blog.html', {'nav' : 'blog'})

def singlePost(request):
   return render(request, 'single_post.html', {'nav' : "single-post"})

def styles(request):
   return render(request, 'styles.html', {'nav ' : 'styles'})

def myaccount(request):
   return render(request, 'accounts.html', {'nav' : 'account'})
#thankyou