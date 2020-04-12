from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.models import UserProfile, Account

admin.site.register(UserProfile)


class AccountAdmin(UserAdmin):
    list_display = ('username', 'email', 'pk', 'last_login', 'date_joined')
    search_fields = ('username', 'email', 'pk',)
    readonly_fields = ('date_joined', 'last_login')

    filter_horizontal = ()
    filter_vertical = ()
    fieldsets = ()
    list_filter = ()



admin.site.register(Account, AccountAdmin)