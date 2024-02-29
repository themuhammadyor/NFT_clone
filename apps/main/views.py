from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.utils.timezone import datetime

from apps.main.forms import ProductCreateForm, ProductUpdateForm
from apps.main.models import Product, Category


# Create your views here.
def index(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    return render(request, 'index.html',
                  {'products': products, 'categories': categories})


def author(request):
    return render(request, 'main/author.html')


def create(request):
    return render(request, 'main/create.html')


def details(request, pk):
    products = Product.objects.all()
    product = Product.objects.get(pk=pk)
    return render(request, 'main/details.html' , {'product': product, 'products': products})


def explore(request):
    return render(request, 'main/explore.html')


@login_required()
def post_create(request):
    if request.method == "POST":
        form = ProductCreateForm(request.POST)
        if form.is_valid():
            product = Product(name=form.cleaned_data["name"], description=form.cleaned_data["description"],
                              author=form.cleaned_data["author"], category=form.cleaned_data["category"],
                              price=form.cleaned_data["price"],
                              cover=form.cleaned_data["cover"], end_in=form.cleaned_data["end_in"],
                              owner=form.cleaned_data["owner"], like_count=form.cleaned_data["like_count"])
            product.author = request.user
            product.published = datetime.datetime.now().strftime("%Y-%m-%d")
            product.save()
            messages.success(request, "product successfully created")
            return redirect(reverse('main:user-profile', kwargs={"username": request.user.username}))
        else:
            return render(request, "main/product-create.html", {"form": form})
    else:
        form = ProductCreateForm()
        return render(request, "main/product-create.html", {"form": form})


@login_required()
def product_update(request, pk: int):
    product = Product.objects.get(pk=pk)
    if request.method == "POST":
        form = ProductUpdateForm(data=request.POST, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, "post successfully updated")
            return redirect(reverse('main:post-detail', kwargs={"pk": product.id}))
        else:
            return render(request, "main/product-update.html", {"form": form})
    else:
        form = ProductUpdateForm(instance=product)
        return render(request, "main/product-update.html", {"form": form})


@login_required()
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        messages.success(request, "post successfully deleted")
        product.delete()
        return redirect(reverse('main:user-profile', kwargs={"username": request.user.username}))
    else:
        return render(request, "main/product-confirm-delete.html", {"product": product})
