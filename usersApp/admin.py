from django.contrib import admin

from usersApp.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'email', 'city', 'phone', 'age']
