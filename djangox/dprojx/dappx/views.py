from django.shortcuts import render, redirect
from dappx.forms import UserForm,UserProfileInfoForm,UserChangeForm,EditProfileForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash#makes sure that the user is logged in even after redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import Http404
from dappx.models import products,productcategories,cartItem,orders,UserProfileInfo
from django.db.models import Q
from django.db import transaction
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.core.mail import send_mail
#import math
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
        #email = user_form.fields.email()
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
            email = request.POST.get('email')
            send_mail(
    'BringSUya Hoşgeldiniz',
    'Sitemize üye olduğunuz için teşekkürler. ',
    'EMAIL_HOST_USER ',
    [email],)
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






def listby(request, search_filter, filter_t, minimum_price, maximum_price):
    category = productcategories.objects.all()
    filter=search_filter #örn: süt. searchlediğin şey
    f = filter_t

    lookups= Q(name__contains=search_filter) | Q(brand__contains=search_filter) | Q(ShortDesc__contains=search_filter) | Q(LongDesc__contains=search_filter)
    results= products.objects.filter(lookups).distinct()
    print('results', results)
    categlookups = Q(CategoryID__CategoryName__contains=search_filter)
    categresults = products.objects.filter(categlookups).distinct()

    min_price = 0
    max_price = 0

    submitbutton = request.GET.get('submit')
 
    #at this step it may 
    #price is submitted from form by filling the boxes
    if minimum_price=="None" and minimum_price=="None":
        min_price = request.GET.get('minprice')
        max_price = request.GET.get('maxprice')
        submitbutton = request.GET.get('submit')
        #if min_price is None and max_price is None and submitbutton=="None":
        if min_price is None and max_price is None:
            
            #no price is entered but listby is wanted by the user
            if filter_t!="None":

                if filter_t=="increasing":
                    results= products.objects.filter(lookups).order_by('price').distinct()
                    categresults = products.objects.filter(categlookups).order_by('price').distinct()
    
                elif filter_t=="decreasing":
                    results= products.objects.filter(lookups).order_by('-price').distinct()
                    categresults = products.objects.filter(categlookups).order_by('-price').distinct()
                
                elif filter_t=="alphabetical":
                    results= products.objects.filter(lookups).order_by('name').distinct()
                    categresults = products.objects.filter(categlookups).order_by('name').distinct()
            
                elif filter_t=="nonalphabetical":
                    results= products.objects.filter(lookups).order_by('-name').distinct()
                    categresults = products.objects.filter(categlookups).order_by('-name').distinct()
                
            context= {'results': results, 'categresults':categresults, 'category':category, 'f':f, 'filter':filter}
            return render(request, 'dappx/listby_results.html', context)
       

        
    #prices are already provided, here we 
    #form is not used, user wanted  to list by
    elif minimum_price is not None and maximum_price is not None:
        print("minimum_price: ", type(minimum_price))
        min_price=float(minimum_price)
        max_price=float(maximum_price)
        
        results = products.objects.filter(lookups, price__range=(min_price, max_price)).distinct()
        categresults = products.objects.filter(categlookups, price__range=(min_price, max_price)).distinct()
        
    #############min, max values are set  until here


    if min_price==max_price:
        #context= {'results': results,  'category':category, 'categresults':categresults, 'submitbutton':submitbutton, 'filter':filter}    
        context = {'category':category}
        return render(request, 'dappx/search_results.html', context) ##will tell there is no result found
        
    else:
        #print("checkminimum price: ", min_price)
        #print("checkmaximum price: ", max_price)
        #print("filter type: ", filter_t)
        #print("price type: ", min_price)
        
        min_price = float(min_price)
        max_price = float(max_price)
        if filter_t=="increasing":
            results= products.objects.filter(lookups, price__range=(min_price, max_price)).order_by('price').distinct()
            categresults = products.objects.filter(categlookups, price__range=(min_price, max_price)).order_by('price').distinct()

        elif filter_t=="decreasing":
            results= products.objects.filter(lookups, price__range=(min_price, max_price)).order_by('-price').distinct()
            categresults = products.objects.filter(categlookups, price__range=(min_price, max_price)).order_by('-price').distinct()
        
        elif filter_t=="alphabetical":
            results= products.objects.filter(lookups, price__range=(min_price, max_price)).order_by('name').distinct()
            categresults = products.objects.filter(categlookups, price__range=(min_price, max_price)).order_by('name').distinct()
    
        elif filter_t=="nonalphabetical":
            results= products.objects.filter(lookups, price__range=(min_price, max_price)).order_by('-name').distinct()
            categresults = products.objects.filter(categlookups, price__range=(min_price, max_price)).order_by('-name').distinct()
        
        elif filter_t=="None":
            print("filterminimum price: ", min_price)
            print("filtermaximum price: ", max_price)
            print(type(f))
            results= products.objects.filter(lookups, price__range=(min_price, max_price)).distinct()
            categresults = products.objects.filter(categlookups, price__range=(min_price, max_price)).distinct()


        #'min_range': min_range, 'max_price':max_price
        context= {'results': results,  
        'category':category, 
        'filter': filter, 
        'categresults':categresults,
        'submitbutton':submitbutton,
        'min_price': min_price, 
        'max_price':max_price,
        'f':f}    
        return render(request, 'dappx/listby_results.html', context)
   
     



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
    category = productcategories.objects.all()
    product = products.objects.all()
    content= {'product':product,'category':category}

    submitbutton= request.GET.get('submit')
    
    if submitbutton is not None:
        print("submit ok")
        everyone = User.objects.all()
        for person in everyone:
            print(person.email)
            send_mail(
            'indirim',
            'SEÇİLİ ÜRÜNLERİMİZDE İNDİRİM BAŞLAMIŞTIR.BU FIRSATLARI KAÇIRMAYIN! ',
            'EMAIL_HOST_USER ',
           [person.email],)
        content= {'product':product,'category':category,'submitbutton': submitbutton}

    return render (request,'dappx/productmanager.html',content) 



@login_required
def cart(request, pr_id):  

    #if request.method == "POST":
    #    a = request.GET.get['amount']
    #    print ("amount: ", a)
    #else:
    #    print("could not get amount")
    #a = request.GET.get("drop_amount")
    #print("amount: ", a)

    category = productcategories.objects.all()  
    if request.method == 'GET':

        submitButton= request.GET.get('submit')
        current_user = request.user

        if pr_id is not -1:
            look=Q(id=pr_id)
            productsAdded= products.objects.filter(look)

            for p in productsAdded:
                #######
                preproduct = products.objects.get(id=pr_id)
                try:
                    preexisting_product= cartItem.objects.get(product=preproduct)
                    preexisting_product.itemquantity += 1
                    preexisting_product.totalCost = preexisting_product.itemquantity*preexisting_product.itemPrice
                    preexisting_product.save()

                except cartItem.DoesNotExist:
                    data = cartItem.objects.create(product=p, itemPrice=0,user=current_user, totalCost=0)
                    #print("data: ", data.user )
                    #print("type of data:",type(data))
                    #data.itemPrice = data.set_itemPrice()
                    data.itemPrice = p.changedprice
                    data.totalCost = p.changedprice
                    data.save()

            

            cartProducts = cartItem.objects.filter(user=current_user)
            if len(cartProducts) > 0:
                length = len(cartProducts)
                lastElement = cartItem.objects.create(itemPrice=0)
                #lastElement = cartProducts[length-1]
                for c in cartProducts:
                    lastElement.totalCost += c.itemPrice*c.itemquantity
                    
                context={'cartProducts': cartProducts,'lastElement':lastElement,'submitButton': submitButton, 'category':category}
            
            else:
                context={'cartProducts':cartProducts, 'submitButton': submitButton, 'category':category}
            
            return render(request, 'dappx/cart.html', context)
            # if len(cartProducts) > 0:
            #     length = len(cartProducts)
            #     lastElement = cartProducts[length-1]
            #     for c in cartProducts:
            #         lastElement.totalCost += c.itemPrice
            
            # context={'cartProducts': cartProducts, 'lastElement':lastElement, 'submitButton': submitButton}
            
            # return render(request, 'dappx/cart.html', context)
        
        else:
            return render(request, 'dappx/cart.html')

    else:
        return render(request, 'dappx/cart.html')



def remove_item(request, pr_id):
    current_user = request.user
    category = productcategories.objects.all()  
    if request.method == 'GET':
        submitButton= request.GET.get('submit')
        productDelete = cartItem.objects.get(itemID = pr_id)
        productDelete.delete()

        cartProducts = cartItem.objects.filter(user=current_user)
        if len(cartProducts) > 0:
            length = len(cartProducts)
            lastElement = cartItem.objects.create(itemPrice=0)
            #lastElement = cartProducts[length-1]
            for c in cartProducts:
                lastElement.totalCost += c.itemPrice*c.itemquantity
            
            context={'cartProducts': cartProducts,'lastElement':lastElement,'submitButton': submitButton, 'category':category}
        
        else:
            context={'cartProducts':cartProducts, 'submitButton': submitButton, 'category':category}
        
        return render(request, 'dappx/cart.html', context)
    
    else:
        return render(request, 'dappx/cart.html')


def checkout(request):
    current_user = request.user
    category = productcategories.objects.all() 
    order = orders.objects.create()
    
    checkout=cartItem.objects.filter(user=current_user)

    cartProducts = cartItem.objects.filter(user=current_user)
    print("cartProducts:", len(cartProducts))
    if len(cartProducts) > 0:
        length = len(cartProducts)
        lastElement = cartItem.objects.create(itemPrice=0)
        #lastElement = cartProducts[length-1]
        for c in cartProducts:
            lastElement.totalCost += c.itemPrice*c.itemquantity
        context={'checkout':checkout, 'order':order, 'category':category, 'lastElement':lastElement}
    else:
        context={'checkout':checkout, 'order':order, 'category':category}
    return render(request, 'dappx/invoice.html', context)





def checkout_complete(request):
    current_user = request.user
    category = productcategories.objects.all() 
    checkout=cartItem.objects.filter(user=current_user)
    
    ############
    for c in checkout:
        #orders.details.add(c)
        print("itemPrice of c:",c.itemPrice)
        print("item user: ", c.user.username)
    #print("checkout items: ",checkout)

    #orders.details.add(checkout)
    
    for cc in checkout:
        order = orders.objects.all()
    
    #######################
    
    for c in checkout:
        a = c.itemquantity
        c.product.stock = a - 1
        c.product.save()
    
    
    user_mail = current_user.email

    #message = [c for c in checkout=cartItem.objects.all()]
    send_mail(
    'Alışverişiniz',
    'Alışverişiniz tamamlanmıştır. Teşekkürler. ',
    'EMAIL_HOST_USER ',
    [user_mail],)
    cartItem.objects.all().delete()
    category = productcategories.objects.all()
    product = products.objects.all()
    content = {'category':category, 'product':product, 'category':category}
    return render (request,'dappx/index.html',content)


def view_orders(request):
    category = productcategories.objects.all()
    current_user = request.user
    #orderlookups = Q(details__user__username=current_user)
    print("hello orderss")
    print('current_user: ', current_user)
    #myorders = orders.objects.filter(details__user__username=current_user).distinct()
    myorders = orders.objects.all()
    print('myorders', myorders)
    context =  {'category':category,'myorders':myorders}

    
    return render(request,'dappx/orders.html', context)


def profile(request):
    category = productcategories.objects.all()
    context={'category':category, 'user': request.user}

    return render(request,'dappx/profile.html', context)


@login_required
def edit_profile(request):
    category = productcategories.objects.all()
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        profile_form = UserProfileInfoForm(request.POST, instance=request.user.userprofileinfo)

        if form.is_valid() and profile_form.is_valid():
            form.save()
            profile_form.save()
            return redirect('/profile')
    else:
        form = EditProfileForm(instance=request.user)
        profile_form = UserProfileInfoForm(instance=request.user.userprofileinfo)      
        #args = {'form': form, 'profile_form': profile_form, 'category': category }
    return render(request,'dappx/edit_profile.html',{'form': form, 'profile_form': profile_form, 'category': category })

@login_required
def change_password(request):
    category = productcategories.objects.all()
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('/profile')
        else:
            #messages.success(request, 'Form submission unsuccessful')
            return HttpResponse("Please pay attention to password changing rules and try again")
            #return redirect('/change-password')
    else:
        form = PasswordChangeForm(user=request.user)
        args = {'form': form, 'category': category }
        return render(request,'dappx/change_password.html',args)

        
def account(request):
    category = productcategories.objects.all()
    context={'category':category, 'user': request.user}

    return render(request,'dappx/account.html', context)

