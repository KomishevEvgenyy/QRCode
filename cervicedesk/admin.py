from django.contrib import admin

from .models import QRCode, QRZone, Feedback

admin.site.register(Feedback)
admin.site.register(QRCode)
admin.site.register(QRZone)

# Register your models here.
