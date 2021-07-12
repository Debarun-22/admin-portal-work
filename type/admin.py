from django.contrib import admin
from .models import Type,Post
# Register your models here.
class TypeAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('type_name',)}
    list_display = ('type_name','category','modified_date')

class PostAdmin(admin.ModelAdmin):
    list_display = ('user','created_date','to_post_date')


admin.site.register(Type,TypeAdmin)
admin.site.register(Post,PostAdmin)