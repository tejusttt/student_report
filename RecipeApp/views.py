from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='/login/')
def recipes(request):
    if request.method == "POST":
        data= request.POST        
        recipe_name = data.get("recipe_name")
        recipe_desc= data.get("recipe_desc")
        recipe_image = request.FILES.get("recipe_image")
        
        Recipe.objects.create(
            recipe_name = recipe_name,
            recipe_desc = recipe_desc,
            recipe_image = recipe_image
        )
        return redirect('/recipes/')
    
    queryset = Recipe.objects.all()
    
    if request.GET.get("search"):
        queryset = queryset.filter( recipe_name__icontains = request.GET.get("search") )
    
    context = {'recipes': queryset}
        
    return render(request, 'recipes.html', context)

@login_required(login_url='/login/')
def delete_recipe(request, id):
    queryset=Recipe.objects.get(id=id)
    queryset.delete()
    
    return redirect('/recipes/')

@login_required(login_url='/login/')
def update_recipe(request, id):
    queryset=Recipe.objects.get(id=id)
    
    if request.method == "POST":
        data= request.POST        
        recipe_name = data.get("recipe_name")
        recipe_desc= data.get("recipe_desc")
        recipe_image = request.FILES.get("recipe_image")
        
        queryset.recipe_name = recipe_name
        queryset.recipe_desc = recipe_desc
        
        if recipe_image :
            queryset.recipe_image = recipe_image
            
        queryset.save()
        return redirect('/recipes/')
        
    
    context = {"recipe":queryset}
    
    return render(request, 'update_recipe.html', context)

def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if not User.objects.filter(username=username).exists():
            messages.error(request,"invalid email")
            return redirect('/login/')
        
        user = authenticate(request, username=username ,password = password)
    
        if user is None:
            messages.error(request, "invalid credentials")
            return redirect('/login/')
        else:
            login(request,user)
            return redirect('//')
    return render(request, 'login.html')
    
def logout_page(request):
    logout(request)
    return redirect('/login/')

def register(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        user = User.objects.filter(username= username).first()
        email_user = User.objects.filter(email=email).first()
        
        if user:
            messages.info(request, "usermame already exits")
            return redirect('/')
        if email_user:
            messages.info(request, "email already exits")
            return redirect('//')
                
        user = User.objects.create(
            first_name = first_name,
            last_name = last_name,
            username = username,
            email = email,
        )
        user.set_password(password)
        user.save()
        messages.success(request, "Account created successfully")
        
    return render(request, 'register.html')