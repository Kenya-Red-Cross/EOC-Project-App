from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group, Permission, PermissionsMixin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from .forms import  UserChangeForm, UserCreationForm

User = get_user_model()

# Remove Group Model from admin. We're not using it.
#admin.site.unregister(Group)


class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ['get_full_name','email','superuser','date_joined']
    readonly_fields = ['date_joined','superuser','last_login']
    list_filter =('date_joined',)
    
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('first_name','last_name','surname','phone_number','region')}),
        (_('Permissions'), {'fields': ('is_active','staff','superuser','groups')}),
        (_('Important dates'), {'fields': ('last_login','date_joined')}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password', 'password_2')}
        ),
    )
    search_fields = ['email']
    ordering = ['email']


admin.site.register(User, UserAdmin)