from django.contrib import admin
from django.contrib import admin  
  
# Register your models here.  
 

# Register your models here.
from .models import Article,Reporter,Question,Choice,Fruits,Students,Employee,Todo,hello


admin.site.register(Article)
admin.site.register(Reporter)
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Fruits)
admin.site.register(Students) 
admin.site.register(Employee)
admin.site.register(Todo)
admin.site.register(hello)