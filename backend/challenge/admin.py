from django.contrib import admin
from .models import Challenge
# Register your models here.


class ChallengeAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'completed')


admin.site.register(Challenge, ChallengeAdmin)
