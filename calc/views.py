from django.shortcuts import render

from calc.models import Customer, Product

# Create your views here.
def home(request): 
    return render(request, 'home.html', {'name':'Raju'})


def add(request):
    val1 = int(request.POST['num1'])
    val2 = int(request.POST['num2'])
    val3 = val1+val2
    return render(request,'result.html',{'result':val3}) 


def dashboard(request):
    customers=Customer.objects.all()
    return render(request, 'dashboard.html', {'customers': customers})

def products(request):
    products=Product.objects.all()
    return render(request,'product.html', {'products': products})

def customer(request, pk_test):
    customer=Customer.objects.get(id=pk_test)
    customers=Customer.objects.all()
    orders=customer.order_set.all()
    order_count=orders.count()
    context={'customers':customers, 'cust':customer,'orders':orders,'ordcount':order_count}
    return render(request,'customer.html',context)