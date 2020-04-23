from django.shortcuts import render
from dappx.forms import UserForm,UserProfileInfoForm,ProductFilter
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import Http404
from dappx.models import products,productcategories

# Create your views here. 

def index(request):
    return render(request,'dappx/index.html')
@login_required
def special(request):
    return HttpResponse("You are logged in !")
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'profile_pic' in request.FILES:
                print('found it')
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            registered = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    return render(request,'dappx/registration.html',
                        {'user_form':user_form,
                        'profile_form':profile_form,
                        'registered':registered})
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'dappx/login.html', {})


def index(request):
    category = productcategories.objects.all()
    product = products.objects.all()
    content = {'category':category, 'product':product,}
    # return render (request,'dappx/index.html',{'category': category})
    return render (request,'dappx/index.html',content
    )

def details(request,product_id):
    try:
        product = products.objects.get(pk=product_id)
    except products.DoesNotExist:
        raise Http404("Product does not exist")
    return render(request,'dappx/details.html',{'product':product})

def search(request):
    object_list = products.objects.filter()
    product_filter = ProductFilter(request.GET, queryset=object_list)
    return render(request, 'dappx/search_results.html', {'filter': product_filter})
