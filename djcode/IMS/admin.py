from django.contrib import admin

# Register your models here.
from IMS.models import *

class CourseAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'credits', 'semester', 'textbook', 'college')
	search_fields = ('id', 'name')

admin.site.register(Student_user)
admin.site.register(Faculty_user)
admin.site.register(Admin_user)
admin.site.register(Course_info, CourseAdmin)
admin.site.register(Class_info)
#admin.site.register(Pre_requisites)
admin.site.register(Class_table)
#admin.site.register(Sys_log)
