from __future__ import unicode_literals
from django.utils.html import format_html
from django.db import models

# Create your models here.


class TodoList(models.Model):
	
	priority_choice = (('1','High'),('2','Medium'),('3','Low'))
	state_choice = (('To Do','To Do'),('Doing','Doing'),('Done','Done'))
	
	
	name = models.CharField(max_length=200)
	description = models.TextField('Description')
	priority = models.CharField(max_length=200,choices=priority_choice,default='2')
	date_due = models.DateField('Due Date')
	state = models.CharField(max_length=200,choices=state_choice,default='To Do')
	
	color_code = models.CharField(max_length=6, blank=True)
	
	def __str__(self):
		return self.name
		
	def name_of_the_task(self):
		return format_html('<span style="color: #{};">{}</span>', 
		   self.color_code,self.name)
		   
		   
	def save(self, *args, **kwargs):
		if self.state == 'To Do':
			self.color_code = 'FF00BF'
		elif self.state == 'Doing':
			self.color_code = '0101DF'
		elif self.state == 'Done':
			self.color_code = '00FF7F'	
		return super(TodoList,self).save(*args, **kwargs)		
		      
		   
	
	