from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from .models import Product
from product.utilities import search_products


# Create your views here.
@login_required(login_url='authentication:login')
def add_product(request):
    if request.method == "POST":
        Name = request.POST.get('Name')
        Manufacturer = request.POST.get('Manufacturer')
        ProductionDate = request.POST.get('ProductionDate')
        ExpiryDate = request.POST.get('ExpiryDate')
        Quantity = request.POST.get('Quantity')
        Price = request.POST.get('Price')
        Product.objects.create(Name, Manufacturer, ProductionDate, ExpiryDate, Quantity, Price)
        return redirect("add_product")
    return render(request, "add_product.html")


@login_required(login_url='authentication:login')
def edit_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        product.Name = request.POST.get('Name')
        product.Manufacturer = request.POST.get('Manufacturer')
        product.ProductionDate = request.POST.get('ProductionDate')
        product.ExpiryDate = request.POST.get('ExpiryDate')
        product.Quantity = request.POST.get('Quantity')
        product.Price = request.POST.get('Price')
        product.save()
        return redirect('edit_product', pk=product.pk)
    return render(request, "edit_product.html")


@login_required(login_url='authentication:login')
def products(request):
    product_list = Product.objects.all()
    return render(request, "index.html", {'products': product_list})


@login_required(login_url='authentication:login')
def search(request):
    query = request.GET.get('q')
    product_list = search_products(query)
    return render(request, 'search_results.html', {'products': product_list})


@login_required(login_url='authentication:login')
def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.delete()
    return redirect('products')
