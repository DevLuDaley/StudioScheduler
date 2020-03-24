from django.contrib import admin
from .models import Artist, Studio, Engineer, Session

# Register your models here.
# ? Is this valid? Can I refactor to use the logic below?
# admin.site.register(Artist, Studio, Engineer, Session)
admin.site.register(Artist)
admin.site.register(Studio)
admin.site.register(Engineer)
admin.site.register(Session)
