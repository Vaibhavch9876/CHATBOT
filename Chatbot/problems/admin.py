from django.contrib import admin

from .models import Problem

class ProblemAdmin(admin.ModelAdmin):
    # p_id = models.AutoField(primary_key=True)
    # p_statement = models.TextField(max_length=1000, blank=False)
    # p_tags = models.CharField(max_length=1000, blank=False)
    # p_rating = models.IntegerField()
    # p_A = models.CharField(blank=False, max_length=100)
    # p_B = models.CharField(blank=False, max_length=100)
    # p_C = models.CharField(max_length=100, blank=True)
    # p_D = models.CharField(max_length=100, blank=True)
    # p_E = models.CharField(max_length=100, blank=True)
    # p_correct = models.CharField(blank=False, max_length=100)
    list_display = ("p_id", "p_statement", "p_tags" , "p_rating" , "p_A" , "p_B" , "p_C" , "p_D" , "p_E" , "p_correct")

admin.site.register(Problem, ProblemAdmin)