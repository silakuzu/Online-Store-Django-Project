from django.shortcuts import render
from dappx.forms import UserForm,UserProfileInfoForm,ProductFilter
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import Http404
from dappx.models import products,productcategories,cartItem,cartTable,orders
from django.db.models import Q

#import requests




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
    category = productcategories.objects.all()
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
                        'registered':registered,
                        'category': category})
def user_login(request):
    category = productcategories.objects.all()
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                if (username == 'salesmanager' and password == 'deneme12'):
                    return HttpResponseRedirect(reverse('salesmanager'))
                elif (username == 'productmanager' and password == 'deneme') :
                    return HttpResponseRedirect(reverse('productmanager'))
                else:  
                    return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'dappx/login.html', {'category': category})


def index(request):
    category = productcategories.objects.all()
    product = products.objects.all()
    content = {'category':category, 'product':product}
    # return render (request,'dappx/index.html',{'category': category})
    return render (request,'dappx/index.html',content)



def search(request):
    #if request.method == 'GET':
        query= request.GET.get('q')
        submitbutton= request.GET.get('submit')
        category = productcategories.objects.all()
        if query is not None:
            lookups= Q(name__contains=query) | Q(brand__contains=query) | Q(ShortDesc__contains=query) | Q(LongDesc__contains=query)
            results= products.objects.filter(lookups).distinct()

            categlookups = Q(CategoryID__CategoryName__contains=query)
            categresults = products.objects.filter(categlookups).distinct()
            context={'results': results,
                    'submitbutton': submitbutton,
                    'category': category,
                    'categresults': categresults}

            return render(request, 'dappx/search_results.html', context)
        else:
            return render(request, 'dappx/search_results.html', {'category': category} )
    #else:
     #   return render(request, 'dappx/search_results.html')



def category(request, category_name):
    results= products.objects.filter(CategoryID__CategoryName=category_name).distinct()
    specificCateg = productcategories.objects.all().filter(CategoryName=category_name).distinct()
    category = productcategories.objects.all()
    context= {'results': results, 'specificCateg': specificCateg, 'category':category}    
    return render(request, 'dappx/category_results.html', context)

def increasing(request, increasing_filter):
    category = productcategories.objects.all()

    lookups= Q(name__contains=increasing_filter) | Q(brand__contains=increasing_filter) | Q(ShortDesc__contains=increasing_filter) | Q(LongDesc__contains=increasing_filter)
    results= products.objects.filter(lookups).order_by('price').distinct()
    categlookups = Q(CategoryID__CategoryName__contains=increasing_filter)
    categresults = products.objects.filter(categlookups).order_by('price').distinct()
    category = productcategories.objects.all()

    filter = increasing_filter
    context={'results': results,
            'category': category,
            'categresults': categresults,
            'filter': filter}
    return render(request, 'dappx/increasing_results.html', context)


def decreasing(request, decreasing_filter):
    category = productcategories.objects.all()
    lookups= Q(name__contains=decreasing_filter) | Q(brand__contains=decreasing_filter) | Q(ShortDesc__contains=decreasing_filter) | Q(LongDesc__contains=decreasing_filter)
    results= products.objects.filter(lookups).order_by('-price').distinct()
    categlookups = Q(CategoryID__CategoryName__contains=decreasing_filter)
    categresults = products.objects.filter(categlookups).order_by('-price').distinct()
    category = productcategories.objects.all()

    filter = decreasing_filter
    context={'results': results,
            'category': category,
            'categresults': categresults,
            'filter': filter}
    return render(request, 'dappx/decreasing_results.html', context)    

def ascending(request, ascending_filter):
    category = productcategories.objects.all()
    lookups= Q(name__contains=ascending_filter) | Q(brand__contains=ascending_filter) | Q(ShortDesc__contains=ascending_filter) | Q(LongDesc__contains=ascending_filter)
    results= products.objects.filter(lookups).order_by('name').distinct()
    categlookups = Q(CategoryID__CategoryName__contains=ascending_filter)
    categresults = products.objects.filter(categlookups).order_by('name').distinct()
    category = productcategories.objects.all()

    filter = ascending_filter
    context={'results': results,
            'category': category,
            'categresults': categresults,
            'filter': filter}
    return render(request, 'dappx/ascending_results.html', context)  

def descending(request, descending_filter):
    category = productcategories.objects.all()
    lookups= Q(name__contains=descending_filter) | Q(brand__contains=descending_filter) | Q(ShortDesc__contains=descending_filter) | Q(LongDesc__contains=descending_filter)
    results= products.objects.filter(lookups).order_by('-name').distinct()
    categlookups = Q(CategoryID__CategoryName__contains=descending_filter)
    categresults = products.objects.filter(categlookups).order_by('-name').distinct()
    category = productcategories.objects.all()

    filter = descending_filter
    context={'results': results,
            'category': category,
            'categresults': categresults,
            'filter': filter}
    return render(request, 'dappx/descending_results.html', context)  



def details(request,product_id):
    category = productcategories.objects.all()
    try:
        product = products.objects.get(pk=product_id)
        #product = products.objects.all().filter.(id=product_id)
    except products.DoesNotExist:
        raise Http404("Product does not exist")
    return render(request,'dappx/details.html',{'product':product, 'category': category})
    

def salesmanager(request):
    category = productcategories.objects.all()
    product = products.objects.all()
    content = {'category':category, 'product':product}
    # return render (request,'dappx/index.html',{'category': category})
    return render (request,'dappx/salesmanager.html',content)

def productmanager(request):
    #category = productcategories.objects.all()
    product = products.objects.all()
    content= {'product':product}
    # return render (request,'dappx/index.html',{'category': category})
    
    
    return render (request,'dappx/productmanager.html',content) 

def cart(request, pr_id=None):
    if request.method == 'GET':

        submitButton= request.GET.get('submit')

        if id is not None:
            look=Q(id=pr_id)
            productsAdded= products.objects.filter(look).distinct()


            context={'productsAdded': productsAdded,
                    'submitButton': submitButton}
            
            return render(request, 'dappx/cart.html', context)
        
        else:
            return render(request, 'dappx/cart.html')

    else:
        return render(request, 'dappx/cart.html')
