from django.contrib import admin
from home.models import CollegeModel
# Register your models here.

class ModelAdmin(admin.ModelAdmin):
    list_display = ('id','stu_name','stu_dob','stu_course','address_city')

admin.site.register(CollegeModel,ModelAdmin)