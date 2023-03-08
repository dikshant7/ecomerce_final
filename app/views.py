from functools import cache
from django.shortcuts import render
from .models import product, user_detail , order
from django.contrib.auth.models import User,auth
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages
def home(request):
    # print(5)
    products=product.objects.all()
    # print(size(products))
    return render(request, 'app/home.html',{'products':products})

def product_detail(request):
 product_id = request.GET.get('query_name')
 i = product.objects.get(id=product_id)
 return render(request, 'app/productdetail.html',{'i':i})

def add_to_cart(request):
    if not request.user.is_authenticated:
        return redirect('/login')
    current_user = request.user
    user_email = current_user.email
    # if not user_detail.objects.filter(user_email=user_email).exists():
    #     messages.info(request,'please complete the profile first')
    #     return redirect('/profile')
    product_id = request.GET.get('query_name')
    # i = product.objects.get(id=product_id) 
    i = user_detail.objects.get(user_email=user_email)
    # i.order={'5':'6'}
    temp=False
    if product_id:
            for j in i.order:
                if j==product_id:
                    temp=True
    if product_id:
        if temp==False:
            i.order[product_id]=1
            i.save()

    products=[]
    quant=[]
    cost=0
    shipping=0
    total=0
    for j in i.order:
        if j!="null":
            p=product.objects.get(id=j)
            quant.append(i.order[j])
            cost=cost+p.price*i.order[j]
            shipping=shipping+30*i.order[j]
            products .append(p)
    total=cost+shipping
    ziped=zip(products,quant)
    return render(request, 'app/addtocart.html',{'cost':cost,'shipping':shipping,'total':total,'ziped':ziped})

def buy_now(request):
    if not request.user.is_authenticated:
        return redirect('/login')
    current_user = request.user
    user_email = current_user.email
    product_id = request.GET.get('query_name')
    i = user_detail.objects.get(user_email=user_email)
    if product_id:
        i.order_buynow=product_id
        i.quant_buynow=1
        i.save()
    quant=i.quant_buynow
    if quant<1:
        quant=1
    cost=0
    shipping=0
    total=0
    p=product.objects.get(id=i.order_buynow)
    cost=p.price*quant
    shipping=30*quant
    total=cost+shipping
    return render(request, 'app/buynow.html',{'cost':cost,'shipping':shipping,'total':total,'i':p,'j':quant})
   
def buyadd(request):
    if not request.user.is_authenticated:
        return redirect('/login')
    current_user = request.user
    user_email = current_user.email
    i = user_detail.objects.get(user_email=user_email)
    i.quant_buynow=i.quant_buynow+1
    i.save()
    return redirect('/buy')

def buysub(request):
    if not request.user.is_authenticated:
        return redirect('/login')
    current_user = request.user
    user_email = current_user.email
    i = user_detail.objects.get(user_email=user_email)
    product_id=i.order_buynow
    i.quant_buynow=i.quant_buynow-1
    i.save()
    quant=i.quant_buynow
    p=product.objects.get(id=product_id)
    cost=p.price*quant
    shipping=30*quant
    total=cost+shipping
    return redirect('/buy')

def profile(request):
    if request.method=="POST":
        address1=request.POST['address1']
        city=request.POST['city']
        state=request.POST['state']
        zip=request.POST['zip']
        current_user = request.user
        user_email = current_user.email
        if address1=="":
            messages.info(request,'please fill the address')
            return redirect('/profile')
        if city=="":
            messages.info(request,'please fill the city')
            return redirect('/profile')
        if state=="":
            messages.info(request,'please fill the state')
            return redirect('/profile')
        if zip=="":
            messages.info(request,'please fill the zip')
            return redirect('/profile')
        i = user_detail.objects.get(user_email=user_email)
        # x=user_detail.objects.create(user_email=user_email,user_address1=address1,user_address2=address2,user_city=city,user_state=state,user_zip=zip)
        i.user_address1=address1
        i.user_city=city
        i.user_state=state
        i.user_zip=zip
        i.save()
        messages.info(request,' succesful')
    return render(request, 'app/profile.html')

def address(request):
    current_user = request.user
    user_email = current_user.email
    i = user_detail.objects.get(user_email=user_email)
    if i.user_address1=="":
        messages.info(request,'please fill the address first')
        return redirect('/profile')
    return render(request, 'app/address.html',{'i':i,'j':current_user})

def orders(request):
    if request.user.is_authenticated:
        current_user = request.user
        user_email = current_user.email
        # if not user_detail.objects.filter(user_email=user_email).exists():
        #     messages.info(request,'please complete the profile first')
        #     return redirect('/profile')
        i = user_detail.objects.get(user_email=user_email)
        products=[]
        quant=[]
        date=[]
        for j in i.order_history:
            o=order.objects.get(id=j)
            p=product.objects.get(id=o.product_id)
            products.append(p)
            quant.append(o.quant)
            date.append(o.created_date)
        ziped=zip(products,quant,date)
    else:
        return render(request,'app/orders.html')
    return render(request, 'app/orders.html',{'zip':ziped})

def change_password(request):
 if request.method=="POST":
            New_Password=request.POST['New Password']
            Confirm_New_Password=request.POST['Confirm New Password']
            if New_Password!=Confirm_New_Password:
                messages.info(request,'password doesnot match')
            else:
                current_user = request.user
                current_user.set_password(New_Password)
                current_user.save()
                messages.info(request,'password change sucessfully kindly login again')

 return render(request, 'app/changepassword.html')

def mobile(request):
 products=product.objects.all()
 return render(request, 'app/mobile.html',{'products':products})

def laptop(request):
 products=product.objects.all()
 return render(request, 'app/laptop.html',{'products':products})

def login(request):
        if request.method=="POST":
            username=request.POST['email']
            password=request.POST['password']
            user=auth.authenticate(username=username,password=password)
            if user is not None:
                auth.login(request,user)
                return redirect('/')
            else:
                messages.info(request,'credential invalid')
                return redirect('login')
        
        return render(request, 'app/login.html')

def customerregistration(request):
    if request.method=='POST':
        first_name=request.POST['firstname']
        last_name=request.POST['lastname']
        email=request.POST['email']
        password=request.POST['password']
        confirmpassword=request.POST['password2']
        username=email
        var=False
        if email=='':
            var=True
            messages.info(request,'please enter email')
        if first_name=='':
            var=True
            messages.info(request,'please enter your first name')
        if last_name=='':
            var=True
            messages.info(request,'please enter your last name')
        if password=='':
            var=True
            messages.info(request,'please enter password')
        if confirmpassword=='':
            var=True
            messages.info(request,'please re enter password')
            
    
        if var==False:
            if password==confirmpassword:
                if User.objects.filter(email=email).exists():
                    messages.info(request,'email already exists')
                    return render(request, 'app/customerregistration.html')
                else:
                    user=User.objects.create_user(username=username,first_name=first_name,last_name=last_name,password=password,email=email)
                    user.save()
                    x=user_detail.objects.create(user_email=email)
                    x.save()
                    messages.info(request,'registeration succesful')
            else:
                messages.info(request,'password doesnot match try again')
    return render(request, 'app/customerregistration.html')

def checkout(request):
    # i = product.objects.get(id=product_id) 
    current_user = request.user
    user_email = current_user.email
    i = user_detail.objects.get(user_email=user_email)
    # j=user.objects
    # i.order={'5':'6'}
    if i.user_address1=="":
        messages.info(request,'please fill the address first')
        return redirect('/profile')

    products=[]
    quant=[]
    cost=0
    shipping=0
    total=0
    for j in i.order:
        if j!="null":
            p=product.objects.get(id=j)
            cost=cost+p.price*i.order[j]
            shipping=shipping+i.order[j]*30
            products .append(p)
            quant.append(i.order[j])
    total=cost+shipping
    ziped=zip(products,quant)
    return render(request, 'app/checkout.html',{'zip':ziped,'total':total,'k':i})

def checkoutbuynow(request):
    current_user = request.user
    user_email = current_user.email
    i = user_detail.objects.get(user_email=user_email)
    if i.user_address1=="":
        messages.info(request,'please fill the address first')
        return redirect('/profile')
    product_id=i.order_buynow
    p=product.objects.get(id=product_id)
    j=i.quant_buynow
    total=p.price*j+30*j
    return render(request,'app/checkoutbuynow.html',{'k':i,'i':p,'j':j,'total':total})

def topwear(request):
    products=product.objects.all()
    return render(request,'app/topwear.html',{'products':products})
def bottomwear(request):
    products=product.objects.all()
    return render(request,'app/bottomwear.html',{'products':products})

def logout(request):
    auth.logout(request)
    return redirect('/')

def add_to_cart1(request): 
    # removing item
    product_id = request.GET.get('query_name')
    current_user = request.user
    user_email = current_user.email
    i = user_detail.objects.get(user_email=user_email)
    i.order.pop(product_id)
    i.save()
    products=[]
    for j in i.order:
        if j!='null':
            products .append(product.objects.get(id=j))
    return redirect('/cart')

def add_to_cart2(request):
    # increasing quantity
    product_id = request.GET.get('query_name')
    # i = product.objects.get(id=product_id) 
    current_user = request.user
    user_email = current_user.email
    i = user_detail.objects.get(user_email=user_email)
    # i.order={'5':'6'}
    temp=i.order[product_id]+1
    i.order[product_id]=temp
    i.save()
    products=[]
    for j in i.order:
        if j!='null':
            products .append(product.objects.get(id=j))
    
    return redirect('/cart')

def add_to_cart3(request):
    # decreasing quantity
    product_id = request.GET.get('query_name')
    # i = product.objects.get(id=product_id) 
    current_user = request.user
    user_email = current_user.email
    i = user_detail.objects.get(user_email=user_email)
    # i.order={'5':'6'}
    temp=i.order[product_id]-1
    if temp==0:
        return redirect('/cart')
    i.order[product_id]=temp
    i.save()
    products=[]
    for j in i.order:
        if j!='null':
            products .append(product.objects.get(id=j))
    
    return redirect('/cart')

def order_placed(request):
    current_user = request.user
    user_email = current_user.email
    i = user_detail.objects.get(user_email=user_email)
    for j in i.order:
        o=order.objects.create(product_id=j,quant=i.order[j],user_email=user_email)
        o.save()
        i.order_history[o.id]=1
    i.order={}
    i.save()
    return redirect('/orders')

def order_placed_buy_now(request):
    # print('yes')
    current_user = request.user
    user_email = current_user.email
    i = user_detail.objects.get(user_email=user_email)
    j=i.order_buynow
    quant=i.quant_buynow
    o=order.objects.create(product_id=j,quant=quant,user_email=user_email)
    o.save()
    i.order_history[o.id]=1
    i.save()
    return redirect('/orders')

