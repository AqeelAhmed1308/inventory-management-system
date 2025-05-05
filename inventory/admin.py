from django.contrib import admin
from .models import Store, Category, Product, Staff, Manager

admin.site.register(Store)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Staff)
admin.site.register(Manager)
