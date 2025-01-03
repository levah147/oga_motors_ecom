from django.contrib import admin
from core.models import Product, Category, Vendor, CartOder, CartOderItems, ProductImages, ProductReview, WishList, Address

class ProductImagesAdmin(admin.TabularInline):
    model = ProductImages

class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImagesAdmin]
    list_display = [ 'user', 'title', 'product_image','price', 'category','vendor','featured','product_status']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title','category_image']

class VendorAdmin(admin.ModelAdmin):
    list_display = ['title','vendor_image']



class CartOrderAdmin(admin.ModelAdmin):
    list_display = ['user','price','paid_status','order_date','product_status']
    
class CartOrderItemsAdmin(admin.ModelAdmin):
    list_display = ['order','invoice_no','item','image','qty','price','total']


class ProductReviewAdmin(admin.ModelAdmin):
    list_display = ['user','product','review', 'rating']
      
class WishListAdmin(admin.ModelAdmin):
    list_display = ['user','product', 'date']

class AddressAdmin(admin.ModelAdmin):
    list_display = ['user','address','status']


class WishAdressListAdmin(admin.ModelAdmin):
    list_display = ['user','address','status']
    
      
    

    
    admin.site.register(Product, ProductAdmin)
    admin.site.register(Category, CategoryAdmin)
    admin.site.register(Vendor, VendorAdmin)
    admin.site.register(CartOder, CartOrderAdmin)
    admin.site.register(CartOderItems, CartOrderItemsAdmin)
    admin.site.register(ProductReview, ProductReviewAdmin)
    admin.site.register(WishList, WishListAdmin)
    admin.site.register(Address, AddressAdmin)
    
