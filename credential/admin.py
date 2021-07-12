from django.contrib import admin
from .models import Credential
# Register your models here.

class CredentialAdmin(admin.ModelAdmin):
    list_display = ('user','category','email','phone_no')

admin.site.register(Credential,CredentialAdmin)