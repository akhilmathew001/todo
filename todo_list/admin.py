from django.contrib import admin

# Register your models here.

from todo_list.models import TodoList


class TodoListAdmin(admin.ModelAdmin):
	date_hierarchy = 'date_due'
	list_filter = ('state','date_due',)
	list_display = ('name_of_the_task','state')
	exclude = ['color_code']
	
admin.site.register(TodoList,TodoListAdmin)
