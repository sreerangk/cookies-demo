from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import reverse

# set cookies
# get cookies
# delete cookies

def login(request):
    if request.method == "GET":
        # getting cookies
        if 'logged_in' in request.COOKIES and 'username' in request.COOKIES:
            context = {
                'username':request.COOKIES['username'],
                'login_status':request.COOKIES.get('logged_in'),
            }
            return render(request, 'home.html', context)
        else:
            return render(request, 'login.html')

    if request.method == "POST":
        username=request.POST.get('email')
        context = {
                'username':username,
                'login_status':'TRUE',
            }
        response = render(request, 'home.html', context)

        # setting cookies
        response.set_cookie('username', username)
        response.set_cookie('logged_in', True)
        return response

def home(request):
    if 'logged_in' in request.COOKIES and 'username' in request.COOKIES:
            context = {
                'username':request.COOKIES['username'],
                'login_status':request.COOKIES.get('logged_in'),
            }
            return render(request, 'home.html', context)
    else:
        return render(request, 'home.html')


def logout(request):
    response = HttpResponseRedirect(reverse('login'))

    # deleting cookies
    response.delete_cookie('username')
    response.delete_cookie('logged_in')

    return response