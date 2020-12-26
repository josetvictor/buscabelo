from django.contrib import admin

from .models import *

admin.site.register(User)
admin.site.register(Customer)
admin.site.register(Establishment)
admin.site.register(Comment)
admin.site.register(Service)
admin.site.register(EstablishmentGalleryImage)
admin.site.register(Scheduling)