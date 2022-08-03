from django.contrib import admin

# Register your models here.
from .models import Booking, Departments,Doctors

admin.site.register(Departments)
admin.site.register(Doctors)
class BookingAdmin(admin.ModelAdmin):
    list_display=('id','P_name','p_phone','P_email','doc_name','booking_date','booking_on')
admin.site.register(Booking,BookingAdmin)
