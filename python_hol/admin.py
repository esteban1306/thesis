from models import Employees, Jobs
from django.contrib import admin

class EmployeeAdmin(admin.ModelAdmin):
	list_display = ('first_name', 'last_name', 'email', 'phone_number', 'hire_date', 'salary')
	list_filter = ['hire_date']
	search_fields = ['last_name']
	date_hierarchy = 'hire_date'

	admin.site.register(Employees)
	admin.site.register(Jobs)
	#Este es un comentario de prueba