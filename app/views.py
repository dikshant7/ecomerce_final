from django.shortcuts import render
from .models import product, user_detail
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
    product_id = request.GET.get('query_name')
    # i = product.objects.get(id=product_id) 
    current_user = request.user
    user_email = current_user.email
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
    return render(request, 'app/addtocart.html',{'products':products,'cost':cost,'shipping':shipping,'total':total,'ziped':ziped})

def buy_now(request):
 return render(request, 'app/buynow.html')

def profile(request):
    if request.method=="POST":
        address1=request.POST['address1']
        address2=request.POST['address2']
        city=request.POST['city']
        state=request.POST['state']
        zip=request.POST['zip']
        current_user = request.user
        user_email = current_user.email
        if user_detail.objects.filter(user_email=user_email).exists():
             messages.info(request,'email already exists')
             return render(request, 'app/profile.html')
        x=user_detail.objects.create(user_email=user_email,user_address1=address1,user_address2=address2,user_city=city,user_state=state,user_zip=zip)
        x.save()
        messages.info(request,' succesful')
    return render(request, 'app/profile.html')

def address(request):
    current_user = request.user
    user_email = current_user.email
    i = user_detail.objects.get(user_email=user_email)
    return render(request, 'app/address.html',{'i':i})

def orders(request):
 return render(request, 'app/orders.html')

def change_password(request):
 return render(request, 'app/changepassword.html')

def mobile(request):
 return render(request, 'app/mobile.html')

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
                    messages.info(request,'registeration succesful')
            else:
                messages.info(request,'password doesnot match try again')
    return render(request, 'app/customerregistration.html')

def checkout(request):
    # i = product.objects.get(id=product_id) 
    current_user = request.user
    user_email = current_user.email
    i = user_detail.objects.get(user_email=user_email)
    # i.order={'5':'6'}
    products=[]
    cost=0
    shipping=0
    total=0
    for j in i.order:
        if j!="null":
            p=product.objects.get(id=j)
            cost=cost+p.price*i.order[j]
            shipping=shipping+i.order[j]*30
            products .append(p)
    total=cost+shipping
    return render(request, 'app/checkout.html',{'products':products,'total':total})

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
