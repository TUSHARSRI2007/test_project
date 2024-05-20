from django.shortcuts import render
from django.http import HttpResponse
from .forms import PasswordForm
import bcrypt

# Create your views here.
def home(request):
    password = bytes(request.POST.get('password'), 'utf-8')
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password, salt)
    hash_password = hashed_password.decode('utf-8')
    print(hash_password)
    
    return render(request, 'home.html', {'password': hash_password})