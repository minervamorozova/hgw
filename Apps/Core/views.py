from django.shortcuts import render, redirect
from .models import Users
from django.contrib import messages
# Create your views here.

def home(request):
    users = Users.objects.all()
    messages.success(request,'Usuarios Listados')
    return render(request, 'core.html', {"Users": users})

def registerUser(request):
    id = request.POST['txtID']
    wallet = request.POST['txtWallet']
    coin = request.POST['txtCoin']

    user = Users.objects.create(idUser=id, idWallet=wallet, coinInGame=coin)
    messages.success(request,'Usuario creado')
    return redirect('/')

def editionUser(request, idUser):
    user = Users.objects.get(idUser=idUser)    
    return render(request, 'editionUser.html', {"user":user})

def editUser(request):
    id = request.POST['txtID']
    wallet = request.POST['txtWallet']
    coin = request.POST['txtCoin']

    user = Users.objects.get(idUser=id)
    user.idUser = id
    user.idWallet = wallet
    user.coinInGame = coin
    user.save()
    messages.success(request,'Usuario Editado')
    return redirect('/')

def deleteUser(request, idUser):
    user = Users.objects.get(idUser=idUser)
    user.delete()
    messages.success(request,'Usuario Eliminado')
    return redirect('/')