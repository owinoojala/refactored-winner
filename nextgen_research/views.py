from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'nextgen/index.html')
def subjects(request):
    context = {'page_title':'Subjects'}
    return render(request, 'nextgen/page.html', context)
