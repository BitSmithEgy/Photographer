from django.contrib import admin
from .models import Video, Package, HomeVideo, Videographer
# Register your models here.
admin.site.register(Package)
admin.site.register(Video)
admin.site.register(HomeVideo)
admin.site.register(Videographer)