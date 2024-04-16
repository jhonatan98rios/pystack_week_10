from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from django.contrib.auth.models import User
from django.contrib.messages import constants, add_message
from django.contrib.auth import authenticate, logout

# Create your views here.
def cadastro(request: HttpRequest):

    print(request.META)
    if request.method == "GET":
        return render(request, 'cadastro.html')
    
    elif request.method == "POST":

        username = request.POST.get("username")
        email = request.POST.get("email")
        senha = request.POST.get("senha")
        confirmar_senha = request.POST.get("confirmar_senha")

        if senha != confirmar_senha:
            add_message(request, constants.ERROR, "A senha e a confirmação de senha devem iguais")
            return redirect("/usuarios/cadastro")
        
        if len(senha) < 6:
            add_message(request, constants.ERROR, "A senha deve yer mais de 6 digitos")
            return redirect("/usuarios/cadastro")
        
        users = User.objects.filter(username=username)

        if users.exists():
            add_message(request, constants.ERROR, "Já existe um usuário com esse username")
            return redirect("/usuarios/cadastro")

        User.objects.create_user(
            username=username,
            email=email,
            password=senha,
        )

        return redirect("/usuarios/login")
    

def login_view(request: HttpRequest):
    if request.method == "GET":
        return render(request, 'login.html')
    
    elif request.method == "POST":
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        user = authenticate(request, username, senha)

        if user:
            auth.login(request, user)
            return redirect('/pacientes/home')
        
        add_message(request, constants.ERROR, "usuário ou senha inválidos")
        return redirect('login')
    
    
def sair(request: HttpRequest):
    logout(request)
    return redirect('/usuario/login')