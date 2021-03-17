from django.contrib import admin
from .models import Blogs,Contact,BlogComment,Carosel

# Register your models here.

admin.site.register(Blogs)
admin.site.register(Contact)
admin.site.register(BlogComment)
admin.site.register(Carosel)

