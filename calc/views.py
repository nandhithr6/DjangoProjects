from django.shortcuts import render, redirect

from calc.models import Customer, Product, Order

# # Create your views here.
# def home(request): 
#     return render(request, 'home.html', {'name':'Home'})


# def add(request):
#     val1 = int(request.POST['num1'])
#     val2 = int(request.POST['num2'])
#     val3 = val1+val2
#     return render(request,'result.html',{'result':val3}) 


# def dashboard(request):
#     customers=Customer.objects.all()
#     orders=Order.objects.all()
#     return render(request, 'dashboard.html', {'customers': customers, 'orders': orders})

# def products(request):
#     products=Product.objects.all()
#     return render(request,'product.html', {'products': products})

# def customer(request, pk_test):
#     customer=Customer.objects.get(id=pk_test)
#     customers=Customer.objects.all()
#     orders=customer.order_set.all()
#     order_count=orders.count()
#     context={'customers':customers, 'cust':customer,'orders':orders,'ordcount':order_count}
#     return render(request,'customer.html',context)

# from .forms import OrderForm

# def createOrder(request):
#     form = OrderForm()
#     if request.method == "POST":
#         form = OrderForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('/')
#     context = {'form': form}
#     return render(request, 'order_form.html', context)

# from django.shortcuts import render, redirect, get_object_or_404

# def updateOrder(request, pk):
#     order = get_object_or_404(Order, id=pk)  
#     form = OrderForm(instance=order)
#     if request.method == "POST":
#         form = OrderForm(request.POST, instance=order)  
#         if form.is_valid():
#             form.save() 
#             return redirect('/')
#     context = {'form': form}
#     return render(request, 'order_form.html', context) 

# def deleteOrder(request, pk):
#     order = get_object_or_404(Order, id=pk)  
#     if request.method == "POST":
#         order.delete()  
#         return redirect('/')  

#     context = {'item': order}
#     return render(request, 'delete.html', context)

def home(request):
    customers = Customer.objects.all()
    return render(request, 'home.html', {'customers': customers})

def insertData(request):
    if request.method == "POST":
        name = request.POST['nameVar']
        age = request.POST['ageVar']
        Customer.objects.create(name=name, age=age)
    customers = Customer.objects.all()
    return render(request, 'home.html', {'customers': customers})
