from django.contrib import admin

# Register your models here.
from users.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone_number', 'website', 'picture')
    list_display_links = ('user', 'phone_number')
    list_editable = ('website', 'picture')
    list_filter = ('created', 'modified', 'user__is_active', 'user__is_staff')
    search_fields = ('user__email', 'user__firstname',
                     'user__lastname', 'phone_number')
