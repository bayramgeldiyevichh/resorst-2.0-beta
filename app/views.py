from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib import messages
from django.db.models import Q
from .forms import*
from .models import *

def index(request):
    category = Category.objects.all()
    banner = Banner.objects.all()
    restoran = Restoran.objects.filter(is_vip=True)
    context = {
        'restoran': restoran,
        'banner': banner,
        'category': category,
    }

    return render(request, 'index.html', context)



# Sign up
def sign_up(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("sign_in")
    return render(request, 'sign_up.html', {'form': form})



# Sign in
def sign_in(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            if hasattr(user, 'profile'):
                return redirect('profile_page')
            else:
                return redirect('/')
        else:
            messages.info(
                request, 'something went wrong, check username or password...!')
    context = {}
    return render(request, 'sign_in.html', context)


#Logout
def logout_page(request):
    logout(request)
    return redirect('/')


# profile_register
def profile_register(request):
    profile_form = ProfileForm()
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, request.FILES)
        print(profile_form)
        if profile_form.is_valid():
            profile_form.save()
            return redirect('profile_page')
    return render(request, 'profile_register.html', {'form': profile_form})



# profile page
def profile_page(request):
    profile = Profile.objects.get(user=request.user.id)
    return render(request, 'profile_page.html', {'profile': profile})




# profile setting
def profile_setting(request):
    profile = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile_page')
    return render(request, 'profile_register.html', {'form': ProfileForm(instance=profile)})



# create restoran
def create_restoran(request):
    create_restoran = RestoranForm()
    if request.method == 'POST':
        create_restoran = RestoranForm(request.POST, request.FILES)
        if create_restoran.is_valid():
            create_restoran.save()
            return redirect('index')
    return render(request, 'create_restoran.html', {'form': create_restoran})



# my restoran
def my_restoran(request):
    search = request.GET.get('search', '')
    my_restoran = Restoran.objects.get(user=request.user.id)
    if search:
        food = Food.objects.filter(Q(name__icontains=search))
    else:
        food = Food.objects.filter(restoran = my_restoran)
    
    return render(request, 'my_restoran.html', {'my_restoran': my_restoran, 'food': food})



# my_restoran_edit
def my_restoran_edit(request):
    my_restoran = Restoran.objects.get(user=request.user)
    if request.method == 'POST':
        form = RestoranForm(request.POST, request.FILES, instance=my_restoran)
        if form.is_valid():
            form.save()
            return redirect('my_restoran')
    return render(request, 'create_restoran.html', {'form': RestoranForm(instance=my_restoran)})


# create food
def create_food(request):
    create_food = CreateFoodForm()
    if request.method == 'POST':
        create_food = CreateFoodForm(request.POST, request.FILES)
        if create_food.is_valid():
            create_food.save()
            return redirect('my_restoran')
    return render(request, 'create_food.html', {'form': create_food})



# food page
def food_page(request, id):
    food_page = Food.objects.filter(id=id)
    return render(request, 'food_page.html', {'food_page': food_page})



#delete food
def delete_food(request,id):
    food = Food.objects.get(id=id)
    food.delete()
    return redirect('my_restoran')



#edit food
def edit_food(request, pk):
    edit_food = Food.objects.get(id=pk)
    if request.method == 'POST':
        edit_food = CreateFoodForm(request.POST, request.FILES, instance=edit_food)
        if edit_food.is_valid():
            edit_food.save()
            return redirect('my_restoran')
    return render(request, 'create_food.html', {'form': CreateFoodForm(instance=edit_food)})


#restoran page
def restoran_page(request, id):
    restoran_page = Restoran.objects.get(id=id)
    food = Food.objects.filter(restoran=restoran_page)
    return render(request, 'restoran_page.html', {'restoran_page': restoran_page, 'food': food})


#food
def food(request, id):
    foods = Food.objects.get(id=id)
    return render (request, 'food.html', {'foods': foods})



    

