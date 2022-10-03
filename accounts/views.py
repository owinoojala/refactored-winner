from django.shortcuts import render, redirect

# Create your views here.
def signup(request):
    return render(request, 'accounts/signup.html')
def signin(request):
    return redirect(writer)
    #return render(request, 'accounts/signin.html')
def writer(request):
    return render(request, 'accounts/writer.html')
