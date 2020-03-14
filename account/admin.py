from django.contrib import admin
from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'date_of_birth', 'photo', 'twitter', 'persional_detail', 'profession', 'twitter']


admin.site.register(Profile, ProfileAdmin)
