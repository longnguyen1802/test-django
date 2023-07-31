import json
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.views.decorators.csrf import csrf_exempt
cookie_map = {}

# Sample users (replace this with your user database)
users = [
    {
        'username': 'user1',
        'password': 'password1'
    },
    {
        'username': 'user2',
        'password': 'password2'
    }
    # Add more users here
]

@csrf_exempt
def login(request):
    print("Get some request")
    return render(request, 'login.html')

@csrf_exempt
def apilogin(request):
    data = request.body.decode('utf-8')  # Decode the request body from bytes to a string
    data = json.loads(data)  # Parse the JSON data
    username = data.get('username')
    password = data.get('password')
    print(username,password)
    user = next((user for user in users if user['username'] == username), None)

    if not user or user['password'] != password:
        return HttpResponse('Invalid credentials.', status=401)

    request.session['user'] = {'username': user['username']}
    #print(request.META)
    return HttpResponse()

@csrf_exempt
def authenticate(request):
    username = request.POST.get('username')
    password = request.POST.get('password')

    user = next((user for user in users if user['username'] == username), None)

    if not user or user['password'] != password:
        return HttpResponse('Invalid credentials.', status=401)

    request.session['user'] = {'username': user['username']}
    #cookie_map[username] = request.headers['Cookie']
    return HttpResponseRedirect('/')

@csrf_exempt
def dashboard(request):
    user = request.session.get('user')
    if not user:
        return redirect('login')
        
    response = render(request, 'dashboard.html')
    response.set_cookie('testSomeCookie', 'cookieTest', max_age=3600, httponly=True)
    return response

def logout(request):
    request.session.clear()
    return HttpResponse('Logged out successfully.')