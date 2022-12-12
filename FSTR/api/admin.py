from django.contrib import admin
from .models import Users, PerevalImages, PerevalAdded, Coords, Level


admin.site.register(Users)
admin.site.register(PerevalAdded)
admin.site.register(PerevalImages)
admin.site.register(Coords)
admin.site.register(Level)
# Register your models here.
