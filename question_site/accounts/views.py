from django.shortcuts import render
from django.http import HttpResponseRedirect
from accounts.custom_form.registration_form import UserCreateForm
from django.contrib.auth import logout

def login_page(request):
    return render(request, 'registration/login.html')

def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')

# User Registration
def register(request):
    if request.method == 'POST':
        print(request.POST)
        form = UserCreateForm(request.POST)
        print(request.POST)

        if form.is_valid():
            print(form)
            new_user = form.save()
            return HttpResponseRedirect('/')
    else:
        form = UserCreateForm()

    return render(
        request,
        "registration/register.html",
        {'form': form}
    )
