from django.contrib import admin
from .models import Category, FoodItem
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields  = {'slug': ('category_name',)} #De khi go ten thi slug hien theo
    list_deplay = ('category_name', 'vendor', 'updated_at') #Hien display o trang admin django
    search_fields = ('category_name', 'vendor__vendor_name') #Chuyen doi du lieu nguoc tu khoa ngoai

class FoodItemAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('food_title',)}
    list_diplay = ('food_title', 'category', 'vendor', 'price', 'is_available', 'price')
    search_fields = ('food_title', 'category__category_name', 'vendor_vendor_name', 'price')
    list_filter = ('is_available',)

admin.site.register(Category, CategoryAdmin)
admin.site.register(FoodItem, FoodItemAdmin)