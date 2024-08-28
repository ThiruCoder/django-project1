from django.db import models

# Create your models here.
class CollegeModel(models.Model):
    stu_name = models.CharField(max_length=50, blank=True, null=True)
    stu_dob = models.DateField()
    stu_course = models.CharField(max_length=30, null=True)
    address_city = models.CharField(max_length=50)

    def __str__(self):
        return self.stu_name

    class Meta():
        verbose_name = 'CollegeModel'
        verbose_name_plural = 'CollegeModels'

    

