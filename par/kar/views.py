from django.shortcuts import render,redirect
from django.http import HttpResponse
from urllib import request
from django.views import View
from . models import Product
from django.db.models import Count
from . forms import RegistrationForm,PasswordChangeForm,CustomerProfileForm
from django.contrib import messages
from .models import Customer


# Create your views here.
def home(request):
    return render(request,"kar/home.html")

def about(request):
    return render(request,"kar/about.html")

def contact(request):
    return render(request,"kar/contact.html")

class CategoryView(View):
    def get(self,request,val):
        product = Product.objects.filter(category=val)
        title = Product.objects.filter(category=val).values('title')
        return render(request,"kar/category.html",locals())
    
class CategoryTitle(View):
    def get(self,request,val):
        product = Product.objects.filter(title=val)
        title = Product.objects.filter(category=product[0].category).values('title')
        return render(request,"kar/category.html",locals())

class ProductDetail(View):
    def get(self,request,pk):
        product = Product.objects.get(pk=pk)
        return render(request,"kar/productdetail.html",locals())

class RegistrationView(View):
    def get(self,request):
        form= RegistrationForm()
        return render(request,'kar/registration.html',locals())
    def post(self,request):
        form=RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"congratulation! User registered")
        else:
            messages.warning(request,"Invalid Input Data")
        return render(request,"kar/registration.html",locals())
    
class ProfileView(View):
    def get(self,request):
        form = CustomerProfileForm()
        return render(request,"kar/registration.html",locals())
    def post(self,request):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            user = request.user
            name = form.clean_data['name']
            locality = form.clean_data['locality']
            city = form.clean_data['city']
            mobile = form.clean_data['mobile']
            state = form.clean_data['state']
            zipcode = form.clean_data['zipcode']
            
            reg = Customer(user=user,name=name,city=city,locality=locality,mobile=mobile,state=state,zipcode=zipcode)
            reg.save()
            messages.success(request,'Congractulations! profile saved successfully')
        else:
            messages.warning(request,'Invalid input data')

        return render(request,"kar/registration.html",locals())

def address(request):
    add = Customer.objects.filter(user=request.user)
    return render(request, 'kar/address.html', locals())

class updateAddress(View):
    def get(self,request,pk):
        add = Customer.objects.get(pk=pk)
        form = CustomerProfileForm(instance=add)
        return render(request, 'kar/updateAddress.html', locals())
    def post(self,request,pk):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            add = Customer.objects.get(pk=pk)
            add.name = form.cleaned_data['name']
            locality = form.clean_data['locality']
            city = form.clean_data['city']
            mobile = form.clean_data['mobile']
            state = form.clean_data['state']
            zipcode = form.clean_data['zipcode']
            add.save()
            messages.success(request,'Congractulations! profile saved successfully')
        else:
            messages.warning(request,'Invalid input data')
        return redirect('address')





