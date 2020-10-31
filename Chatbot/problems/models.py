from django.db import models


class Problem(models.Model):
    p_id = models.IntegerField(primary_key=True, auto_created=True)
    p_statement = models.CharField(max_length=1000, blank=False)
    p_tags = models.CharField(max_length=1000, blank=False)
    p_rating = models.IntegerField()
    p_A = models.CharField(blank=False, max_length=100)
    p_B = models.CharField(blank=False, max_length=100)
    p_C = models.CharField(max_length=100)
    p_D = models.CharField(max_length=100)
    p_E = models.CharField(max_length=100)
    p_correct = models.CharField(blank=False, max_length=100)

    class Meta:
      verbose_name_plural = "problems"

    def __str__(self):
        return self.name