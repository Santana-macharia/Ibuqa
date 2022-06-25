from django.contrib import admin
from .models import Users
from .models import Customers
from .models import Orders

admin.site.register(Users)
admin.site.register(Customers)
admin.site.register(Orders)