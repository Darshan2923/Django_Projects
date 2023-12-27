from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Notes)




# class DescInline(admin.TabularInline):
#     model = Description
#     extra = 3


# class TitleAdmin(admin.ModelAdmin):
#     fieldsets = [
#         (None,               {'fields': ['title']}),
#     ]
#     inlines = [DescInline]



# admin.site.register(Title,TitleAdmin)
# admin.site.register(Description)
