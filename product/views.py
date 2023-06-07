from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from datetime import date, timedelta
from django.db.models import Count

from .utilities import notify_admin, search_products
from .models import Product


# Create your views here.
@login_required(login_url='authentication:login')
def add_product(request):
    if request.method == "POST":
        Name = request.POST.get('Name')
        Manufacturer = request.POST.get('Manufacturer')
        BarCode = request.POST.get('BarCode')
        ProductionDate = request.POST.get('ProductionDate')
        ExpiryDate = request.POST.get('ExpiryDate')
        Quantity = request.POST.get('Quantity')
        Price = request.POST.get('Price')
        Product.objects.create(
            Name=Name,
            Manufacturer=Manufacturer,
            BarCode=BarCode,
            ProductionDate=ProductionDate,
            ExpiryDate=ExpiryDate,
            Quantity=Quantity,
            Price=Price
        )
        return redirect("product:products")


@login_required(login_url='authentication:login')
def edit_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        product.Name = request.POST.get('Name')
        product.Manufacturer = request.POST.get('Manufacturer')
        product.BarCode = request.POST.get('BarCode')
        if request.POST.get('ProductionDate'):
            product.ProductionDate = request.POST.get('ProductionDate')
        if request.POST.get('ExpiryDate'):
            product.ExpiryDate = request.POST.get('ExpiryDate')
        product.Quantity = request.POST.get('Quantity')
        product.Price = request.POST.get('Price')
        product.save()
        return redirect("product:products")
    return render(request, "edit.html", {"product": product})


@login_required(login_url='authentication:login')
def expired_products_view(request):
    today = date.today()
    expired_products = Product.objects.filter(ExpiryDate__lt=today)
    total_products = expired_products.count()
    total_expired_products = expired_products.filter(ExpiryDate__lt=today).count()
    total_batches = expired_products.values('Manufacturer').annotate(total=Count('Manufacturer')).count()
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'addProduct':
            add_product(request)
            return render(request, "index.html", {'products': expired_products})
        # Send email
        subject = "Expired Products"
        notify_admin(subject, expired_products)
        return HttpResponse('Email sent successfully!')
    return render(request, "index.html",
                  {'products': expired_products,
                   'total_products': total_products,
                   'total_expired_products': total_expired_products,
                   'total_batches': total_batches}
                  )


def expiring_products_view(request, month):
    today = date.today()
    print(today)
    print(month)
    print(timedelta(days=int(month)) * 30)
    threshold_date = today + timedelta(days=int(month)) * 31
    print(threshold_date)
    expiring_products = Product.objects.filter(ExpiryDate__lte=threshold_date)
    total_products = expiring_products.count()
    total_expired_products = expiring_products.filter(ExpiryDate__lt=today).count()
    total_batches = expiring_products.values('Manufacturer').annotate(total=Count('Manufacturer')).count()
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'addProduct':
            add_product(request)
            return render(request, "index.html", {'products': expiring_products})
        # Send email
        subject = "Products due to expire"
        notify_admin(subject, expiring_products)
        return HttpResponse('Email sent successfully!')
    return render(request, "index.html",
                  {'products': expiring_products,
                   'total_products': total_products,
                   'total_expired_products': total_expired_products,
                   'total_batches': total_batches}
                  )


@login_required(login_url='authentication:login')
def products(request):
    product_list = Product.objects.all()
    total_products = product_list.count()
    total_expired_products = product_list.filter(ExpiryDate__lt=date.today()).count()
    total_batches = product_list.values('Manufacturer').annotate(total=Count('Manufacturer')).count()
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'addProduct':
            add_product(request)
            return render(request, "index.html", {'products': product_list})
        # Send email
        subject = "Details about all products"
        notify_admin(subject, product_list)
        return HttpResponse('Email sent successfully!')
    return render(request, "index.html",
                  {'products': product_list,
                   'total_products': total_products,
                   'total_expired_products': total_expired_products,
                   'total_batches': total_batches}
                  )


@login_required(login_url='authentication:login')
def search(request):
    query = request.GET.get('q')
    product_list = search_products(query)
    total_products = product_list.count()
    total_expired_products = product_list.filter(ExpiryDate__lt=date.today()).count()
    total_batches = product_list.values('Manufacturer').annotate(total=Count('Manufacturer')).count()
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'addProduct':
            add_product(request)
            return render(request, "index.html", {'products': product_list})
        # Send email
        subject = "Details about searched products"
        notify_admin(subject, product_list)
        return HttpResponse('Email sent successfully!')
    return render(request, "index.html",
                  {'products': product_list,
                   'total_products': total_products,
                   'total_expired_products': total_expired_products,
                   'total_batches': total_batches}
                  )


@login_required(login_url='authentication:login')
def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.delete()
    return redirect('product:products')
