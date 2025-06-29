from django.shortcuts import render, HttpResponse

# Create your views here.
def blogHome(request): 
    return render(request,'blogHome.html')

def blogPost(request, slug): 
    return render(request,'blogPost.html')