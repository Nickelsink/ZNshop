from django.contrib import admin

# Register your models here.
from shop.models import Goods, News

admin.site.register(Goods)
admin.site.register(News)