from core.models import Product, Category, Vendor, CartOder, CartOderItems, ProductImages, ProductReview, WishList, Address


def default(request):
    Categories = Category.objects.all()

    return{
        'Categories':Categories,
    }

