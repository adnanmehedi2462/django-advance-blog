from django.contrib import admin
from .models import (author,categary,artical,comment)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name','details','profile_pic']
    search_fields =['details',]
    list_per_page=10

    class Meta:
        Model=author
admin.site.register(author,AuthorAdmin)
class CategoryAdmin(admin.ModelAdmin):

    search_fields =['name',]
    list_per_page=10


    class Meta:
        Model=categary
admin.site.register(categary,CategoryAdmin)

class ArticalAdmin(admin.ModelAdmin):
    list_display = ['title','posted_on']
    search_fields =['title',]
    list_per_page=10
    list_filter=['posted_on',"categary"]

    class Meta:
        Model=artical
admin.site.register(artical,ArticalAdmin)

class commentadmin(admin.ModelAdmin):
    class Meta:
        Model=comment
admin.site.register(comment,commentadmin)
