from django.contrib import admin
from .models import Places,Services,Booking,Members
# Register your models here.
admin.site.register(Places)
admin.site.register(Services)
admin.site.register(Members)
admin.site.register(Booking)