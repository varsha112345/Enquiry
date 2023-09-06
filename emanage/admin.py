from django.contrib import admin

# Register your models here.
from .models import *
# Register your models here.
admin.site.register(Enquiry)
admin.site.register(Reason_follow)
admin.site.register(reason_for_follow_up)
admin.site.register(Cource)
admin.site.register(system_details)
admin.site.register(Category)
admin.site.register(Allocation)
admin.site.register(Desktop)
admin.site.register(Compulsory)
admin.site.register(Optional)