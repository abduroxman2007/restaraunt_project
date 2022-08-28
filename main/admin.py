from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Branch)
admin.site.register(Client)
admin.site.register(Food)
admin.site.register(Table)
admin.site.register(TableOrder)
admin.site.register(OrderFood)
admin.site.register(Rating)