from django.shortcuts import render


# Takes the users to the homepage
def index(request):
    return render(request, 'home/index.html')
