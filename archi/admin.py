from django.contrib import admin
from .models import Recipe, Update, Category

# Register your models here.
admin.site.register(Recipe)
admin.site.register(Update)
admin.site.register(Category)
