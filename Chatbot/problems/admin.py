from django.contrib import admin

from .models import Problem

class ProblemAdmin(admin.ModelAdmin):
    list_display = ("p_id", "p_statement",)

admin.site.register(Problem, ProblemAdmin)