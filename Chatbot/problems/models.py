from django.db import models


class Problem(models.Model):
    p_id = models.AutoField(primary_key=True)
    p_statement = models.TextField(max_length=1000, blank=False)
    p_tags = models.CharField(max_length=1000, blank=False)
    p_rating = models.IntegerField()
    p_A = models.CharField(blank=False, max_length=100)
    p_B = models.CharField(blank=False, max_length=100)
    p_C = models.CharField(max_length=100, blank=True)
    p_D = models.CharField(max_length=100, blank=True)
    p_E = models.CharField(max_length=100, blank=True)
    p_correct = models.CharField(blank=False, max_length=100)

    class Meta:
      verbose_name_plural = "problems"

    def __str__(self):
        res =  self.p_statement
        res += "Options : ";
        if self.p_A != None :
            res+= " " + self.p_A
        if self.p_B != None :
            res+= " " + self.p_B
        if self.p_C != None :
            res+= " " + self.p_C
        if self.p_D != None :
            res+= " " + self.p_D
        if self.p_E != None :
            res+= " " + self.p_E
        return res
