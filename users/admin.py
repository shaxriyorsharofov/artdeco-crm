from django.contrib.auth.models import Group
from django.contrib import admin
from .models import User, CheckImage
# Register your models here.


class CheckImageAdmin(admin.TabularInline):
    model = CheckImage


class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'course_name', 'money_paid', 'status', 'course_percentage']
    list_filter = ['course_name', 'status', 'course_percentage']
    inlines = [CheckImageAdmin, ]


admin.site.register(User, UserAdmin)
admin.site.unregister(Group)

