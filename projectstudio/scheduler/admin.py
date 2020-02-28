from django.contrib import admin
from .models import Artist, Studio, Engineer, Session

# Register your models here.
admin.site.register(Artist)
admin.site.register(Studio)
admin.site.register(Engineer)
admin.site.register(Session)
