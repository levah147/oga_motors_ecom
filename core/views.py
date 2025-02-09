from django.shortcuts import render
from core.models import Product, Category, Vendor, CartOder, CartOderItems, ProductImages, ProductReview, WishList, Address

# Create your views here.

def index(request):
    # product = Product.objects.all().order_by(("-id"))
    product = Product.objects.filter(product_status="published", featured =True)

    context ={
        'products':product
    }
    return render (request,'core/index13.html',context)


def product_list_view(request):
    product = Product.objects.filter(product_status="published")


    context ={
        'products':product
    }
    return render (request,'core/product_list.html',context)


def category_list(request):
    category = Category.objects.all()

    context ={
        'categorys':category
    }
    return render (request,'core/category_list.html',context)



def category_product_list(request, cid):
    category = Category.objects.get(cid=cid)
    products =Product.objects.filter(product_status="published",category=category)
    context = {
        'category':category,
        'products':products,
    }
    return render(request, 'core/category-product-list.html', context)


def vendor_list_view(request):
    vendors =Vendor.objects.all()
    context = {
        "vendors":vendors
    }
    return render(request, 'core/vendor-list.html',context)


def vendor_detail_view(request, vid):
    vendor =Vendor.objects.get(vid=vid)
    context = {
        "vendor":vendor
    }
    return render(request, 'core/vendor_detail_view.html',context)