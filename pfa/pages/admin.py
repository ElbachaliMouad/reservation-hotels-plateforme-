from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import  Membre, Invitation , Workshop
from django.contrib.auth.admin import UserAdmin
from .models import Picture



class MembreAdmin(admin.ModelAdmin):
    list_display = ('username', 'email','code_invitation','password','type')

# Register your models here.

admin.site.register(Membre, MembreAdmin)

class WorkshopAdmin(admin.ModelAdmin):
    list_display=('name','owner','description','image')


admin.site.register(Workshop, WorkshopAdmin)


class InvitationAdmin(admin.ModelAdmin):
    list_display = ('code', 'valeur')  # Display specific fields

admin.site.register(Invitation, InvitationAdmin)



class PictureAdmin(admin.ModelAdmin):
    list_display = list_display = ('title', 'owner', 'image','image_hash','description')


admin.site.register(Picture, PictureAdmin)
